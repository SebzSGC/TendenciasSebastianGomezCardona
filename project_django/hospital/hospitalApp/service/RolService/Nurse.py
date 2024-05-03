from django.forms import model_to_dict

from hospital.connection_mongo import collection, collection_appointment
from hospitalApp import models
from hospitalApp.service import validatorService
from datetime import datetime


def getOrdersByIdPatient(idPatient: int):
    orders_with_dates = []
    dates = collection.find_one({"_id": str(idPatient)})["histories"].keys()
    for date in dates:
        order = collection.find_one({
            "_id": str(idPatient),
            f"histories.{date}.order": {"$exists": True}
        })
        if order:
            order_data = {
                "date": date,
                "orders": order["histories"][date]["order"]
            }
            orders_with_dates.append(order_data)
    if orders_with_dates:
        return orders_with_dates
    else:
        raise Exception("No se encontraron órdenes para el paciente en ninguna fecha")


def registerVitalDataForPatient(idPatient: int, arterialPressure: float, temperature: float, pulse: int,
                                bloodOxygenLevel: float):
    if not validatorService.validatePatientById(idPatient):
        raise Exception("El paciente no existe")

    patient = models.Patient(**validatorService.getPatientById(idPatient))
    vitalData = models.VitalData(None, idPatient, arterialPressure, temperature, pulse, bloodOxygenLevel)
    vitalData.save()
    date = datetime.today().strftime("%d/%m/%Y %H:%M")
    clinicalVisit = models.ClinicalVisit(idPatient=patient, date=date, vitalData=vitalData)
    clinicalVisit.save()

    vitalData = {
        key: value for key, value in vars(vitalData).items() if key != '_state' and key != 'idPatient_id'
    }
    collection_appointment.insert_one({
        "_id": str(idPatient),
        "appointments": {
            date: {"vitalData": vitalData}
        }
    })


def registerMedicineFromOrder(orderId: int, item: int, idPatient: int, dateVisit: str):
    if not validatorService.validatePatientById(idPatient):
        raise Exception("El paciente no existe")
    if not models.OrderMedication.objects.filter(item=item, idOrder=orderId).exists():
        raise Exception("El medicamento no existe en la orden")
    if not models.ClinicalVisit.objects.filter(idPatient=idPatient, date=dateVisit).exists():
        raise Exception("La fecha de visita no existe")
    orderMedication = models.OrderMedication.objects.select_related("idMedication").get(item=item, idOrder=orderId)
    orderMedicationToDict = model_to_dict(orderMedication)
    medicationToDict = model_to_dict(orderMedication.idMedication)
    for key in orderMedicationToDict.keys():
        if key in medicationToDict:
            del medicationToDict[key]

    if "idMedication" in orderMedicationToDict:
        del orderMedicationToDict["idMedication"]
    data = {
        "OrderMedication": orderMedicationToDict,
        "Medication": medicationToDict
    }

    collection_appointment.update_one(
        {"_id": str(idPatient)},
        {"$set": {f"appointments.{dateVisit}.medication": data}}
    )


def registerProcedureFromOrder(orderId: int, item: int, idPatient: int, dateVisit: str):
    if not validatorService.validatePatientById(idPatient):
        raise Exception("El paciente no existe")
    if not models.OrderProcedure.objects.filter(item=item, idOrder=orderId).exists():
        raise Exception("El procedimiento no existe en la orden")
    if not models.ClinicalVisit.objects.filter(idPatient=idPatient, date=dateVisit).exists():
        raise Exception("La fecha de visita no existe")
    orderProcedure = models.OrderProcedure.objects.select_related("idProcedure").get(item=item, idOrder=orderId)
    orderProcedureToDict = model_to_dict(orderProcedure)
    procedureToDict = model_to_dict(orderProcedure.idMedication)
    for key in orderProcedureToDict.keys():
        if key in procedureToDict:
            del procedureToDict[key]

    if "idProcedure" in orderProcedureToDict:
        del orderProcedureToDict["idProcedure"]
    data = {
        "OrderProcedure": orderProcedureToDict,
        "Procedure": procedureToDict
    }

    collection_appointment.update_one(
        {"_id": str(idPatient)},
        {"$set": {f"appointments.{dateVisit}.procedure": data}}
    )
