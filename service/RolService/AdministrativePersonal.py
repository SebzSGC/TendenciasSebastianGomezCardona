import model.User as User
from validator import typeValidator
from model.Invoice import Invoice
from model.MedicalAppointment import MedicalAppointment


def validatePatientId(hospital, id):
    if hospital.patients == []:
        return None
    for patient in hospital.patients:
        if patient.id == id:
            return patient
    return None
    
def validateDoctor(hospital, name):
    if hospital.employees == []:
        return None
    for doctor in hospital.employees:
        if doctor.fullName == name and doctor.rol == "Doctor":
            return doctor
    return None

def getMedicine(hospital, medicine):
    if medicine is None or medicine == "N/A":
        return None
    for medication in hospital.stockMedicine:
        if medication.name == medicine:
            return medication
    return None

def getProcedure(hospital, procedure):
    if procedure is None or procedure == "N/A":
        return None
    for procedures in hospital.procedures:
        if procedures.name == procedure:
            return procedures
    return None

def getMedicineById(hospital, medicineById):
    if medicineById is None or medicineById == "N/A":
        return None
    for medication in hospital.stockMedicine:
        if medication.id == medicineById:
            return medication
    return None

def getProcedureById(hospital, procedureById):
    if procedureById is None or procedureById == "N/A":
        return None
    for procedures in hospital.procedures:
        if procedures.id == procedureById:
            return procedures
    return None

def validDoctorId(hospital, id):
    if hospital.employees == []:
        return None
    for doctor in hospital.employees:
        if doctor.idNumber == id and doctor.rol == "Doctor":
            return doctor
    return None

def createPatient(hospital, id, fullName, bornDate, genre, address, phoneNumber, email):
    patient = validatePatientId(hospital, id)
    typeValidator.validEmail(email)
    typeValidator.validPhoneNumber(phoneNumber)
    typeValidator.validDateAndAge(bornDate)
    if patient:
        raise Exception("ya existe un paciente con esa cedula registrada")
    patient = User.Patient(id, fullName, bornDate, genre, address, phoneNumber, email)
    hospital.clinicalHistories[str(id)] = {} 
    hospital.patients.append(patient)

def allDataCompletePatient(hospital, patient):
    patient = validatePatientId(hospital, patient.id)
    if not patient:
        raise Exception("Ocurrio un error al crear el paciente, intente de nuevo")
    for item in hospital.patients:
        if item.id == patient.id:
            item = patient
    print(f"Paciente: {patient.fullName} creado con éxito")

def createEmergencyContact(hospital, idUser, name, relationship, phoneNumber):
    patient = validatePatientId(hospital, idUser)
    if not patient:
        raise Exception("El paciente no existe")
    contact = User.EmergencyContact(idUser, name, relationship, phoneNumber)
    patient.emergencyContact = contact

def createMedicalInsurance(hospital, idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity):
    patient = validatePatientId(hospital, idUser)
    if not patient:
        raise Exception("El paciente no existe")
    insurance = User.MedicalInsurance(idUser, nameOfInsuranceCompany, policyNumber, policyState, policyValidity)
    patient.medicalInsurance = insurance

def updatePatient(patient, attribute, newInfo, oldAttribute):
    setattr(patient, attribute, newInfo)
    print(f"Informacion del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def updateEmergencyContact(hospital, contact, attribute, newInfo, oldAttribute):
    contact = validatePatientId(hospital, contact.idUser)
    if not contact:
        raise Exception("El contacto de emergencia no esta asociado a un paciente")
    setattr(contact, attribute, newInfo)
    print(f"Informacion de contacto del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def updateMedicalInsurance(hospital, insurance, attribute, newInfo, oldAttribute):
    insurance = validatePatientId(hospital, insurance.idUser)
    if not insurance:
        raise Exception("La poliza no esta asociada a un paciente")
    setattr(insurance, attribute, newInfo)
    print(f"Informacion de la poliza del paciente: {oldAttribute} cambiado por {newInfo}, actualizacion con éxito")

def generateAppointment(hospital, patient, doctor, date):
    if patient == None:
        raise Exception("El paciente no existe")
    if doctor == None:
        raise Exception("El doctor no existe")
    date = typeValidator.validDate(date)
    appointment = MedicalAppointment(patient.id, doctor.idNumber, date)
    hospital.appointments.append(appointment)
    print(f"Cita programada para el paciente: {patient.fullName}, el dia {date} con el doctor: {doctor.fullName}")

def generateInvoice(hospital, patient, appointment):
    totalToPay = 0
    idDoctor = appointment["DoctorDocument"]
    invoice = Invoice(appointment, patient)
    doctor = validDoctorId(hospital, idDoctor)
    print(f"Factura generada para el paciente: {patient.fullName}, con la cita: {appointment["Date"]}")
    print("Nombre del paciente: ",invoice.patient.fullName)
    print("Edad del paciente: ", typeValidator.getCorrectAge(invoice.patient.bornDate))
    print("Cedula del paciente", invoice.patient.id)
    print("Nombre del doctor: ", doctor.fullName)
    print("Nombre de la compañia de seguro del paciente: ", invoice.patient.medicalInsurance.nameOfInsuranceCompany)
    print("Numero de poliza del paciente: ", invoice.patient.medicalInsurance.policyNumber)
    print("Dias de vigencia de la poliza: ", typeValidator.getValidityPolicy(invoice.patient.medicalInsurance.policyValidity))
    print("Fecha de la finalizacion de la poliza: ", invoice.patient.medicalInsurance.policyValidity)
    if invoice.medicalAppointment["order"]["orderMedications"]:
        print("Medicamentos: ")
        for medication in invoice.medicalAppointment["order"]["orderMedications"]:
            if medication == "idMedication":
                infoMedicine = getMedicineById(hospital, invoice.medicalAppointment["order"]["orderMedications"]["item"])
                print(" item: ", invoice.medicalAppointment["order"]["orderMedications"]["item"])
                print("     Medicamento: ", infoMedicine.name)
                print("     Cantidad: ", infoMedicine.dosage)
                print("     Precio: ", infoMedicine.price)
                totalToPay += infoMedicine.price
            continue    
    else:
        print("No se recetaron medicamentos")

    if invoice.medicalAppointment["order"]["orderProcedures"]:
        print("Procedimientos: ")
        for procedure in invoice.medicalAppointment["order"]["orderProcedures"]:
            if procedure == "idProcedure":
                infoProcedure = getProcedureById(hospital, invoice.medicalAppointment["order"]["orderProcedures"]["item"])
                print(" item: ", invoice.medicalAppointment["order"]["orderProcedures"]["item"])
                print("     Procedimiento: ", infoProcedure.name)
                print("     Descripcion: ", infoProcedure.description)
            continue
    else:
        print("No se programaron procedimientos")

    if invoice.patient.medicalInsurance.policyState == True:
        print("El paciente cuenta con seguro medico")
        print("Copago de: $", 50000)
        print("Precio por medicamentos: ", totalToPay)
        print("Total a pagar: ", 50000)
    else:    
        print("El paciente no cuenta con seguro medico")
        print("Precio por medicamentos: ", totalToPay)
        print("Total a pagar: ", totalToPay)