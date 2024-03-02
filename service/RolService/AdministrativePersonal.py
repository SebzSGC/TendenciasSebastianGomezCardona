from model import Hospital, User, Invoice

def validatePatientId(hospital, id):
    for patient in hospital.patients:
        if patient.id == id:
            return patient
        return None

def createPatient(hospital, id, fullName, bornDate, genre, address, phoneNumber, email):
    patient=validatePatientId(hospital, id)
    if patient:
        raise Exception("ya existe un paciente con esa cedula registrada")
    patient = None
    patient = User(id, fullName, bornDate, genre, address, phoneNumber, email)
    hospital.clinicalHistories[str(id)] = {} 
    hospital.patients.append(patient)
    print(f"Paciente: {patient.fullName} creado con éxito")

def createEmergencyContact(idUser, name, relationship, phoneNumber):
    patient = validatePatientId(idUser)
    if not patient:
        raise Exception("El paciente no existe")
    contact = User.EmergencyContact(idUser, name, relationship, phoneNumber)
    patient.emergencyContact = contact

def updatePatient(patient, attribute, newInfo, oldAttribute):
    patient = validatePatientId(patient.id)
    if not patient:
        raise Exception("El paciente no existe")
    setattr(patient, attribute, newInfo)
    print(f"Informacion del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def updateEmergencyContact(contact, attribute, newInfo, oldAttribute):
    contact = validatePatientId(contact.id)
    if not contact:
        raise Exception("El contacto de emergencia no esta asociado a un paciente")
    setattr(contact, attribute, newInfo)
    print(f"Informacion de contacto del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def generateAppointment():
    pass

def generateMedicalInsurance():
    pass

def generateInvoice():
    pass

def getOrders():
    pass