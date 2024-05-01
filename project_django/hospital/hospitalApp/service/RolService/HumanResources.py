from hospitalApp.service import validatorService
from hospitalApp.validator import typeValidator, userTypeValidator, employeeTypeValidator
from hospitalApp import models


def createEmployee(fullName: str, email: str, phoneNumber: str, bornDate: str, address: str,
                   rol: str, userName: str, password: str) -> None:
    typeValidator.validEmail(email)
    typeValidator.validPhoneNumber(phoneNumber)
    typeValidator.validDateAndAge(bornDate)
    typeValidator.validPassword(password)
    if len(address) > 30:
        raise Exception("Dirección muy larga")
    if validatorService.validateEmployeeByUserName(userName) and userName.isalnum() and len(userName) <= 15:
        raise Exception("ya existe un empleado con ese nombre de usuario o no cumple los requisitos")
    employee = models.Employee(fullName=fullName, email=email, phoneNumber=phoneNumber, bornDate=bornDate,
                               address=address, rol=rol,
                               userName=userName, password=password)
    employee.save()


def updateEmployee(id: int, fullName: str, email: str, phoneNumber: str, bornDate: str, address: str,
                   rol: str, userName: str, password: str) -> None:
    typeValidator.validEmail(email)
    typeValidator.validPhoneNumber(phoneNumber)
    typeValidator.validDateAndAge(bornDate)
    typeValidator.validPassword(password)
    if len(address) > 30:
        raise Exception("Dirección muy larga")
    if validatorService.validateEmployeeByUserName(userName) and userName.isalnum() and len(userName) <= 15:
        raise Exception("ya existe un empleado con ese nombre de usuario o no cumple los requisitos")
    if validatorService.validateEmployeeById(id):
        models.Patient.objects.filter(id=id).update(fullName=fullName, bornDate=bornDate, rol=rol,
                                                    address=address, phoneNumber=phoneNumber,
                                                    email=email)


def deleteEmployee(id: int) -> None:
    if validatorService.validateEmployeeById(id):
        models.Employee.objects.filter(id=id).delete()
    else:
        raise Exception("El empleado no existe")
