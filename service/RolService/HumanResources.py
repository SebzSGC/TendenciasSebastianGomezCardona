def createEmployee(hospital, user):
    hospital.employees.append(user)
    return print(f"Empleado: {user.fullName} creado con éxito")

def deleteEmployee(hospital, user, loginService):
    deletedUser = loginService.searchEmployee(hospital, user)
    if deletedUser == None:
        return print("Usuario no encontrado")
    else:
        hospital.employees.remove(deletedUser)
        return print(f"Empleado: {deletedUser.fullName} eliminado con éxito")
    
def getAllEmployees(hospital):
    if len(hospital.employees) == 0:
        return print("No hay empleados registrados en el sistema")
    userNumber = 1
    for employee in hospital.employees:
        print("---Lista de empleados---")
        print(f"Empleado {userNumber}:")
        print(
        f"Nombre Completo: {employee.fullName}\nDocumento: {employee.idNumber}\nCorreo electrónico: {employee.email}\nNúmero de teléfono: {employee.phoneNumber}\nFecha de nacimiento: {employee.bornDate}\nDirección: {employee.adress}\nRol: {employee.rol}\nNombre de usuario: {employee.userName}\nContraseña: {employee.password}\n ")
        userNumber += 1
    return print("Usuarios cargados con éxito")    
def reAssignRol(hospital, user, newRol):
   oldRol = hospital.employees[hospital.employees.index(user)].role 
   hospital.employees[hospital.employees.index(user)].role = newRol
   return print(f"Rol de {user.fullName} cambiado de {oldRol} a {newRol} con éxito")