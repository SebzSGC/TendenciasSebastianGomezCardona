from .. import models


def searchEmployee(userName: srt) -> bool:
    return models.Patient.objects.filter(userName=userName).exists()
