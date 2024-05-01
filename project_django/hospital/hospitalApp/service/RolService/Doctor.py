from hospitalApp import models
from django.forms.models import model_to_dict
from django.db import connection
from hospitalApp.validator import typeValidator
from hospitalApp.service import validatorService
from hospital.connection_mongo import collection
import json


def getBasicPatientInfo(idDocument: int):
    patient = models.Patient.objects.prefetch_related('emergencyContact', 'medicalInsurance').get(idDocument=idDocument)
    response = {"Patient": model_to_dict(patient), "EmergencyContact": model_to_dict(patient.emergencyContact),
                "MedicalInsurance": model_to_dict(patient.medicalInsurance)}
    return response


def getPatientClinicalHistory(idDocument: int) -> dict:
    if validatorService.validatePatientById(idDocument):
        clinicalHistories = collection.find_one({"_id": str(idDocument)})
        return clinicalHistories


def getAppointmentsMade(idDocument: int) -> list:
    if validatorService.validatePatientById(idDocument) and models.ClinicalVisit.objects.filter(
            idPatient=idDocument).exists():
        visits = models.ClinicalVisit.objects.values().filter(idPatient=idDocument)
        return list(visits)
    else:
        raise Exception("No se encontraron visitas para el paciente")


def getAppointments(patientDocument: int) -> list:
    if validatorService.validatePatientById(patientDocument):
        appointments = models.MedicalAppointment.objects.values().filter(idPatient=patientDocument)
        return list(appointments)
    else:
        raise Exception("No se encontraron citas para el paciente")


def generateHistory(patientDocument: int, doctorDocument: int, date: str, consultReason: str, symptomatology: str,
                    diagnosis: str):
    if models.ClinicalHistory.objects.filter(idPatient=patientDocument, date=date, idDoctor=doctorDocument).exists():
        raise Exception("Ya existe una historia clinica para el paciente en la fecha especificada")
    if validatorService.validatePatientById(patientDocument) and validatorService.validateDoctorById(
            doctorDocument) and typeValidator.validDate(date):
        patient = models.Patient(**validatorService.getPatientById(patientDocument))
        doctor = models.Employee(**validatorService.getEmployeeById(doctorDocument))
        newClinicalHistory = models.ClinicalHistory(idPatient=patient, idDoctor=doctor,
                                                    consultReason=consultReason,
                                                    symptomatology=symptomatology, diagnosis=diagnosis, date=date)
        newClinicalHistory.save()
        clinicalHistoryData = {
            key: value for key, value in vars(newClinicalHistory).items() if key != '_state'
        }
        patientData = {
            key: value for key, value in vars(patient).items() if key != '_state'
        }
        doctorData = {
            key: value for key, value in vars(doctor).items() if key != '_state'
        }
        clinicalHistoryData["Patient"] = patientData
        clinicalHistoryData["Doctor"] = doctorData
        del clinicalHistoryData["idPatient_id"]
        del clinicalHistoryData["idDoctor_id"]

        collection.update_one(
            {"_id": str(patientDocument)},
            {"$set": {f"histories.{newClinicalHistory.date}": clinicalHistoryData}}
        )


    else:
        raise Exception("No se pudo generar la historia clinica, valida los datos")


def generateOrder(idPatient: int, idDoctor: int, idClinicalHistory: int):
    if validatorService.validatePatientById(idPatient) and validatorService.validateDoctorById(idDoctor):
        clinicalHistory = models.ClinicalHistory.objects.get(id=idClinicalHistory)
        actualOrder = models.Order(idClinicalHistory=clinicalHistory)
        actualOrder.save()
        collection.update_one(
            {"_id": str(idPatient)},
            {"$set": {f"histories.{clinicalHistory.date}.order": {"id": actualOrder.id}}}
        )
    else:
        raise Exception("No se pudo generar la orden, valida los datos")


def generateOrderHelpDiagnostic(idPatient: int, idHistory: int, idOrder: int, item: int, helpDiagnostic: str, quantity: int,
                                amount: float):
    if models.OrderMedication.objects.filter(idOrder=idOrder).exists():
        raise Exception("No se puede agregar una ayuda diagnostica a una orden que ya tiene medicamentos")
    if models.OrderProcedure.objects.filter(idOrder=idOrder).exists():
        raise Exception("No se puede agregar una ayuda diagnostica a una orden que ya tiene procedimientos")
    if models.Order.objects.filter(id=idOrder).exists():
        try:
            clinicalHistory = models.ClinicalHistory.objects.get(id=idHistory)
            order = models.Order.objects.get(id=idOrder)
        except Exception as e:
            raise Exception(str(e))
        OrderHelpDiagnostic = models.OrderHelpDiagnostic()
        OrderHelpDiagnostic.idOrder = order
        OrderHelpDiagnostic.item = item
        OrderHelpDiagnostic.nameHelpDiagnostic = helpDiagnostic
        OrderHelpDiagnostic.quantity = quantity
        OrderHelpDiagnostic.amount = amount
        OrderHelpDiagnostic.save()

        helpDiagnosticData = {
            key: value for key, value in vars(OrderHelpDiagnostic).items() if
            key != '_state' and key != 'idClinicalHistory_id' and key != 'idOrder_id' and key != 'item'
        }
        collection.update_one(
            {"_id": str(idPatient)},
            {"$set": {f"histories.{clinicalHistory.date}.order.helpDiagnostic.items": {str(item): helpDiagnosticData}}}
        )
    else:
        raise Exception("No existe esa orden especificada")

#
def generateOrderMedication(idPatient: int, idOrder: int, item: int, idMedicine: int, dose: str, treatmentDuration: str,
                            amount: str):
    if models.OrderHelpDiagnostic.objects.filter(idOrder=idOrder).exists():
        raise Exception("No se puede agregar un medicamento a una orden que ya tiene ayuda diagnostica")
    if models.Order.objects.filter(id=idOrder).exists():
        try:
            order = models.Order.objects.get(id=idOrder)
            medication = models.Medication.objects.get(id=idMedicine)
            clinicalHistory = models.ClinicalHistory.objects.get(idPatient=idPatient)
        except Exception as e:
            raise Exception(str(e))
        OrderMedication = models.OrderMedication()
        OrderMedication.idOrder = order
        OrderMedication.idMedication = medication
        OrderMedication.dose = dose
        OrderMedication.treatmentDuration = treatmentDuration
        OrderMedication.amount = amount
        OrderMedication.item = item
        OrderMedication.save()

        orderMedicationData = {
            key: value for key, value in vars(OrderMedication).items() if
            key != '_state' or key != 'idOrder_id' or key != 'idMedication_id'
        }

        collection.update_one(
            {"_id": str(idPatient)},
            {"$set": {f"histories.{clinicalHistory.date}.order.orderMedication": orderMedicationData}}
        )


def generateOrderProcedure(idPatient: int, idOrder: int, item: int, procedureId: int, amount: str, frequency: str):
    if models.OrderHelpDiagnostic.objects.filter(idOrder=idOrder).exists():
        raise Exception("No se puede agregar un procedimiento a una orden que ya tiene ayuda diagnostica")
    try:
        order = models.OrderHelpDiagnostic.objects.get(id=idOrder)
        procedure = models.OrderProcedure.objects.get(id=procedureId)
        clinicalHistory = models.ClinicalHistory.objects.get(idPatient=idPatient)
    except Exception as e:
        raise Exception(str(e))
    if models.Order.objects.filter(id=idOrder).exists():
        OrderProcedure = models.OrderProcedure()
        OrderProcedure.idOrder = order
        OrderProcedure.idProcedure = procedure
        OrderProcedure.amount = amount
        OrderProcedure.frequency = frequency
        OrderProcedure.item = item
        OrderProcedure.save()

        orderProcedureData = {
            key: value for key, value in vars(OrderProcedure).items() if
            key != '_state' or key != 'idOrder_id' or key != 'idMedication_id'
        }

        collection.update_one(
            {"_id": str(idPatient)},
            {"$set": {f"histories.{clinicalHistory.date}.order.orderProcedure": orderProcedureData}}
        )
