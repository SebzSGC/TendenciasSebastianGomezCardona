from django.forms import model_to_dict
from ... import models
from ...validator import typeValidator, userTypeValidator, employeeTypeValidator
from hospital.connection_mongo import collection
from .. import validatorService


def createPatient(idDocument: int, fullName: str, bornDate: str, genre: str, address: str, phoneNumber: str,
                  email: str) -> None:
    typeValidator.validEmail(email)
    typeValidator.validPhoneNumber(phoneNumber)
    typeValidator.validDateAndAge(bornDate)
    if len(address) > 30:
        raise Exception("Dirección muy larga")
    if validatePatientId(idDocument):
        raise Exception("El paciente ya existe")
    patient = models.Patient(idDocument, fullName, bornDate, genre, address, phoneNumber, email)
    patient.save()
    clinicalHistory = {"_id": str(patient.idDocument), "historias": {}}
    collection.insert_one(clinicalHistory)


def createEmergencyContact(fullName: str, relationship: str, phoneNumber: str, patientId: int) -> None:
    typeValidator.validPhoneNumber(phoneNumber)
    if validatePatientId(patientId):
        patient = validatorService.getPatientById(patientId)
        emergencyContact = models.EmergencyContact(idPatient=patient,
                                                   fullName=fullName, relationship=relationship,
                                                   phoneNumber=phoneNumber)
        emergencyContact.save()
    else:
        raise Exception("No se permite asignar un contacto de emergencia a un paciente que no existe")


def createMedicalInsurance(idPatient: int, nameOfInsuranceCompany: str, policyNumber: int, policyState: bool,
                           policyValidity: str) -> None:
    if validatorService.validatePatientById(idPatient):
        patient = models.Patient(**validatorService.getPatientById(idPatient))
        insurance = models.MedicalInsurance(idPatient=patient, nameOfInsuranceCompany=nameOfInsuranceCompany,
                                            policyNumber=policyNumber, policyState=policyState,
                                            policyValidity=policyValidity)
        insurance.save()
    else:
        raise Exception("No se permite asignar un seguro medico a un paciente que no existe")


def updatePatient(idDocument: int, fullName: str, bornDate: str, genre: str, address: str, phoneNumber: str,
                  email: str) -> None:
    typeValidator.validEmail(email)
    typeValidator.validPhoneNumber(phoneNumber)
    typeValidator.validDateAndAge(bornDate)
    if len(address) > 30:
        raise Exception("Dirección muy larga")
    if validatorService.validatePatientById(idDocument):
        models.Patient.objects.filter(idDocument=idDocument).update(fullName=fullName, bornDate=bornDate, genre=genre,
                                                                    address=address, phoneNumber=phoneNumber,
                                                                    email=email)
    else:
        raise Exception("El paciente no existe")


def updateEmergencyContact(idPatient: int, fullName: str, relationship: str, phoneNumber: str) -> None:
    if validatorService.validatePatientById(idPatient):
        models.EmergencyContact.objects.filter(idPatient=idPatient).update(fullName=fullName, relationship=relationship,
                                                                           phoneNumber=phoneNumber)
    else:
        raise Exception("El contacto de emergencia no existe")


def updateMedicalInsurance(idPatient: int, nameOfInsuranceCompany: str, policyNumber: int, policyState: bool,
                           policyValidity: str) -> None:
    if validatorService.validatePatientById(idPatient):
        models.MedicalInsurance.objects.filter(idPatient=idPatient).update(
            nameOfInsuranceCompany=nameOfInsuranceCompany, policyNumber=policyNumber, policyState=policyState,
            policyValidity=policyValidity)
    else:
        raise Exception("El seguro medico no existe")

# def generateAppointment(hospital, patient, doctor, date):
#     if patient == None:
#         raise Exception("El paciente no existe")
#     if doctor == None:
#         raise Exception("El doctor no existe")
#     date = typeValidator.validDate(date)
#     appointment = MedicalAppointment(patient.id, doctor.idNumber, date)
#     hospital.appointments.append(appointment)
#     print(f"Cita programada para el paciente: {patient.fullName}, el dia {date} con el doctor: {doctor.fullName}")
#
#
# def generateInvoice(hospital, patient, appointment):
#     totalToPay = 0
#     idDoctor = appointment["DoctorDocument"]
#     invoice = Invoice(appointment, patient)
#     doctor = validDoctorId(hospital, idDoctor)
#     printInvoiceDetails(invoice, doctor)
#     totalToPay = calculateTotalToPay(hospital, invoice, totalToPay)
#     printTotalToPay(invoice, totalToPay)
#
#
# def printInvoiceDetails(invoice, doctor):
#     print(
#         f"Factura generada para el paciente: {invoice.patient.fullName}, con la cita: {invoice.medicalAppointment['Date']}")
#     print("Nombre del paciente: ", invoice.patient.fullName)
#     print("Edad del paciente: ", typeValidator.getCorrectAge(invoice.patient.bornDate))
#     print("Cedula del paciente", invoice.patient.id)
#     print("Nombre del doctor: ", doctor.fullName)
#     print("Nombre de la compañia de seguro del paciente: ", invoice.patient.medicalInsurance.nameOfInsuranceCompany)
#     print("Numero de poliza del paciente: ", invoice.patient.medicalInsurance.policyNumber)
#     print("Dias de vigencia de la poliza: ",
#           typeValidator.getValidityPolicy(invoice.patient.medicalInsurance.policyValidity))
#     print("Fecha de la finalizacion de la poliza: ", invoice.patient.medicalInsurance.policyValidity)
#
#
# def calculateTotalToPay(hospital, invoice, totalToPay):
#     if invoice.medicalAppointment["order"]["orderMedications"]:
#         print("Medicamentos: ")
#         totalToPay = calculateTotalForMedications(hospital, invoice, totalToPay)
#     else:
#         print("No se recetaron medicamentos")
#
#     if invoice.medicalAppointment["order"]["orderProcedures"]:
#         print("Procedimientos: ")
#         calculateTotalForProcedures(hospital, invoice)
#     else:
#         print("No se programaron procedimientos")
#     return totalToPay
#
#
# def calculateTotalForMedications(hospital, invoice, totalToPay):
#     for medication in invoice.medicalAppointment["order"]["orderMedications"]:
#         if medication == "idMedication":
#             infoMedicine = getMedicineById(hospital, invoice.medicalAppointment["order"]["orderMedications"]["item"])
#             print(" item: ", invoice.medicalAppointment["order"]["orderMedications"]["item"])
#             print("     Medicamento: ", infoMedicine.name)
#             print("     Cantidad: ", infoMedicine.dosage)
#             print("     Precio: ", infoMedicine.price)
#             totalToPay += infoMedicine.price
#     return totalToPay
#
#
# def calculateTotalForProcedures(hospital, invoice):
#     for procedure in invoice.medicalAppointment["order"]["orderProcedures"]:
#         if procedure == "idProcedure":
#             infoProcedure = getProcedureById(hospital, invoice.medicalAppointment["order"]["orderProcedures"]["item"])
#             print(" item: ", invoice.medicalAppointment["order"]["orderProcedures"]["item"])
#             print("     Procedimiento: ", infoProcedure.name)
#             print("     Descripcion: ", infoProcedure.description)
#
#
# def printTotalToPay(invoice, totalToPay):
#     if invoice.patient.medicalInsurance.policyState == True:
#         print("El paciente cuenta con seguro medico")
#         print("Copago de: $", 50000)
#         print("Precio por medicamentos: ", totalToPay)
#         print("Total a pagar: ", 50000)
#     else:
#         print("El paciente no cuenta con seguro medico")
#         print("Precio por medicamentos: ", totalToPay)
#         print("Total a pagar: ", totalToPay)
