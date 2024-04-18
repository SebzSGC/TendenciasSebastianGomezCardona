from .. import models


def validCredentials(userName: srt, password: str) -> bool:
    return models.Employee.objects.filter(userName=userName, password=password).exists()
