class ClinicalVisit():
    def __init__(self, idPatient, date, vitalData):
        self.idPatient = idPatient
        self.date = date
        self.medication = []
        self.procedure = []
        self.vitalData = vitalData