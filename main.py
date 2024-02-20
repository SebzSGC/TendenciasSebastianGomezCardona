from model import User 
from model import Employee
from model import Hospital
from service import loginService 

employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Manager", "johndoe", "password")

def adminMenu(hospital, user):
    print("Inicializando menu de administrador")

def doctorMenu(hospital, user):
    print("Inicializando menu de doctor")

def nurseMenu(hospital, user):
    print("Inicializando menu de enfermera")

def supportMenu(hospital, user):
    print("Inicializando menu de soporte")

def HumanResourcesMenu(hospital, user):
    print("Inicializando menu de recursos humanos")

def userMenu(hospital, user):
    print("Inicializando menu de usuario")

def loginRouter(hospital,user):
    if isinstance(user, Employee):
        if user.rol=="Administrador":
            adminMenu(hospital,user)
        elif user.rol=="Doctor":
            doctorMenu(hospital,user)
        elif user.rol=="Enfermera":
            nurseMenu(hospital,user)
        elif user.rol=="Soporte":
            supportMenu(hospital,user)
        elif user.rol=="Recursos Humanos":
            HumanResourcesMenu(hospital,user)
    elif isinstance(user, User):
        userMenu(hospital,user)

initialMenu="1. iniciar sesion\n0. cerrar programa\n"


while True:
    option=input(initialMenu)
    print("ha elegido la opcion", option)
    if option=="1":
        print("ingrese su usuario:")
        userName = input()
        password = input("ingrese la contraseña:\n")
        print("eres un empleado?:")
        userType = input("1. si\n2. no\n")
        if userType=="1":
            user = loginService.searchEmployee(Hospital,userName)
        elif userType=="2":
            user = loginService.searchPatient(Hospital,userName)
        else:
            print("opcion no valida")
            continue
        if user==None:
            print("usuario no encontrado")
            continue
        if user.password!=password:
            print("error de usuario o contraseña")
            continue
        loginRouter(Hospital,user)
    if option == "0":
        print("chau")
        break


