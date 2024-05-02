from hospitalApp import models
from django.forms.models import model_to_dict
from hospital.connection_mongo import collection


def validatePatientById(idDocument: int) -> bool:
    return models.Patient.objects.filter(idDocument=idDocument).exists()


def getPatientById(idDocument: int) -> dict | None:
    return model_to_dict(models.Patient.objects.get(pk=idDocument))


def getPatients() -> list | None:
    return list(models.Patient.objects.values())


def getEmployees() -> list | None:
    return list(models.Employee.objects.values())


def getEmployeeById(id: int) -> dict | None:
    return model_to_dict(models.Employee.objects.get(pk=id))


def getEmergencyContactById(idPatient: int) -> dict | None:
    return model_to_dict(models.EmergencyContact.objects.get(idPatient=idPatient))


def getMedicalInsuranceById(idPatient: int) -> dict | None:
    return model_to_dict(models.MedicalInsurance.objects.get(idPatient=idPatient))


def validateDoctorByName(fullName: str) -> bool:
    return models.Employee.objects.filter(fullName=fullName, rol="Doctor").exists()


def validateDoctorById(id: int) -> bool:
    return models.Employee.objects.filter(id=id, rol="Doctor").exists()


def getMedicineByName(name: str) -> dict | None:
    return model_to_dict(models.Medication.objects.get(name=name))


def getProcedureByName(name: str) -> dict | None:
    return model_to_dict(models.Procedure.objects.get(name=name))


def getMedicineById(id: int) -> dict | None:
    return models.Medication.objects.get(id=id)


def getProcedureById(id: int) -> dict | None:
    return models.Procedure.objects.get(id=id)


def validateEmployeeById(id: int) -> bool:
    return models.Employee.objects.filter(id=id).exists()


def validateEmployeeByUserName(userName):
    return models.Employee.objects.filter(userName=userName).exists()


def getDoctor(idDocument: int):
    return model_to_dict(models.Employee.objects.get(idDocument=idDocument, rol="Doctor"))


def getAppointmentsById(idPatient: int) -> list | None:
    return list(models.MedicalAppointment.objects.filter(idPatient=idPatient).values())


def getAppointmentByIdAndDate(idPatient: int, date: str):
    return model_to_dict(models.MedicalAppointment.objects.get(idPatient=idPatient, date=date))


def getOrdersByIdPatient(idPatient: int):
    dates = list(models.ClinicalHistory.objects.filter(idPatient=idPatient).values_list('date', flat=True))
    orders = []
    for date in dates:
        order = collection.find_one({
            "_id": str(idPatient),
            f"histories.{date}.order": {"$exists": True}
        })
        if order:
            orders.append(order["histories"][date]["order"])
    if orders:
        return orders
    else:
        raise Exception("No se encontraron órdenes para el paciente en ninguna fecha")
