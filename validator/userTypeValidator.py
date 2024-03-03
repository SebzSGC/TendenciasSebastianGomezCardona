import service.RolService.AdministrativePersonal as administrativePersonal

def getPatientData(hospital):
    try:
        print("Por favor ingrese los datos del paciente:")
        id = len(hospital.patients) + 1
        fullName = input("Nombre completo: ")
        bornDate = input("Fecha de nacimiento (DD-MM-AAAA): ")
        genre = input("Género: ")
        address = input("Dirección: ")
        phoneNumber = input("Número de teléfono: ")
        email = input("Correo electrónico: ")
        administrativePersonal.createPatient(hospital,id, fullName, bornDate, genre, address, phoneNumber, email)
    except Exception as error:
        print(str(error))

def allDataCompletePatient(hospital, patient):
    try:
        administrativePersonal.allDataCompletePatient(hospital, patient)
    except Exception as error:
        print(str(error))

def getUpdatePatientData(patient, attribute):
    try:
        correctAttributes = {
            "1": "fullName",
            "2": "bornDate",
            "3": "genre",
            "4": "address",
            "5": "phoneNumber",
            "6": "adress"
        }

        attributeNames = {
            "1": "nombre completo",
            "2": "fecha de nacimiento",
            "3": "género",
            "4": "dirección",
            "5": "número de teléfono",
            "6": "dirección"
        }

        if attribute in correctAttributes:
            oldAttribute = getattr(patient, correctAttributes[attribute])
            newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
            administrativePersonal.updatePatient(patient, correctAttributes[attribute], newInfo, oldAttribute)
    except Exception as error:
        print(str(error))

def getEmergencyContactData(hospital, patient):
    try:
        print(f"Por favor ingrese los datos del contacto de emergencia de {patient.fullName}")
        id = patient.id
        name = input("Nombre completo: ")
        relationship = input("Relación: ")
        phoneNumber = input("Número de teléfono: ")
        administrativePersonal.createEmergencyContact(hospital, id, name, relationship, phoneNumber)
    except Exception as error:
        print(str(error))
        
def getUpdateEmergencyContactData(hospital, contact, attribute):
    try:
        correctAttributes ={
            "1": "name",
            "2": "relationship",
            "3": "phoneNumber",
        }

        attributeNames = {
            "1": "nombre",
            "2": "relación",
            "3": "número de teléfono",
        }

        if attribute in correctAttributes:
            oldAttribute = getattr(contact, correctAttributes[attribute])
            newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
            administrativePersonal.updateEmergencyContact(hospital, contact, attribute, newInfo, oldAttribute)
            return True
        else:
            return False
    except Exception as error:  
        print(str(error))

def getMedicalInsuranceData(hospital, patient):
    try:
        print(f"Por favor ingrese los datos de la poliza de {patient.fullName}")
        idUser = patient.id
        nameOfInsuranceCompany = input("Nombre de la compañia de seguros: ")
        policyNumber = input("Número de poliza: ")
        policyState = input("Estado de la poliza: ")
        policyValidity = input("Vigencia de la poliza: ")
        administrativePersonal.createMedicalInsurance(hospital, idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity)
    except Exception as error:
        print(str(error))

def getUpdateMedicalInsuranceData(hospital, insurance, attribute):
    try:
        correctAttributes ={
            "1": "nameOfInsuranceCompany",
            "2": "policyNumber",
            "3": "policyState",
            "4": "policyValidity",
        }

        attributeNames = {
            "1": "nombre de la compañia de seguros",
            "2": "número de poliza",
            "3": "estado de la poliza",
            "4": "vigencia de la poliza",
        }

        if attribute in correctAttributes:
            oldAttribute = getattr(insurance, correctAttributes[attribute])
            newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
            administrativePersonal.updateMedicalInsurance(hospital, insurance, attribute, newInfo, oldAttribute)
            return True
        else:
            return False
    except Exception as error:
        print(str(error))

def validMedicalInsuranceData(hospital, userToUpdate):
    while True:
        attribute = input("1. Nombre de la compañia de seguros \n2. Numero de poliza\n3. Estado de la poliza\n4. Vigencia de la poliza\n5. Regresar\n")
        if attribute not in ["1", "2", "3", "4", "5"]:
           return print("Opción inválida")
        if attribute == "5":
            break
        isValid = getUpdateMedicalInsuranceData(hospital, userToUpdate.medicalInsurance, attribute)
        if not isValid:
            print("Opción inválida")
            continue
        option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
        if option == "2":
            break
        if option == "1":
            continue

def validContactEmergencyData(hospital, userToUpdate):
    while True:
        print("¿Qué información deseas cambiar?")
        attribute = input("1. Nombre completo \n2. Relación\n3. Número de teléfono\n4. Regresar\n")
        if attribute not in ["1", "2", "3", "4"]:
           return print("Opción inválida")
        if attribute == "4":
            break
        isValid = getUpdateEmergencyContactData(hospital, userToUpdate.emergencyContact, attribute)
        if not isValid:
            print("Opción inválida")
            continue
        option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
        if option == "2":
            break
        if option == "1":
            continue

def validPatientData(hospital, userToUpdate):
    while True:
        print("¿Qué información deseas cambiar?")
        attribute = input("1. Nombre completo \n2. Fecha de nacimiento\n3. Genero\n4. Direccion\n5. Numero de telefono\n6. Correo electronico\n7. Contacto de emergencia\n8. Poliza\n9. Regresar\n")
        if attribute not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Opción inválida")
            continue
        if attribute == "9":
            break
        getUpdatePatientData(userToUpdate, attribute)
        if attribute == "7":
            menuUpdateContactEmergency(hospital, userToUpdate)
        if attribute == "8":
            menuUpdateInsurance(hospital, userToUpdate)
        else:
            break

def menuUpdateContactEmergency(hospital, userToUpdate):
    validContactEmergencyData(hospital, userToUpdate)

def menuUpdateInsurance(hospital, userToUpdate):
    validMedicalInsuranceData(hospital, userToUpdate)