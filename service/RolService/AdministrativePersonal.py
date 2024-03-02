import model

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
    patient = model.User(id, fullName, bornDate, genre, address, phoneNumber, email)
    hospital.patients.append(patient)
    print(f"Paciente: {patient.fullName} creado con éxito")

def updatePatient(patient, attribute, newInfo, oldAttribute):
    setattr(patient, attribute, newInfo)
    print(f"Informacion del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def generateAppointment():
    pass

def generateMedicalInsurance():
    pass

def generateInvoice():
    pass

def getOrders():
    pass