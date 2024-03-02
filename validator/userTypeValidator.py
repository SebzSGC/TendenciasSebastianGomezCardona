import service.RolService.AdministrativePersonal as administrativePersonal

def getPatientData(hospital):
    print("Por favor ingrese los datos del paciente:")
    id = len(hospital.patients) + 1
    fullName = input("Nombre completo: ")
    bornDate = input("Fecha de nacimiento (DD-MM-AAAA): ")
    genre = input("Género: ")
    address = input("Dirección: ")
    phoneNumber = input("Número de teléfono: ")
    email = input("Correo electrónico: ")
    administrativePersonal.createPatient(hospital, id, fullName, bornDate, genre, address, phoneNumber, email)

def getUpdatePatientData(patient, attribute):
        correctAttributes = {
            "1": "fullName",
            "2": "bornDate",
            "3": "genre",
            "4": "address",
            "5": "phoneNumber",
            "6": "adress"
        }

        if attribute in correctAttributes:
            oldAttribute = getattr(patient, correctAttributes[attribute])
            newInfo = input(f"Ingrese el nuevo dato para {correctAttributes[attribute]}: ")
            administrativePersonal.updatePatient(patient, correctAttributes[attribute], newInfo, oldAttribute)

def getEmergencyContactData(patient):
    print(f"Por favor ingrese los datos del contacto de emergencia de {patient.fullName}")
    id = patient.id
    name = input("Nombre completo: ")
    relationship = input("Relación: ")
    phoneNumber = input("Número de teléfono: ")
    administrativePersonal.createEmergencyContact(id, name, relationship, phoneNumber)

def getUpdateEmergencyContactData(contact, attribute):
    correctAttributes ={
        "1": "name",
        "2": "relationship",
        "3": "phoneNumber",
    }

    if attribute in correctAttributes:
        oldAttribute = getattr(contact, correctAttributes[attribute])
        newInfo = input(f"Ingrese el nuevo dato para {correctAttributes[attribute]}: ")
        administrativePersonal.updateEmergencyContact(contact, attribute, newInfo, oldAttribute)

def getMedicalInsuranceData(patient):
    print(f"Por favor ingrese los datos de la poliza de {patient.fullName}")
    idUser = patient.id
    nameOfInsuranceCompany = input("Nombre de la compañia de seguros: ")
    policyNumber = input("Número de poliza: ")
    policyState = input("Estado de la poliza: ")
    policyValidity = input("Vigencia de la poliza: ")
    administrativePersonal.createMedicalInsurance(idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity)

def getUpdateMedicalInsuranceData(insurance, attribute):
    correctAttributes ={
        "1": "nameOfInsuranceCompany",
        "2": "policyNumber",
        "3": "policyState",
        "4": "policyValidity",
    }

    if attribute in correctAttributes:
        oldAttribute = getattr(insurance, correctAttributes[attribute])
        newInfo = input(f"Ingrese el nuevo dato para {correctAttributes[attribute]}: ")
        administrativePersonal.updateMedicalInsurance(insurance, attribute, newInfo, oldAttribute)