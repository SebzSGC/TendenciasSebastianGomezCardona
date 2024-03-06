from model.User import *
from model.Employee import Employee
from model.Hospital import Hospital
from service import loginService
from validator import userTypeValidator, typeValidator, employeeTypeValidator
from service.RolService import AdministrativePersonal, Doctor, Nurse, HumanResources, InformationSupport

hospital = Hospital()
employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "1990/01/01", "123 Main St", "Recursos Humanos", "johndoe", "password")
employee2 = Employee("sebastian", "123456789", "johndoe@example.com", "1234567890", "1990/01/01", "123 Main St", "Administrador", "sebz", "password")
employee3 = Employee("doctor", "123456789", "johndoe@example.com", "1234567890", "1990/01/01", "123 Main St", "Doctor", "doctor", "doctor")
patient = Patient("123","paciente","1990/03/02", "masculino", "123 Main St", "123456","test@2")

hospital.employees.append(employee1)
hospital.employees.append(employee2)
hospital.employees.append(employee3)
hospital.patients.append(patient)

#SUBMENUS
def isNotNoneUpatedUser(userToUpdate):
    if userToUpdate == None:
        print("Usuario no encontrado")
        return
    employeeTypeValidator.validEmployeeData(userToUpdate)
    print("Informacion actualizada con éxito")

def isNotNoneUpatedPatient(hospital, userToUpdate):
    if userToUpdate == None:
        print("Usuario no encontrado")
        return
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
            document = input("Ingrese el documento del paciente:\n")
            userTypeValidator.getAppointmetData(hospital, document)
        elif option=="4":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def HumanResourcesMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de recursos humanos: {currentUser.fullName}")
        option=input("1. crear empleado \n2. cambiar rol de empleado \n3. elimwinar empleado \n4. actualizar informacion de empleado\n5. ver a todos los empleados \n6. cerrar sesion\n")
        if option=="1":
            employeeTypeValidator.getEmployeeData(hospital)
        elif option=="2":
            employeeTypeValidator.getReAssignRolData(hospital)
        elif option=="3":
            deleteEmployee = input("ingrese el nombre de usuario del empleado a eliminar:\n")
            employeeTypeValidator.getDeleteEmployeeData(hospital, deleteEmployee) 
        elif option=="4":
            userToUpdateName = input("Ingrese el nombre completo del paciente a actualizar:\n")
            userToUpdate = loginService.searchEmployee(hospital, userToUpdateName)
            isNotNoneUpatedUser(userToUpdate)
        elif option == "5":
            employeeTypeValidator.getAllEmployeesData(hospital)
        elif option == "6":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def doctorMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de doctor: {currentUser.fullName}")
        option=input("1. ver datos del paciente \n2. Generar historia clinica \n3. cerrar sesion\n")
        if option=="1":
            patientDocument = input("Ingrese el documento del paciente:\n")
            userTypeValidator.getClinicalHistoryData(hospital, patientDocument, currentUser.idNumber)
        elif option=="2":
            pass
        elif option=="3":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def nurseMenu(hospital, currentUser):
    print("Inicializando menu de enfermera")

def supportMenu(hospital, currentUser):
    print("Inicializando menu de soporte")

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
