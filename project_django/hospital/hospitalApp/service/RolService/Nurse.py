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


# def selectDictionaryByOrderId(vectors):
#     if vectors is None or vectors == [] or vectors == "N/A":
#         return "N/A"
#     if 'idMedication' in vectors[0]:
#         print("IDs de ordenes que contienen el medicamento suministrado, porfavor elija la correcta.")
#     else:
#         print("IDs de ordenes que contienen el procedimiento realizado, porfavor elija la correcta:")
#     id_positions = {vector["idOrder"]: idx for idx, vector in enumerate(vectors)}
#     for id_order in id_positions.keys():
#         print(f"Orden #{id_order} = {id_order}")
#     selected_id = input("Ingrese el ID de la orden que desea seleccionar: ")
#     selected_position = id_positions.get(selected_id)
#     if selected_position is not None:
#         return vectors[selected_position]
#     else:
#         return None
#
#
# def print_all(clinicalVisit):
#     print("Datos vitales:")
#     print(" Documento del paciente: ", clinicalVisit.vitalData.idPatient)
#     print(" Presion arterial: ", clinicalVisit.vitalData.arterialPressure)
#     print(" Temperatura: ", clinicalVisit.vitalData.temperature)
#     print(" Pulso: ", clinicalVisit.vitalData.pulse)
#     print(" Nivel de oxigeno en la sangre: ", clinicalVisit.vitalData.bloodOxygenLevel)
#     print("Medicina administrada:")
#     if clinicalVisit.medication != "N/A":
#         printMedicines(clinicalVisit.medication)
#     else:
#         print(clinicalVisit.medication)
#     print("Procedimientos:")
#     if clinicalVisit.procedure != "N/A":
#         printProcedures(clinicalVisit.procedure)
#     else:
#         print(clinicalVisit.procedure)
#
#
# def printMedicines(medication):
#     for key, value in medication.items():
#         print(f" {key}: {value}")


def printProcedures(procedures):
    for key, value in procedures.items():
        print(f" {key}: {value}")
