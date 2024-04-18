def validatePatientById(idDocument: int) -> bool:
    return models.Patient.objects.filter(idDocument=idDocument).exists()


def getPatientById(idDocument: int) -> dict | None:
    return model_to_dict(models.Patient.objects.get(pk=idDocument))


def getPatients() -> list | None:
    return list(models.Patient.objects.values())


def getEmergencyContactById(idPatient: int) -> dict | None:
    return model_to_dict(models.EmergencyContact.objects.get(idPatient=idPatient))


def getMedicalInsuranceById(idPatient: int) -> dict | None:
    return model_to_dict(models.MedicalInsurance.objects.get(idPatient=idPatient))


def validateDoctorByName(fullName: str) -> bool:
    return models.Employee.objects.filter(fullName=fullName, rol="Doctor").exists()


def validateDoctorById(id: int) -> bool:
    return models.Employee.objects.filter(id=id, rol="Doctor").exists()


def getMedicineByName(name: str) -> dict | None:
    return model_to_dict(models.Medication.objects.get(name=name))


def getProcedureByName(name: str) -> dict | None:
    return model_to_dict(models.Procedure.objects.get(name=name))


def getMedicineById(id: int) -> dict | None:
    return models.Medication.objects.get(id=id)


def getProcedureById(id: int) -> dict | None:
    return models.Procedure.objects.get(id=id)
