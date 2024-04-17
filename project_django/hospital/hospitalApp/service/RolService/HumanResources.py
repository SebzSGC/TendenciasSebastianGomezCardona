# from model.Employee import Employee
# from HospitalApp.validator import typeValidator
#
#
# def validateEmployeeId(hospital, id):
#     if hospital.employees == []:
#         return None
#     for employee in hospital.employees:
#         if employee.idNumber == id:
#             return employee
#     return None
#
# def validateEmployeeUsernName(hospital, userName):
#     if hospital.employees == []:
#         return None
#     for employee in hospital.employees:
#         if employee.userName == userName:
#             return employee
#     return None
#
# def createEmployee(hospital, fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password):
#     typeValidator.validEmail(email)
#     typeValidator.validPhoneNumber(phoneNumber)
#     typeValidator.validDateAndAge(bornDate)
#     typeValidator.validPassword(password)
#     if len(adress) > 30:
#         raise Exception("Dirección muy larga")
#     if validateEmployeeId(hospital, idNumber):
#         raise Exception("ya existe un empleado con esa cedula registrada")
#     if validateEmployeeUsernName(hospital, userName) and userName.isalnum() and len(userName) <= 15:
#         raise Exception("ya existe un empleado con ese nombre de usuario o no cumple los requisitos")
#     employee = Employee(fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password)
#     hospital.employees.append(employee)
#     print(f"Empleado: {employee.fullName} creado con éxito")
#
# def updateEmployee(employee, attribute, newInfo, oldAttribute):
#     setattr(employee, attribute, newInfo)
#     print(f"Informacion del empleado: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")
#
# def deleteEmployee(hospital, user):
#     if user not in hospital.employees:
#         raise Exception("Empleado no encontrado")
#     hospital.employees.remove(user)
#     print(f"Empleado: {user.fullName} eliminado con éxito")
#
# def getAllEmployees(hospital):
#     if len(hospital.employees) == 0:
#         raise Exception("No hay empleados registrados en el sistema")
#     userNumber = 1
#     for employee in hospital.employees:
#         print("---Lista de empleados---")
#         print(f"Empleado {userNumber}:")
#         print(
#         f"Nombre Completo: {employee.fullName}\nDocumento: {employee.idNumber}\nCorreo electrónico: {employee.email}\nNúmero de teléfono: {employee.phoneNumber}\nFecha de nacimiento: {employee.bornDate}\nDirección: {employee.adress}\nRol: {employee.rol}\nNombre de usuario: {employee.userName}\nContraseña: {employee.password}\n ")
#         userNumber += 1
#     print("Usuarios cargados con éxito")
#
# def updateRol(hospital, user, newRol):
#    oldRol = hospital.employees[hospital.employees.index(user)].rol
#    hospital.employees[hospital.employees.index(user)].rol = newRol
#    print(f"Rol de {user.fullName} cambiado de {oldRol} a {newRol} con éxito")