import datetime
import re

def validRole(newRole):
    rolOptions = {
    "1": "Administrador",
    "2": "Doctor",
    "3": "Enfermera",
    "4": "Soporte",
    "5": "Recursos Humanos"
    }
    return rolOptions.get(newRole, "Opción inválida")

def validGenre(newGenre):
    genreOptions = {
    "1": "Masculino",
    "2": "Femenino",
    "3": "Otro"
    }
    return genreOptions.get(newGenre, "Opción inválida")

def getCorrectAge(bornDate):
    bornDate = datetime.datetime.strptime(bornDate, "%d/%m/%Y")
    actualDate = datetime.datetime.today()
    age = actualDate.year - bornDate.year
    if (actualDate.month, actualDate.day) < (bornDate.month, bornDate.day):
        age -= 1
    return age

def getValidityPolicy(datePolicyValidity):
    datePolicyValidity = datetime.datetime.strptime(datePolicyValidity, "%d/%m/%Y")
    actualDate = datetime.datetime.today()
    validity = actualDate - datePolicyValidity
    return validity.days

def validDate(date):
    try:
        dateObjt = datetime.datetime.strptime(date, '%d/%m/%Y')
        correctDate = dateObjt.strftime('%d/%m/%Y')
        return correctDate
    except ValueError:
        raise ValueError("Formato de fecha inválido, por favor ingrese la fecha en el formato dd/mm/yyyy")
    

def validDateAndAge(date):
    try:
        dateObjt = datetime.datetime.strptime(date, '%d/%m/%Y')
        actualDate = datetime.now()
        difference = actualDate.year - dateObjt.year
        if 0 <= difference <= 150:
            return True
        else:
            raise Exception("Edad ingresada no valida")
    except ValueError:
        raise Exception("Formato de fecha inválido")

def validEmail(email):
    if "@" in email and "." in email:
        return
    else:
        raise ValueError("Formato de correo inválido")
    
def validPhoneNumber(phone):
    if len(phone) < 11 and len(phone) > 0 and phone.isdigit():
        return
    else:
        raise ValueError("Formato de número de teléfono inválido")
    
def validPassword(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if bool(re.match(pattern, password)):
        return
    else:
        raise ValueError("Formato de contraseña inválido") 