from hospitalApp import models
from hospitalApp.validator import typeValidator
from hospitalApp.service.RolService import AdministrativePersonal, Doctor, Nurse


def getPatientData(hospital):
    try:
        print("Por favor ingrese los datos del paciente:")
        idDocument = int(input("Numero de documento: "))
        fullName = input("Nombre completo: ")
        bornDate = input("Fecha de nacimiento (DD/MM/AAAA): ")
        genre = "Opción inválida"
        while genre == "Opción inválida":
            print("Por favor seleccione el genero:")
            genre = input("1. Masculino\n2. Femenino\n3. Otro\n")
            genre = typeValidator.validGenre(genre)
        address = input("Dirección: ")
        phoneNumber = input("Número de teléfono: ")
        email = input("Correo electrónico: ")
        AdministrativePersonal.createPatient(idDocument, fullName, bornDate, genre, address, phoneNumber, email)
    except Exception as error:
        print(str(error))


# def allDataCompletePatient(hospital, patient):
#     try:
#         AdministrativePersonal.allDataCompletePatient(hospital, patient)
#     except Exception as error:
#         print(str(error))
#
#
# def getUpdatePatientData(patient, attribute):
#     try:
#         correctAttributes = {
#             "1": "fullName",
#             "2": "bornDate",
#             "3": "genre",
#             "4": "address",
#             "5": "phoneNumber",
#             "6": "address"
#         }
#
#         attributeNames = {
#             "1": "nombre completo",
#             "2": "fecha de nacimiento",
#             "3": "género",
#             "4": "dirección",
#             "5": "número de teléfono",
#             "6": "dirección"
#         }
#
#         if attribute in correctAttributes:
#             oldAttribute = getattr(patient, correctAttributes[attribute])
#             newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
#             AdministrativePersonal.updatePatient(patient, correctAttributes[attribute], newInfo, oldAttribute)
#     except Exception as error:
#         print(str(error))


def getEmergencyContactData(patient: models.Patient):
    try:
        print(f"Por favor ingrese los datos del contacto de emergencia de {patient.fullName}")
        name = input("Nombre completo: ")
        relationship = input("Relación: ")
        phoneNumber = input("Número de teléfono: ")
        AdministrativePersonal.createEmergencyContact(name, relationship, phoneNumber, patient)
    except Exception as error:
        print(str(error))

# def getUpdateEmergencyContactData(hospital, contact, attribute):
#     try:
#         correctAttributes = {
#             "1": "name",
#             "2": "relationship",
#             "3": "phoneNumber",
#         }
#
#         attributeNames = {
#             "1": "nombre",
#             "2": "relación",
#             "3": "número de teléfono",
#         }
#
#         if attribute in correctAttributes:
#             oldAttribute = getattr(contact, correctAttributes[attribute])
#             newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
#             AdministrativePersonal.updateEmergencyContact(hospital, contact, attribute, newInfo, oldAttribute)
#             return True
#         else:
#             return False
#     except Exception as error:
#         print(str(error))
#
#
# def getMedicalInsuranceData(hospital, patient):
#     try:
#         print(f"Por favor ingrese los datos de la poliza de {patient.fullName}")
#         idUser = patient.id
#         nameOfInsuranceCompany = input("Nombre de la compañia de seguros: ")
#         policyNumber = input("Número de poliza:\n")
#         policyState = input("Estado de la poliza (activo/inactivo):\n")
#         if policyState not in ["activo", "inactivo"]:
#             raise Exception("Estado de la poliza inválido")
#         if policyState == "inactivo":
#             policyState = False
#         if policyState == "activo":
#             policyState = True
#         if policyState != "activo" and policyState != "inactivo":
#             policyState = False
#         policyValidity = input("Fecha de finalizacion de la poliza:\n")
#         AdministrativePersonal.createMedicalInsurance(hospital, idUser, nameOfInsuranceCompany, policyNumber,
#                                                       policyState, policyValidity)
#     except Exception as error:
#         print(str(error))
#
#
# def getUpdateMedicalInsuranceData(hospital, insurance, attribute):
#     try:
#         correctAttributes = {
#             "1": "nameOfInsuranceCompany",
#             "2": "policyNumber",
#             "3": "policyState",
#             "4": "policyValidity",
#         }
#
#         attributeNames = {
#             "1": "nombre de la compañia de seguros",
#             "2": "número de poliza",
#             "3": "estado de la poliza",
#             "4": "vigencia de la poliza",
#         }
#
#         if attribute in correctAttributes:
#             oldAttribute = getattr(insurance, correctAttributes[attribute])
#             newInfo = input(f"Ingrese el nuevo dato para {attributeNames[attribute]}: ")
#             AdministrativePersonal.updateMedicalInsurance(hospital, insurance, attribute, newInfo, oldAttribute)
#             return True
#         else:
#             return False
#     except Exception as error:
#         print(str(error))
#
#
# def validMedicalInsuranceData(hospital, userToUpdate):
#     while True:
#         attribute = input(
#             "1. Nombre de la compañia de seguros \n2. Numero de poliza\n3. Estado de la poliza\n4. Vigencia de la poliza\n5. Regresar\n")
#         if attribute not in ["1", "2", "3", "4", "5"]:
#             return print("Opción inválida")
#         if attribute == "5":
#             break
#         isValid = getUpdateMedicalInsuranceData(hospital, userToUpdate.medicalInsurance, attribute)
#         if not isValid:
#             print("Opción inválida")
#             continue
#         option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
#         if option == "2":
#             break
#         if option == "1":
#             continue
#
#
# def validContactEmergencyData(hospital, userToUpdate):
#     while True:
#         print("¿Qué información deseas cambiar?")
#         attribute = input("1. Nombre completo \n2. Relación\n3. Número de teléfono\n4. Regresar\n")
#         if attribute not in ["1", "2", "3", "4"]:
#             return print("Opción inválida")
#         if attribute == "4":
#             break
#         isValid = getUpdateEmergencyContactData(hospital, userToUpdate.emergencyContact, attribute)
#         if not isValid:
#             print("Opción inválida")
#             continue
#         option = input("Deseas actualizar otro campo?\n1. Si\n2. No\n")
#         if option == "2":
#             break
#         if option == "1":
#             continue
#
#
# def validPatientData(hospital, userToUpdate):
#     while True:
#         print("¿Qué información deseas cambiar?")
#         attribute = input(
#             "1. Nombre completo \n2. Fecha de nacimiento\n3. Genero\n4. Direccion\n5. Numero de telefono\n6. Correo electronico\n7. Contacto de emergencia\n8. Poliza\n9. Regresar\n")
#         if attribute not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#             print("Opción inválida")
#             continue
#         if attribute == "9":
#             break
#         getUpdatePatientData(userToUpdate, attribute)
#         if attribute == "7":
#             menuUpdateContactEmergency(hospital, userToUpdate)
#         if attribute == "8":
#             menuUpdateInsurance(hospital, userToUpdate)
#         else:
#             break
#
#
# def getAppointmetData(hospital, document):
#     try:
#         patient = AdministrativePersonal.validatePatientId(hospital, document)
#         doctor = input("Ingrese el nombre del doctor que atenderá al paciente: ")
#         treatingDoctor = AdministrativePersonal.validateDoctor(hospital, doctor)
#         date = input("Ingrese la fecha de la cita (dd/mm/yyyy):\n")
#         AdministrativePersonal.generateAppointment(hospital, patient, treatingDoctor, date)
#     except Exception as error:
#         print(str(error))
#
#
# def getClinicalHistoryData(hospital, doctorDocument):
#     try:
#         patientDocument = input("Ingrese el documento del paciente:\n")
#         date = datetime.date.today().strftime("%d/%m/%Y")
#         consultReason = input("Ingrese el motivo de la consulta:\n")
#         symptomatology = input("Ingrese la sintomatologia:\n")
#         diagnosis = input("Ingrese el diagnostico:\n")
#         medicine = input("Ingrese el nombre del medicamento (N/A si no aplica):\n")
#         if medicine == "":
#             medicine = "N/A"
#         procedure = input("Ingrese el nombre del procedimiento (N/A si no aplica):\n")
#         if procedure == "":
#             procedure = "N/A"
#         helpDiagnostic = input("Ingrese el diagnostico de ayuda (N/A si no aplica):\n")
#         if helpDiagnostic == "":
#             helpDiagnostic = "N/A"
#         Doctor.generateHistory(hospital, patientDocument, doctorDocument, procedure, medicine, helpDiagnostic, date,
#                                consultReason, symptomatology, diagnosis)
#     except Exception as error:
#         print(str(error))
#
#
# def getAllPatientData(hospital):
#     try:
#         patientDocument = input("Ingrese el documento del paciente:\n")
#         while True:
#             print("¿Qué información deseas ver?")
#             attribute = input("1. Datos personales \n2. Historia clínica\n3. Visitas Clinicas\n4. Regresar\n")
#             if attribute not in ["1", "2", "3", "4"]:
#                 print("Opción inválida")
#                 continue
#             if attribute == "4":
#                 break
#             if attribute == "1":
#                 Doctor.getPersonalPatientInfo(hospital, patientDocument)
#             if attribute == "2":
#                 Doctor.getPersonalClinicalHistory(hospital, patientDocument)
#             if attribute == "3":
#                 visit = Doctor.getPersonalVisits(hospital, patientDocument)
#                 Nurse.print_all(visit)
#     except Exception as error:
#         print(str(error))
#
#
# def getVitalData(hospital):
#     try:
#         patientDocument = input("Ingrese el documento del paciente:\n")
#         arterialPressure = input("Ingrese la presión arterial:\n")
#         temperature = input("Ingrese la temperatura:\n")
#         pulse = input("Ingrese el pulso:\n")
#         oxygenBloodLevel = input("Ingrese el nivel de oxígeno en la sangre:\n")
#         medication = input("Ingrese el nombre del medicamento aplicado:\n")
#         if medication == "":
#             medication = "N/A"
#         procedure = input("Ingrese el nombre del procedimiento aplicado:\n")
#         if procedure == "":
#             procedure = "N/A"
#         Nurse.registerVitalDataForPatient(hospital, patientDocument, arterialPressure, temperature, pulse,
#                                           oxygenBloodLevel, medication, procedure)
#     except Exception as error:
#         print(str(error))
#
#
# def getInvoiceData(hospital, document):
#     try:
#         patient = AdministrativePersonal.validatePatientId(hospital, document)
#         if patient == None:
#             raise Exception("El paciente no existe")
#         appointment = Doctor.getAppointmentsByPatient(hospital, document)
#         AdministrativePersonal.generateInvoice(hospital, patient, appointment)
#     except Exception as error:
#         print(str(error))
#
#
# def menuUpdateContactEmergency(hospital, userToUpdate):
#     validContactEmergencyData(hospital, userToUpdate)
#
#
# def menuUpdateInsurance(hospital, userToUpdate):
#     validMedicalInsuranceData(hospital, userToUpdate)
