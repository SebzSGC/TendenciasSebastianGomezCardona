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

def validDate(date):
    try:
        date_objt = datetime.datetime.strptime(date, '%d/%m/%Y')
        correctDate = date_objt.strftime('%d/%m/%Y')
        return correctDate
    except ValueError:
        raise ValueError("Formato de fecha inválido, por favor ingrese la fecha en el formato dd/mm/yyyy")