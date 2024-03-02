from model.User import *
from model.Employee import Employee
from model.Hospital import Hospital
from service import loginService
from validator import typeValidator
from service.RolService import AdministrativePersonal, Doctor, Nurse, HumanResources, InformationSupport

hospital = Hospital()
employee1 = Employee("John Doe", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Recursos Humanos", "johndoe", "password")
employee2 = Employee("sebastian", "123456789", "johndoe@example.com", "1234567890", "1990-01-01", "123 Main St", "Administrador", "sebz", "password")

hospital.employees.append(employee1)
hospital.employees.append(employee2)

def menuUpdateContactEmergency(userToUpdate):
    while True:
        print("¿Qué información deseas cambiar?")
        attribute = input("1. Nombre completo \n2. Relación\n3. Número de teléfono\n4. Regresar\n")
        if attribute not in ["1", "2", "3", "4"]:
           return print("Opción inválida")
        if attribute == "4":
            break
        newValue = input("ingrese el nuevo valor:\n")
        contact = userToUpdate.emergencyContact.updateEmergencyContact(attribute, newValue)
        if contact == "Opción inválida":
            print("Opción inválida")
            continue
        print("Informacion de contacto de emergencia actualizada con éxito")
        option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
        if option == "2":
            break
        if option == "1":
            continue
    return

def menuUpdateInsurance(userToUpdate):
    while True:
        attribute = input("1. Nombre de la compañia de seguros \n2. Numero de poliza\n3. Estado de la poliza\n4. Vigencia de la poliza\n5. Regresar\n")
        if attribute not in ["1", "2", "3", "4", "5"]:
           return print("Opción inválida")
        if attribute == "5":
            break
        newValue = input("ingrese el nuevo valor:\n")
        insurance = userToUpdate.medicalInsurance.updateMedicalInsurance(attribute, newValue)
        if insurance == "Opción inválida":
            print("Opción inválida")
            continue
        print("Informacion de la poliza actualizada con éxito")
        option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
        if option == "2":
            break
        if option == "1":
            continue
    return

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
        userToUpdate.updateEmployee(attribute, newValue, typeValidator)

def isNotNoneUpatedPatient(userToUpdate):
    if userToUpdate == None:
        print("Usuario no encontrado")
        return
    while True:
        print("¿Qué información deseas cambiar?")
        attribute = input("1. Nombre completo \n2. Fecha de nacimiento\n3. Genero\n4. Direccion\n5. Numero de telefono\n6. Correo electronico\n7. Regresar\n")
        if attribute not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Opción inválida")
            continue
        if attribute == "7":
            break
        newValue = input("ingrese el nuevo valor:\n")
        userToUpdate.updatePatient(attribute, newValue)
        option = input("Deseas actualizar la informacion de contacto de emergencia?\n1. Si\n2. No\n")
        if option == "1":
            menuUpdateContactEmergency(userToUpdate)
        option = input("Deseas actualizar la informacion de la poliza?\n1. Si\n2. No\n")
        if option == "1":
            menuUpdateInsurance(userToUpdate)
        else:
            break
    return

#MENUS
def adminMenu(hospital, currentUser):
    while True:
        print(f"Inicializando menu de administrador: {currentUser.fullName}")
        option=input("1. Registrar paciente \n2. Actualizar paciente\n3. Programar cita\n4. cerrar sesion\n5. cerrar sesion\n6. cerrar sesion\n")
        if option=="1":
            newPatient = User.createPatient(hospital.patients, hospital)
            contact = EmergencyContact.createEmergencyContact(newPatient.id, newPatient.fullName)
            newPatient.emergencyContact = contact
            insurance = MedicalInsurance.createMedicalInsurance(newPatient.id, newPatient.fullName)
            newPatient.medicalInsurance = insurance
            AdministrativePersonal.createPatient(hospital, newPatient)
        elif option=="2":
            userToUpdate = input("ingrese el nombre completo del paciente a actualizar:\n")
            userToUpdate = loginService.searchPatient(hospital, userToUpdate)
            isNotNoneUpatedPatient(userToUpdate)
        elif option=="3":
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
    elif isinstance(currentUser, User):
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
