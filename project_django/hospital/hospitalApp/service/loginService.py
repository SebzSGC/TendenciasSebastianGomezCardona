import string
import secrets

from .. import models


def login(userName: str, password: str):
    try:
        user = models.Employee.objects.get(userName=userName)
    except:
        raise Exception("El usuario no existe")
    if user.password != password:
        raise Exception("Contraseña incorrecta")
    activeSession = models.Session.objects.filter(idEmployee=user)
    if activeSession.exists():
        raise Exception("Ya hay una sesión activa")
    chars = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(chars) for _ in range(225))
    session = models.Session()
    session.idEmployee = user
    session.token = token
    session.save()
    return session


def getSession(token: str):
    try:
        return models.Session.objects.get(token=token)
    except:
        raise Exception("La sesión no existe")
