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

def reAssignRol(hospital, user, newRol):
   oldRol = hospital.employees[hospital.employees.index(user)].rol 
   hospital.employees[hospital.employees.index(user)].rol = newRol
   return print(f"Rol de {user.fullName} cambiado de {oldRol} a {newRol} con éxito")