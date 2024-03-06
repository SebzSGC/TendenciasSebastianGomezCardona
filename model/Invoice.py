class Invoice():
    def __init__(self, medicalAppointment, medicalInsurance, user):
        self.medicalAppointment = medicalAppointment
        self.medicalInsurance = medicalInsurance
        self.patient = user