class Invoice():
    def __init__(self, medicalInsurance, user, order):
        self.medicalInsurance = medicalInsurance
        self.patient = user
        self.order = order