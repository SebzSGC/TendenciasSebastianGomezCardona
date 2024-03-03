from model.User import *
from model.Employee import Employee
from model.Hospital import Hospital
from service import loginService
from validator import userTypeValidator, typeValidator, employeeTypeValidator
from service.RolService import AdministrativePersonal, Doctor, Nurse, HumanResources, InformationSupport

hospital = Hospital()
employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Recursos Humanos", "johndoe", "password")
employee2 = Employee("sebastian", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Administrador", "sebz", "password")

hospital.employees.append(employee1)
hospital.employees.append(employee2)

#SUBMENUS
def isNotNoneUpatedUser(userToUpdate):
    if userToUpdate == None:
        print("Usuario no encontrado")
        return
    while True:
        print("¿Qué información deseas cambiar?")
        attribute = input("1. Nombre completo \n2. Numero de identificacion \n3. Correo electrónico \n4. Número de teléfono \n5. Fecha de nacimiento (YYYY-MM-DD)\n6. Dirección\n7. Rol\n8. Nombre de usuario\n9. Contraseña\n10. Regresar\n")
        if attribute not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Opción inválida")
            continue
        if attribute == "10":
            break
        if attribute == "7":
            newValue = input("Que rol deseas asignar?\n1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
        else:
            newValue = input("ingrese el nuevo valor:\n")
        userToUpdate.updateEmployee(attribute, newValue, )

def isNotNoneUpatedPatient(hospital, userToUpdate):
    if userToUpdate == None:
        return print("Usuario no encontrado")
    userTypeValidator.validPatientData(hospital, userToUpdate)
    print("Informacion actualizada con éxito")
    
#MENUS
def adminMenu(hospital, currentUser):
    print(f"Inicializando menu de administrador: {currentUser.fullName}")
    while True:
        option=input("1. Registrar paciente \n2. Actualizar paciente\n3. Programar cita\n4. cerrar sesion\n")
        if option=="1":
            userTypeValidator.getPatientData(hospital)
            newPatient = hospital.patients[-1]
            userTypeValidator.getEmergencyContactData(hospital, newPatient)
            userTypeValidator.getMedicalInsuranceData(hospital, newPatient)
            userTypeValidator.allDataCompletePatient(hospital, newPatient)
        elif option=="2":
            userToUpdateName = input("Ingrese el nombre completo del paciente a actualizar:\n")
            userToUpdate = loginService.searchPatient(hospital, userToUpdateName)
            isNotNoneUpatedPatient(hospital, userToUpdate)
        elif option=="3":
            print("proximamente...")
        elif option=="4":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def doctorMenu(hospital, currentUser):
    print("Inicializando menu de doctor")

def nurseMenu(hospital, currentUser):
    print("Inicializando menu de enfermera")

def supportMenu(hospital, currentUser):
    print("Inicializando menu de soporte")

def HumanResourcesMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de recursos humanos: {currentUser.fullName}")
        option=input("1. crear empleado \n2. cambiar rol de empleado \n3. eliminar empleado \n4. actualizar informacion de empleado\n5. ver a todos los empleados \n6. cerrar sesion\n")
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
            isNotNoneUpatedUser(userToUpdate)
        elif option == "5":
            HumanResources.getAllEmployees(hospital)
        elif option == "6":
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
    elif isinstance(currentUser, Patient):
        userMenu(hospital,currentUser)

initialMenu="1. iniciar sesion\n0. cerrar programa\n"


while True:
    option=input(initialMenu)
    if option=="1":
        userName = input("ingrese su usuario:\n")
        password = input("ingrese la contraseña:\n")
        userType = None
        currentUser = loginService.searchEmployee(hospital,userName)
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
