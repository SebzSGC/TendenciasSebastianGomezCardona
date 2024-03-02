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
        self.medicalInsurance = MedicalInsurance
class EmergencyContact():
    def __init__(self, idUser, name, relationship, phoneNumber):
        self.idUser = idUser
        self.name = name
        self.relationship = relationship
        self.phoneNumber = phoneNumber

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