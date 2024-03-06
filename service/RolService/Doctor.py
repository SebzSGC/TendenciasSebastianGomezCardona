import datetime
from model.Order import Order

def getAppointmentByDate(hospital):
    date = input("Ingrese la fecha de la cita (dd/mm/yyyy):\n")
    if date not in hospital.appointments:
        raise Exception("No hay citas programadas para esta fecha")
    for appointment in hospital.appointments:
        if hospital.appointments.date == date:
            return appointment
    raise Exception("No hay citas programadas para esta fecha")

def getAllPatientInfo():
    pass

def generateHistory(hospital, patientDocument, procedure, medicine, helpDiagnostic, doctorDocument):
    if str(patientDocument) not in hospital.patients:
        raise Exception("El documento del paciente no es valido o no existe")
    if str(doctorDocument) not in hospital.doctors:
        raise Exception("El documento del doctor no es valido o no existe")
    newClinicalHistory = {}
    date = datetime.date.today().strftime("%d/%m/%Y")
    newClinicalHistory["Date"] = date
    newClinicalHistory["DoctorDocument"] = doctorDocument
    newClinicalHistory["consultReason"] = input("Ingrese el motivo de la consulta:\n")
    newClinicalHistory["symptomatology"] = input("Ingrese la sintomatologia:\n")
    newClinicalHistory["diagnosis"] = input("Ingrese el diagnostico:\n")
    order = Order(patientDocument)
    if medicine != "N/A" and helpDiagnostic == "N/A":
        newClinicalHistory["idOrder"] = order.id
        newClinicalHistory["idMedicine"]
        newClinicalHistory["dose"]
        newClinicalHistory["treatmentDuration"]
        newClinicalHistory["item"]
    if procedure != "N/A" and helpDiagnostic == "N/A":
        newClinicalHistory["idOrder"] = order.id
        newClinicalHistory["idProcedure"]
        newClinicalHistory["amount"]
        newClinicalHistory["frequency"]
        newClinicalHistory["specialAssistance"]
        newClinicalHistory["idSpecialist"]
        newClinicalHistory["item"]
    if helpDiagnostic != "N/A" and procedure == "N/A" and medicine == "N/A":
        newClinicalHistory["idOrder"]
        newClinicalHistory["idhelpDiagnostic"]
        newClinicalHistory["quantity"]
        newClinicalHistory["specialAssistance"]
        newClinicalHistory["idSpecialist"]
        newClinicalHistory["item"]
    hospital.clinicalHistories[str(patientDocument)][date] = newClinicalHistory