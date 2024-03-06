from model.User import VitalData
from model.clinicalVisit import ClinicalVisit
from service.RolService.AdministrativePersonal import validatePatientId

def registerVitalDataForPatent(hospital,idUser,arterialPressure,temperature,pulse,bloodOxygenLevel, idOrder):
    if validatePatientId(hospital, idUser) == None:
        raise Exception("El paciente no existe")
    vitalData = VitalData(idUser,arterialPressure,temperature,pulse,bloodOxygenLevel)
    generateClinicalVisit(hospital, idUser, idOrder, vitalData)

def generateClinicalVisit(hospital, idPatient, idOrder, vitalData):
    clinicalVisit = ClinicalVisit(idPatient, idOrder, vitalData)
    hospital.clinicalVisits.append(clinicalVisit)
    print("Visita clínica generada con éxito")

def generateOrder():
    pass


