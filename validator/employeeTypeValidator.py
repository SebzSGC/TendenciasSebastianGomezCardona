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

def getUpdateEmployeeData(employee, attribute):
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
            newInfo = typeValidator.validRole(newInfo)
        if newInfo == "Opción inválida":
            print("Opción inválida")
        if attribute in correctAttributes:
            oldAttribute = getattr(employee, correctAttributes[attribute])
            newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
            HumanResources.updateEmployee(employee, correctAttributes[attribute], newInfo, oldAttribute)
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
            newRole = input("1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
            newRole = typeValidator.validRole(newRole)
            HumanResources.updateRol(hospital, employeeUser, newRole)
    except Exception as error:
        print(str(error))