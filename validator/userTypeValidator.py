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
        correctAttributes ={
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