import datetime
def getAllPatientInfo():
    pass

def generateHistory(hospital, user):
    if str(user.id) not in hospital.patients:
        return print("El usuario no existe")
    newClinicalHistory = {}
    date = datetime.date.today().strftime("%m/%d/%Y")
    hospital.clinicalHistories[str(user.id)][date] = newClinicalHistory