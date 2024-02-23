from model.User import User
from model.Employee import Employee
from model.Hospital import Hospital
from service import loginService
from validator import typeValidator
from service.RolService import AdministrativePersonal, Doctor, Nurse, HumanResources, InformationSupport

hospital = Hospital()
employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Recursos Humanos", "johndoe", "password")
hospital.employees.append(employee1)

def isNotNone(userToUpdate):
    if userToUpdate == None:
        print("Usuario no encontrado")
        return
    print("¿Qué información deseas cambiar?")
    attribute = input("1. Nombre completo \n2. Numero de identificacion \n3. Correo electrónico \n4. Número de teléfono \n5. Fecha de nacimiento (YYYY-MM-DD)\n6. Dirección\n7. Rol\n8. Nombre de usuario\n9. Contraseña\n")
    newValue = input("ingrese el nuevo valor:\n")
    userToUpdate.updateEmployee(attribute, newValue)

#MENUS
def adminMenu(hospital, currentUser):
    print("Inicializando menu de administrador")

def doctorMenu(hospital, currentUser):
    print("Inicializando menu de doctor")

def nurseMenu(hospital, currentUser):
    print("Inicializando menu de enfermera")

def supportMenu(hospital, currentUser):
    print("Inicializando menu de soporte")

def HumanResourcesMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de recursos humanos: {currentUser.fullName}")
        option=input("1. crear empleado \n2. cambiar rol de empleado \n3. eliminar empleado \n4. actualizar informacion de empleado \n5. cerrar sesion\n")
        if option=="1":
            newUser = Employee.createEmployee(typeValidator)
            HumanResources.createEmployee(hospital, newUser)
        elif option=="2":
            typeValidator.manageEmployeeRole(hospital, loginService, HumanResources)
        elif option=="3":
            deleteEmployee = input("ingrese el nombre de usuario del empleado a eliminar:\n")
            HumanResources.deleteEmployee(hospital, deleteEmployee, loginService)  
        elif option=="4":
            userToUpdate = input("ingrese el nombre de usuario del empleado a actualizar:\n")
            userToUpdate = loginService.searchEmployee(hospital, userToUpdate)
            isNotNone(userToUpdate)
        elif option == "5":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def userMenu(hospital, currentUser):
    print("Inicializando menu de usuario")
#RUTAS DE MENUS
def loginRouter(hospital,currentUser):
    if isinstance(currentUser, Employee):
        if currentUser.rol=="Administrador":
            adminMenu(hospital,currentUser)
        elif currentUser.rol=="Doctor":
            doctorMenu(hospital,currentUser)
        elif currentUser.rol=="Enfermera":
            nurseMenu(hospital,currentUser)
        elif currentUser.rol=="Soporte":
            supportMenu(hospital,currentUser)
        elif currentUser.rol=="Recursos Humanos":
            HumanResourcesMenu(hospital,currentUser)
    elif isinstance(currentUser, User):
        userMenu(hospital,currentUser)

initialMenu="1. iniciar sesion\n0. cerrar programa\n"


while True:
    option=input(initialMenu)
    if option=="1":
        userName = input("ingrese su usuario:\n")
        password = input("ingrese la contraseña:\n")
        userType = None
        while userType not in["1","2"]:
            print("eres un empleado?:")
            userType = input("1. si\n2. no\n")
        if userType=="1":
            currentUser = loginService.searchEmployee(hospital,userName)
        elif userType=="2":
            currentUser = loginService.searchPatient(hospital,userName)
        else:
            print("opcion no valida")
            continue
        if currentUser==None:
            print("usuario no encontrado")
            continue
        if currentUser.password!=password:
            print("error de usuario o contraseña")
            continue
        loginRouter(hospital,currentUser)
    elif option == "0":
        print("Saliendo...")
        break
    else:
        print("opcion no valida")
        continue
