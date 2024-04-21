from hospitalApp import models
from django.forms.models import model_to_dict
from django.db import connection
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

# def generateHistory(hospital, patientDocument, doctorDocument, procedure, medicine, helpDiagnostic, date, consultReason, symptomatology, diagnosis):
#     patient = validatePatientId(hospital, patientDocument)
#     doc = validDoctorId(hospital, doctorDocument)
#
#     if not (patient and doc):
#         raise Exception("El documento del paciente o del doctor no es valido o no existe")
#
#     try:
#         typeValidator.validDate(date)
#     except ValueError as e:
#         raise Exception(str(e))
#
#     medicine = getMedicine(hospital, medicine) if medicine != "N/A" else "N/A"
#     procedure = getProcedure(hospital, procedure) if procedure != "N/A" else "N/A"
#
#     newClinicalHistory = {
#         "Date": date,
#         "DoctorDocument": doctorDocument,
#         "consultReason": consultReason,
#         "symptomatology": symptomatology,
#         "diagnosis": diagnosis,
#         "order": None
#     }
#
#     if procedure is None and medicine is None and helpDiagnostic == "N/A":
#         print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
#     else:
#         idOrder = len(hospital.orders) + 1
#         actualOrder = Order.Order(idOrder, patientDocument, doctorDocument, date)
#
#         if helpDiagnostic != "N/A" and procedure == "N/A" and medicine == "N/A":
#             handleDiagnostic(actualOrder)
#         elif helpDiagnostic == "N/A" and procedure == "N/A" and medicine != "N/A":
#             handleMedication(actualOrder, medicine, hospital)
#         elif helpDiagnostic == "N/A" and medicine == "N/A" and procedure != "N/A":
#             handleProcedure(actualOrder, procedure, hospital)
#         elif procedure != "N/A" and medicine != "N/A" and helpDiagnostic == "N/A":
#             handleMedication(actualOrder, medicine, hospital)
#             handleProcedure(actualOrder, procedure, hospital)
#         else:
#             raise Exception("No se puede agregar una ayuda diagnostica si se esta asignando un procedimiento o medicamento")
#         newClinicalHistory["order"] = vars(actualOrder)
#         setOrderDetails(hospital, newClinicalHistory)
#
#     hospital.clinicalHistories[str(patientDocument)][date] = newClinicalHistory
#     print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
#
# def handleDiagnostic(actualOrder):
#     item = len(actualOrder.orderHelpDiagnostics) + 1
#     nameHelpDiagnostic = input("Ingrese el nombre del diagnostico de ayuda:\n")
#     quantity = input("Ingrese la cantidad:\n")
#     amount = input("Ingrese el valor:\n")
#     specialAssistance = input("Requiere de asistencia por especialista:\n").lower() == "si"
#     if specialAssistance:
#             idSpecialist = setSpecialist()
#     else:
#         idSpecialist = None
#     actualDiagnostic = Order.OrderHelpDiagnostic(actualOrder.id, nameHelpDiagnostic, quantity, amount, specialAssistance, idSpecialist, item)
#     actualOrder.orderHelpDiagnostics.append(actualDiagnostic)
#     print(f"La historia clinica del paciente {actualOrder.idPatient} ha sido generada con exito")
#     print(f"Ayuda diagnostica agregada a la orden #{actualOrder.id}")
#
# def handleMedication(actualOrder, medicine, hospital):
#     while True:
#         item = len(actualOrder.orderMedications) + 1
#         idMedicine = medicine.id
#         dose = input("Ingrese la dosis del medicamento:\n")
#         treatmentDuration = input("Ingrese la duración del tratamiento:\n")
#         amount = medicine.price
#         actualMedication = Order.OrderMedication(actualOrder.id, idMedicine, dose, treatmentDuration, amount, item)
#         actualOrder.orderMedications.append(actualMedication)
#         print(f"La orden #{actualOrder.id} del paciente se le ha asignado el medicamento {medicine.name} y sus respectivos datos con exito")
#         if input("Desea agregar otro medicamento? (si/no)\n").lower() == "no":
#             break
#         medicine = input("Ingrese el nombre del medicamento:\n")
#         medicine = getMedicine(hospital, medicine)
#         if medicine is None:
#             print("El medicamento no existe")
#             break
#
# def handleProcedure(actualOrder, procedure, hospital):
#     while True:
#         item = len(actualOrder.orderProcedures) + 1
#         idProcedure = procedure.id
#         amount = input("Ingrese la cantidad del procedimiento:\n")
#         frequency = input("Ingrese la frecuencia del procedimiento:\n")
#         specialAssistance = input("¿Requiere de asistencia por especialista? (si/no)\n").lower() == "si"
#         if specialAssistance:
#             idSpecialist = setSpecialist()
#         else:
#             idSpecialist = None
#         actualProcedure = Order.OrderProcedure(actualOrder.id, idProcedure, amount, frequency, specialAssistance, idSpecialist, item)
#         actualOrder.orderProcedures.append(actualProcedure)
#         print(f"La orden #{actualOrder.id} del paciente se le ha asignado el procedimiento {procedure.name} y sus respectivos datos con exito")
#         if input("Desea agregar otro procedimiento? (si/no)\n").lower() == "no":
#             break
#         procedure = input("Ingrese el nombre del procedimiento:\n")
#         procedure = getProcedure(hospital, procedure)
#         if procedure is None:
#             print("El procedimiento no existe")
#             break
#
# def setSpecialist():
#
#     inventorySpecialists = {
#         "Especialista 1": "123",
#         "Especialista 2": "456",
#         "Especialista 3": "789"
#     }
#
#     print("Especialistas disponibles:")
#     for specialistName in inventorySpecialists:
#         print(f"- {specialistName}")
#     selectedSpecialist = input("Ingrese el nombre del especialista:\n")
#     if selectedSpecialist not in inventorySpecialists:
#         raise Exception("El especialista no existe")
#     idSpecialist = inventorySpecialists.get(selectedSpecialist)
#     return idSpecialist
#
# def setOrderDetails(hospital, newClinicalHistory):
#     order = newClinicalHistory["order"]
#     if order["orderMedications"]:
#         for index, medicationOrder in enumerate(order["orderMedications"]):
#             order["orderMedications"][index] = (vars(medicationOrder))
#     if order["orderProcedures"]:
#         for index, procedureOrder in enumerate(order["orderProcedures"]):
#             order["orderProcedures"][index] = (vars(procedureOrder))
#     if order["orderHelpDiagnostics"]:
#         for index, diagnosticOrder in enumerate(order["orderHelpDiagnostics"]):
#             order["orderHelpDiagnostics"][index] = (vars(diagnosticOrder))
#     hospital.orders.append(order)
