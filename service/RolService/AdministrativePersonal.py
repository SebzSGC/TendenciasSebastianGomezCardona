import datetime
import validator.typeValidator as validator
import model.User as User
from model.MedicalAppointment import MedicalAppointment
from model.Order import Order

def validatePatientId(hospital, id):
    if hospital.patients == []:
        return None
    for patient in hospital.patients:
        if patient.id == id:
            return patient
    return None
    
def validateDoctor(hospital, name):
    if hospital.employees == []:
        return None
    for doctor in hospital.employees:
        if doctor.fullName == name and doctor.rol == "Doctor":
            return doctor
    return None

def createPatient(hospital, id, fullName, bornDate, genre, address, phoneNumber, email):
    patient = validatePatientId(hospital, id)
    if patient:
        raise Exception("ya existe un paciente con esa cedula registrada")
    patient = User.Patient(id, fullName, bornDate, genre, address, phoneNumber, email)
    hospital.clinicalHistories[str(id)] = {} 
    hospital.patients.append(patient)

def allDataCompletePatient(hospital, patient):
    patient = validatePatientId(hospital, patient.id)
    if not patient:
        raise Exception("Ocurrio un error al crear el paciente, intente de nuevo")
    for item in hospital.patients:
        if item.id == patient.id:
            item = patient
    print(f"Paciente: {patient.fullName} creado con éxito")

def createEmergencyContact(hospital, idUser, name, relationship, phoneNumber):
    patient = validatePatientId(hospital, idUser)
    if not patient:
        raise Exception("El paciente no existe")
    contact = User.EmergencyContact(idUser, name, relationship, phoneNumber)
    patient.emergencyContact = contact

def createMedicalInsurance(hospital, idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity):
    patient = validatePatientId(hospital, idUser)
    if not patient:
        raise Exception("El paciente no existe")
    insurance = User.MedicalInsurance(idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity)
    patient.medicalInsurance = insurance

def updatePatient(patient, attribute, newInfo, oldAttribute):
    setattr(patient, attribute, newInfo)
    print(f"Informacion del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def updateEmergencyContact(hospital, contact, attribute, newInfo, oldAttribute):
    contact = validatePatientId(hospital, contact.idUser)
    if not contact:
        raise Exception("El contacto de emergencia no esta asociado a un paciente")
    setattr(contact, attribute, newInfo)
    print(f"Informacion de contacto del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def updateMedicalInsurance(hospital, insurance, attribute, newInfo, oldAttribute):
    insurance = validatePatientId(hospital, insurance.idUser)
    if not insurance:
        raise Exception("La poliza no esta asociada a un paciente")
    setattr(insurance, attribute, newInfo)
    print(f"Informacion de la poliza del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def generateAppointment(hospital, patient, doctor, date):
    if patient == None:
        raise Exception("El paciente no existe")
    if doctor == None:
        raise Exception("El doctor no existe")
    date = validator.validDate(date)
    appointment = MedicalAppointment(patient.id, doctor.idNumber, date)
    order = Order(patient.id)
    hospital.orders.append(order)
    hospital.appointments.append(appointment)
    print(f"Cita programada para el paciente: {patient.fullName}, el dia {date} con el doctor: {doctor.fullName}")

def generateMedicalInsurance():
    pass

def generateInvoice():
    pass

def getOrders():
    pass