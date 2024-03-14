import datetime

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
        date_objt = datetime.datetime.strptime(date, '%d/%m/%Y')
        correctDate = date_objt.strftime('%d/%m/%Y')
        return correctDate
    except ValueError:
        raise ValueError("Formato de fecha inválido, por favor ingrese la fecha en el formato dd/mm/yyyy")