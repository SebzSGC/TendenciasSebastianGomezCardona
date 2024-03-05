class Order():
    def __init__(self, idMedicalAppointment):
        self.idMedicalAppointment = idMedicalAppointment
        self.medications = []
        self.procedures = []
        self.tests = []
        self.observations = []