from model.Order import Order, OrderMedication, OrderProcedure
from model.Procedure import Procedure
from model.User import *
from model.Employee import Employee
from model.Hospital import Hospital
from model.Medication import Medication
from service import loginService
from validator import userTypeValidator, typeValidator, employeeTypeValidator
from service.RolService import AdministrativePersonal, Doctor, Nurse, HumanResources, InformationSupport

hospital = Hospital()
EmergencyContact1 = EmergencyContact("123", "Juan Perez", "Padre", "1234567890")
MedicalInsurance1 = MedicalInsurance("123", "Sura", "123456789", "Activo", "13/03/2024")
employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "27/02/2004", "123 Main St", "Recursos Humanos", "johndoe", "password")
employee2 = Employee("sebastian", "123456789", "johndoe@example.com", "1234567890", "27/02/2004", "123 Main St", "Administrador", "sebz", "password")
employee3 = Employee("doctor", "123456789", "johndoe@example.com", "1234567890", "27/02/2004", "123 Main St", "Doctor", "doctor", "doctor")
employee4 = Employee("nurse", "123456789", "johndoe@example.com", "1234567890", "27/02/2004", "123 Main St", "Enfermera", "nurse", "nurse")
patient = Patient("123","paciente","27/02/2004", "masculino", "123 Main St", "123456","test@2")
patient.emergencyContact = EmergencyContact1
patient.medicalInsurance = MedicalInsurance1
medicina = Medication("1","pepa", 2500, "25gr")
procedure = Procedure("1", "Cirugia de corazon", "Cirugia")
actualOrder = Order("1", "123", "123456789", "09/03/2024")
actualMedication = OrderMedication("1", "1", "2", "3", "2","1")
actualOrder2 = Order("2", "123", "123456789", "13/03/2024")
actualMedication2 = OrderMedication("2", "1", "2", "3", "2","1") 
actualProcedure2 = OrderProcedure("2", "1", "2", "3", False, None, "1")
order2 = vars(actualOrder2)
order2["orderMedications"] = vars(actualMedication2)
order2["orderProcedures"] = vars(actualProcedure2)
newClinicalHistory2 = {
        "Date": "13/03/2024",
        "DoctorDocument": "123456789",
        "consultReason": "consultReason",
        "symptomatology": "symptomatology",
        "diagnosis": "diagnosis",
        "order": order2
    }
order = vars(actualOrder)
order["orderMedications"] = vars(actualMedication)
newClinicalHistory = {
        "Date": "09/03/2024",
        "DoctorDocument": "123456789",
        "consultReason": "consultReason",
        "symptomatology": "symptomatology",
        "diagnosis": "diagnosis",
        "order": order
    }

hospital.orders.append(order)
hospital.orders.append(order2)
hospital.employees.append(employee1)
hospital.employees.append(employee2)
hospital.employees.append(employee3)
hospital.employees.append(employee4)
hospital.patients.append(patient)
hospital.clinicalHistories["123"] = {}
hospital.clinicalHistories["123"]["09/03/2024"] = newClinicalHistory
hospital.clinicalHistories["123"]["13/03/2024"] = newClinicalHistory2
hospital.stockMedicine.append(medicina)
hospital.procedures.append(procedure)

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
        option=input("1. Registrar paciente \n2. Actualizar paciente\n3. Programar cita\n4. Generar factura\n5. cerrar sesion\n")
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
            document = input("Ingrese el documento del paciente:\n")
            userTypeValidator.getInvoiceData(hospital, document)
        elif option=="5":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def HumanResourcesMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de recursos humanos: {currentUser.fullName}")
        option=input("1. crear empleado \n2. cambiar rol de empleado \n3. eliminar empleado \n4. actualizar informacion de empleado\n5. ver a todos los empleados \n6. cerrar sesion\n")
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
            userTypeValidator.getAllPatientData(hospital)
        elif option=="2":
            userTypeValidator.getClinicalHistoryData(hospital, currentUser.idNumber)
        elif option=="3":
            print("cerrando sesion...")
            return
        else:
            print("opcion no valida")
            continue

def nurseMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de enfermera: {currentUser.fullName}")
        option=input("1. ver datos del paciente \n2. Generar registro de visita\n3. cerrar sesion\n")
        if option=="3":
            break
        if option=="1":
             userTypeValidator.getAllPatientData(hospital)
        if option=="2":
            userTypeValidator.getVitalData(hospital)
                  

def supportMenu(hospital, currentUser):
    print("Inicializando menu de soporte")

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
