class User():
    def __init__(self, id, fullName, bornDate, genre, address, phoneNumber, email):
        self.id = id
        self.fullName = fullName
        self.bornDate = bornDate
        self.genre = genre
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.emergencyContact = EmergencyContact
        self.medicalInsurance = EmergencyContact

    @classmethod
    def createPatient(cls, patients):
        print("Por favor ingrese los datos del paciente:")
        id = len(patients) + 1
        fullName = input("Nombre completo: ")
        bornDate = input("Fecha de nacimiento (YYYY-MM-DD): ")
        genre = input("Género: ")
        address = input("Dirección: ")
        phoneNumber = input("Número de teléfono: ")
        email = input("Correo electrónico: ")
        return cls(id, fullName, bornDate, genre, address, phoneNumber, email)
    
    def updatePatient(self, attribute, newInfo):
        correctAttributes ={
            "1": "fullName",
            "2": "bornDate",
            "3": "genre",
            "4": "address",
            "5": "phoneNumber",
            "6": "adress"
        }
        if attribute in correctAttributes:
            oldAttribute = getattr(self, correctAttributes[attribute])
            setattr(self, correctAttributes[attribute], newInfo)
            return print(f"Informacion del paciente: {oldAttribute} cambiado por {getattr(self, correctAttributes[attribute])}, actualizacion con éxito")
        else:
            return print("Opción inválida")

class EmergencyContact():
    def __init__(self, idUser, name, relationship, phoneNumber):
        self.idUser = idUser
        self.name = name
        self.relationship = relationship
        self.phoneNumber = phoneNumber

    @classmethod
    def createEmergencyContact(cls, idUser, userName):
        print(f"Por favor ingrese los datos del contacto de {userName}")
        id = idUser
        name = input("Nombre completo: ")
        relationship = input("Relación: ")
        phoneNumber = input("Número de teléfono: ")
        return cls(id, name, relationship, phoneNumber)
    
    def updateEmergencyContact(self, attribute, newInfo):
        correctAttributes ={
            "1": "name",
            "2": "relationship",
            "3": "phoneNumber",
        }
        if attribute in correctAttributes:
            oldAttribute = getattr(self, correctAttributes[attribute])
            setattr(self, correctAttributes[attribute], newInfo)
            return print(f"Informacion de contacto del paciente: {oldAttribute} cambiado por {getattr(self, correctAttributes[attribute])}, actualizacion con éxito")
        else:
            return print("Opción inválida")

class MedicalInsurance():
    def __init__(self, idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity):
        self.idUser = idUser
        self.nameOfInsuranceCompany = nameOfInsuranceCompany
        self.policyNumber = policyNumber
        self.policyState = policyState
        self.policyValidity = policyValidity

    @classmethod
    def createMedicalInsurance(cls, idUser, userName):
        print(f"Por favor ingrese los datos de poliza del paciente {userName}")
        id = idUser
        nameOfInsuranceCompany = input("Nombre de la compañia de seguros: ")
        policyNumber = input("Número de poliza: ")
        policyState = input("Estado de la poliza: ")
        policyValidity = input("Vigencia de la poliza: ")
        return cls(id, nameOfInsuranceCompany, policyNumber, policyState, policyValidity)
    
    def updateMedicalInsurance(self, attribute, newInfo):
        correctAttributes ={
            "1": "nameOfInsuranceCompany",
            "2": "policyNumber",
            "3": "policyState",
            "4": "policyValidity",
        }
        if attribute in correctAttributes:
            oldAttribute = getattr(self, correctAttributes[attribute])
            setattr(self, correctAttributes[attribute], newInfo)
            return print(f"Informacion de la poliza del paciente: {oldAttribute} cambiado por {getattr(self, correctAttributes[attribute])}, actualizacion con éxito")
        else:
            return print("Opción inválida")

class VitalData():
    def __init__(self, idUser, arterialPressure, temperature, pulse, bloodOxygenLevel):
        self.idUser = idUser
        self.arterialPressure = arterialPressure
        self.temperature = temperature
        self.pulse = pulse
        self.bloodOxygenLevel = bloodOxygenLevel