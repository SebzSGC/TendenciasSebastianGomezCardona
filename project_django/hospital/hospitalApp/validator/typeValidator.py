from datetime import datetime
import re  # Regular expressions


def validRole(newRole: str) -> str:
    rolOptions = {
        "1": "Administrador",
        "2": "Doctor",
        "3": "Enfermera",
        "4": "Soporte",
        "5": "Recursos Humanos"
    }
    return rolOptions.get(newRole, "Opción inválida")


def validGenre(newGenre: str) -> str:
    genreOptions = {
        "1": "Masculino",
        "2": "Femenino",
        "3": "Otro"
    }
    return genreOptions.get(newGenre, "Opción inválida")


def getCorrectAge(bornDate: str) -> int:
    bornDate = datetime.strptime(bornDate, "%d/%m/%Y")
    actualDate = datetime.today()
    age = actualDate.year - bornDate.year
    if (actualDate.month, actualDate.day) < (bornDate.month, bornDate.day):
        age -= 1
    return age


def getValidityPolicy(datePolicyValidity: str) -> int:
    datePolicyValidity = datetime.strptime(datePolicyValidity, "%d/%m/%Y")
    actualDate = datetime.today()
    validity = actualDate - datePolicyValidity
    return validity.days


def validDate(date: str) -> str:
    try:
        dateObj = datetime.strptime(date, '%d/%m/%Y')
        correctDate = dateObj.strftime('%d/%m/%Y')
        return correctDate
    except ValueError:
        raise ValueError("Formato de fecha inválido, por favor ingrese la fecha en el formato dd/mm/yyyy")


def validDateAndAge(date: str) -> bool:
    dateObj = datetime.strptime(date, '%d/%m/%Y')
    actualDate = datetime.now()
    difference = actualDate.year - dateObj.year
    if 0 <= difference <= 150:
        return True
    else:
        raise Exception("Edad ingresada no valida")


def validEmail(email: str) -> bool:
    if "@" not in email and "." not in email:
        raise ValueError("Formato de correo inválido")
    else:
        return True


def validPhoneNumber(phone: str) -> None:
    try:
        if 11 > len(phone) > 0 and phone.isdigit():
            return
    except ValueError:
        raise ValueError("Formato de número de teléfono inválido")


def validPassword(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if bool(re.match(pattern, password)):
        return True
    else:
        raise ValueError("Formato de contraseña inválido")
