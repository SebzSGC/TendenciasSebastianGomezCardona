def validRole(newRole):
    rolOptions = {
    "1": "Administrador",
    "2": "Doctor",
    "3": "Enfermera",
    "4": "Soporte",
    "5": "Recursos Humanos"
    }
    return rolOptions.get(newRole, "Opción inválida")

def manageEmployeeRole(hospital, loginService, HumanResources):
    employeeUserName = input("ingrese el nombre de usuario del empleado:\n")
    employeeUser = loginService.searchEmployee(hospital,employeeUserName)
    if employeeUser==None:
        print("usuario no encontrado")
    else:
        print(f"Empleado: {employeeUser.fullName} encontrado")
        newRole = input("1. Administrador\n2. Doctor\n3. Enfermera\n4. Soporte\n5. Recursos Humanos\n")
        newRole = validRole(newRole)
        HumanResources.reAssignRol(hospital, employeeUser, newRole)