class User():
    def __init__(self, id, fullName, bornDate, genre, adress, phoneNumber, email):
        self.id = id
        self.fullName = fullName
        self.bornDate  = bornDate
        self.genre = genre
        self.adress = adress
        self.phoneNumber = phoneNumber
        self.email = email

class EmergencyContact():
    def __init__(self, name, RelationShip, phoneNumber, idUser):
        self.idUser = idUser
        self.name = name
        self.RelationShip = RelationShip
        self.phoneNumber = phoneNumber

class MedicalInsurance():
    def __init__(self, nameOfInsuranceCompany, policyNumber, policyState, policyValidity, idUser):
        self.idUser = idUser
        self.nameOfInsuranceCompany = nameOfInsuranceCompany
        self.policyNumber = policyNumber
        self.policyState = policyState
        self.policyValidity = policyValidity

class VitalData():
    def __init__(self, idUser, arterialPressure, temperature, pulse, bloodOxygenLevel):
        self.idUser = idUser
        self.arterialPressure = arterialPressure
        self.temperature = temperature
        self.pulse = pulse
        self.bloodOxygenLevel = bloodOxygenLevel
     