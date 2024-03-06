class ClinicalVisit():
    def __init__(self, idPatient, idOrder, vitalData):
        self.idPatient = idPatient
        self.idOrder = idOrder
        self.vitalData = vitalData
        self.medicine = []
        self.procedures = []