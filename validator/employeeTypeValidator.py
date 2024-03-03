import service.RolService.HumanResources as HumanResources
import validator.typeValidator as typeValidator
import service.loginService as loginService

def getEmployeeData(hospital):
    try:
        print("Por favor ingrese los datos del empleado:")
        fullName = input("Nombre completo: ")
        idNumber = input("Número de identificación: ")
        email = input("Correo electrónico: ")
        phoneNumber = input("Número de teléfono: ")
        bornDate = input("Fecha de nacimiento (YYYY-MM-DD): ")
        adress = input("Dirección: ")
        rol = "Opción inválida"
        while rol == "Opción inválida":
            print("Por favor seleccione el rol del empleado:")
            rol = input("1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
            rol = typeValidator.validRole(rol)
        userName = input("Nombre de usuario: ")
        password = input("Contraseña: ")
        HumanResources.createEmployee(hospital, fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password)
    except Exception as error:
        print(str(error))

def getUpdateEmployeeData(employee, attribute, newValue):
    try:
        correctAttributes = {
            "1": "fullName",
            "2": "idNumber",
            "3": "email",
            "4": "phone",
            "5": "bornDate",
            "6": "adress",
            "7": "rol",
            "8": "userName",
            "9": "password"
        }

        attributeNames = {
            "1": "Nombre Completo",
            "2": "Documento de identidad",
            "3": "Correo electrónico",
            "4": "Telefono",
            "5": "Fecha de nacimiento",
            "6": "Dirección",
            "7": "Rol",
            "8": "Nombre de usuario",
            "9": "Contraseña"
        }
        if attribute == "7":
            newValue = typeValidator.validRole(newValue)
        if newValue == "Opción inválida":
            raise Exception("Opción inválida")
        if attribute in correctAttributes:
            oldAttribute = getattr(employee, correctAttributes[attribute])
            print(f"El valor actual de {attributeNames[attribute]} es: {oldAttribute}")
            HumanResources.updateEmployee(employee, correctAttributes[attribute], newValue, oldAttribute)
    except Exception as error:
        print(str(error))

def getDeleteEmployeeData(hospital, user):
    try:
        deleteUser = loginService.searchEmployee(hospital, user)
        if deleteUser == None:
            print("Usuario no encontrado")
        else:
            HumanResources.deleteEmployee(hospital, deleteUser)
    except Exception as error:
        print(str(error))

def getAllEmployeesData(hospital):
    try:
        HumanResources.getAllEmployees(hospital)
    except Exception as error:
        print(str(error))

def getReAssignRolData(hospital):
    try:
        employeeUserName = input("ingrese el nombre de usuario del empleado:\n")
        employeeUser = loginService.searchEmployee(hospital,employeeUserName)
        if employeeUser==None:
            print("usuario no encontrado")
        else:
            print(f"Empleado: {employeeUser.fullName} encontrado")
            print("¿Qué rol deseas asignar?")
            newRole = input("1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
            newRole = typeValidator.validRole(newRole)
            HumanResources.updateRol(hospital, employeeUser, newRole)
    except Exception as error:
        print(str(error))

def validEmployeeData(userToUpdate):
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
        getUpdateEmployeeData(userToUpdate, attribute, newValue)