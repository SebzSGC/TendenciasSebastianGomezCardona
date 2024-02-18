class Invoice():
    def __init__(self, medicalInsurance, user, order):
        self.patient = user
        self.medicalInsurance = medicalInsurance
        self.order = order

class MedicalAppointment():
    def __init__(self, id , idUser, treatingDoctor):
        self.id = id
        self.idUser = idUser
        self.treatingDoctor = treatingDoctor

class Order():
    def __init__(self, idMedicalAppointment):
        self.idMedicalAppointment = idMedicalAppointment
        self.medications = []
        self.procedures = []
        self.tests = []
        self.observations = []

class Medication():
    def __init__(self, name, price, dosage, idOrder):
        self.idOrder = idOrder
        self.nombre = name
        self.price = price
        self.dosage = dosage

class Procedure():
    def __init__(self, name, idOrder):
        self.name = name
        self.idOrder = idOrder