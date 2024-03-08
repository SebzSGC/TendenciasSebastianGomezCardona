class Patient():
    def __init__(self, id, fullName, bornDate, genre, address, phoneNumber, email):
        self.id = id
        self.fullName = fullName
        self.bornDate = bornDate
        self.genre = genre
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.emergencyContact = None
        self.medicalInsurance = None
        self.clinicalHistory = None
        self.order = None
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
class ClinicalHistory():
    def __init__(self, idUser, doctorDocument, consultReason, symptomatology, diagnosis, date, procedure, medicine, helpDiagnostic):
        self.idUser = idUser
        self.doctorDocument = doctorDocument
        self.consultReason = consultReason
        self.symptomatology = symptomatology
        self.diagnosis = diagnosis
        self.date = date
        self.procedure = procedure
        self.medicine = medicine
        self.helpDiagnostic = helpDiagnostic
class VitalData():
    def __init__(self, idUser, arterialPressure, temperature, pulse, bloodOxygenLevel):
        self.idUser = idUser
        self.arterialPressure = arterialPressure
        self.temperature = temperature
        self.pulse = pulse
        self.bloodOxygenLevel = bloodOxygenLevel