class Order():
    def __init__(self, id, idPatient,idDoctor, creationDate):
        self.id = id
        self.idPatient = idPatient
        self.idDoctor = idDoctor
        self.creationDate = creationDate
        self.orderMedications = []
        self.orderProcedures = []
        self.orderHelpDiagnostics = []

class OrderMedication():
    def __init__(self, idOrder, idMedication, dose, treatmentDuration, amount, item):
        self.idOrder = idOrder
        self.idMedication = idMedication
        self.dose = dose
        self.treatmentDuration = treatmentDuration
        self.amount = amount
        self.item = item

class OrderProcedure():
    def __init__(self, idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist, item):
        self.idOrder = idOrder
        self.idProcedure = idProcedure
        self.amount = amount
        self.frequency = frequency
        self.specialAssistance = specialAssistance
        self.idSpecialist = idSpecialist
        self.item = item
class OrderHelpDiagnostic():
    def __init__(self, idOrder, nameHelpDiagnostic, quantity, amount, specialAssistance, idSpecialist, item):
        self.idOrder = idOrder
        self.nameHelpDiagnostic = nameHelpDiagnostic
        self.quantity = quantity
        self.amount = amount
        self.specialAssistance = specialAssistance
        self.idSpecialist = idSpecialist
        self.item = item