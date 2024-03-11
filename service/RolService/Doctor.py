import datetime
from model.Medication import Medication
import validator.typeValidator as typeValidator
from service.RolService.AdministrativePersonal import validatePatientId, validDoctorId
import model.Order as Order

def printClinicalHistory(history, indent=0):
    for key, value in history.items():
        if isinstance(value, dict):
            print("  " * indent + f"{key}:")
            printClinicalHistory(value, indent + 1)
        elif isinstance(value, list):
            print("  " * indent + f"{key}:")
            for item in value:
                printClinicalHistory(item, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")

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

def getAppointmentByDate(hospital):
    date = input("Ingrese la fecha de la cita (dd/mm/yyyy):\n")
    if date not in hospital.appointments:
        raise Exception("No hay citas programadas para esta fecha")
    for appointment in hospital.appointments:
        if hospital.appointments.date == date:
            return appointment
    raise Exception("No hay citas programadas para esta fecha")

def getPersonalPatientInfo(hospital, patientDocument):
    patient = validatePatientId(hospital, patientDocument)
    if not patient:
        raise Exception("El paciente no existe")
    print(f"Nombre: {patient.fullName}")
    print(f"Documento: {patient.id}")
    print(f"Fecha de nacimiento: {patient.bornDate}")
    print(f"Genero: {patient.genre}")
    print(f"Dirección: {patient.address}")
    print(f"Telefono: {patient.phoneNumber}")
    print(f"Correo: {patient.email}")
    if patient.emergencyContact:
        print(f"Contacto de emergencia: {patient.emergencyContact.name}")
        print(f"Relación: {patient.emergencyContact.relationship}")
        print(f"Telefono: {patient.emergencyContact.phoneNumber}")
    if patient.medicalInsurance:
        print(f"Seguro médico: {patient.medicalInsurance.nameOfInsuranceCompany}")
        print(f"Numero de poliza: {patient.medicalInsurance.policyNumber}")
        print(f"Estado de la poliza: {patient.medicalInsurance.policyState}")
        print(f"Vigencia de la poliza: {patient.medicalInsurance.policyValidity}")

def getPersonalClinicalHistory(hospital, patientDocument):
    patient = validatePatientId(hospital, patientDocument)
    if not patient:
        raise Exception("El paciente no existe")
    if not hospital.clinicalHistories[patientDocument]:
        print("El paciente no tiene historias clinicas registradas")
        return
    print("Fechas disponibles:")
    for date in hospital.clinicalHistories[patientDocument].keys():
        print(date)
    chosenDate = input("Por favor, ingrese una fecha para visualizar:\n")
    if chosenDate not in hospital.clinicalHistories[patientDocument]:
        print("La fecha seleccionada no está disponible. Por favor, elija una fecha válida.")
    else:
        history = hospital.clinicalHistories[patientDocument][chosenDate]
        printClinicalHistory(history)

def getPersonalVisits(hospital, patientDocument):
    patient = validatePatientId(hospital, patientDocument)
    if not patient:
        raise Exception("El paciente no existe")
    if hospital.patientVisits == []:
        print("El paciente no tiene visitas registradas")
    print("Fechas disponibles:")
    for visit in hospital.patientVisits:
        print(visit.date)
    chosenDate = input("Por favor, ingrese una fecha para visualizar:\n")
    for visit in hospital.patientVisits:
        if chosenDate == visit.date:
            return visit
    else:
        raise Exception("La fecha seleccionada no está disponible. Por favor, elija una fecha válida.")

def generateHistory(hospital, patientDocument, doctorDocument, procedure, medicine, helpDiagnostic, date, consultReason, symptomatology, diagnosis):
    patient = validatePatientId(hospital, patientDocument)
    doc = validDoctorId(hospital, doctorDocument)
    
    if not (patient and doc):
        raise Exception("El documento del paciente o del doctor no es valido o no existe")

    try:
        typeValidator.validDate(date)
    except ValueError as e:
        raise Exception(str(e))

    medicine = getMedicine(hospital, medicine) if medicine != "N/A" else "N/A"
    procedure = getProcedure(hospital, procedure) if procedure != "N/A" else "N/A"

    # Create clinical history
    newClinicalHistory = {
        "Date": date,
        "DoctorDocument": doctorDocument,
        "consultReason": consultReason,
        "symptomatology": symptomatology,
        "diagnosis": diagnosis,
        "order": None
    }

    if procedure is None and medicine is None and helpDiagnostic == "N/A":
        print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
    else:
        idOrder = len(hospital.orders) + 1
        actualOrder = Order.Order(idOrder, patientDocument, doctorDocument, date)

        if helpDiagnostic != "N/A" and procedure == "N/A" and medicine == "N/A":
            handleDiagnostic(actualOrder)
        elif helpDiagnostic == "N/A" and procedure == "N/A" and medicine != "N/A":
            handleMedication(actualOrder, medicine)
        elif helpDiagnostic == "N/A" and medicine == "N/A" and procedure != "N/A":
            handleProcedure(actualOrder, procedure)
        elif procedure != "N/A" and medicine != "N/A" and helpDiagnostic == "N/A":
            handleMedication(actualOrder, medicine)
            handleProcedure(actualOrder, procedure)
        else:
            raise Exception("No se puede agregar una ayuda diagnostica si se esta asignando un procedimiento o medicamento")
        newClinicalHistory["order"] = vars(actualOrder)
        setOrderDetails(hospital, newClinicalHistory)

    hospital.clinicalHistories[str(patientDocument)][date] = newClinicalHistory
    print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")

def handleDiagnostic(actualOrder):
    nameHelpDiagnostic = input("Ingrese el nombre del diagnostico de ayuda:\n")
    quantity = input("Ingrese la cantidad:\n")
    amount = input("Ingrese el valor:\n")
    specialAssistance = input("Requiere de asistencia por especialista:\n").lower() == "si"
    idSpecialist = input("Ingrese el id del especialista:\n") if specialAssistance else None
    actualDiagnostic = Order.OrderHelpDiagnostic(actualOrder.id, nameHelpDiagnostic, quantity, amount, specialAssistance, idSpecialist)
    actualOrder.orderHelpDiagnostics.append(actualDiagnostic)
    print(f"La historia clinica del paciente {actualOrder.idPatient} ha sido generada con exito")
    print(f"Ayuda diagnostica agregada a la orden #{actualOrder.id}")

def handleMedication(actualOrder, medicine):
    idMedicine = medicine.id
    dose = input("Ingrese la dosis:\n")
    treatmentDuration = input("Ingrese la duración del tratamiento:\n")
    amount = input("Ingrese la cantidad:\n")
    actualMedication = Order.OrderMedication(actualOrder.id, idMedicine, dose, treatmentDuration, amount)
    actualOrder.orderMedications.append(actualMedication)
    print(f"La orden #{actualOrder.id} del paciente se le ha asignado el medicamento {medicine.name} y sus respectivos datos con exito")

def handleProcedure(actualOrder, procedure):
    idProcedure = procedure.id
    amount = input("Ingrese la cantidad:\n")
    frequency = input("Ingrese la frecuencia:\n")
    specialAssistance = input("Requiere de asistencia por especialista:\n").lower() == "si"
    idSpecialist = input("Ingrese el id del especialista:\n") if specialAssistance else None

    actualProcedure = Order.OrderProcedure(actualOrder.id, idProcedure, amount, frequency, specialAssistance, idSpecialist)
    actualOrder.orderProcedures.append(actualProcedure)
    print(f"La orden #{actualOrder.id} del paciente se le ha asignado el procedimiento {procedure.name} y sus respectivos datos con exito")

def setOrderDetails(hospital, newClinicalHistory):
    order = newClinicalHistory["order"]
    if order["orderMedications"]:
        for medicationOrder in order["orderMedications"]:
            order["orderMedications"] = vars(medicationOrder)
    if order["orderProcedures"]:
        for procedureOrder in order["orderProcedures"]:
            order["orderProcedures"] = vars(procedureOrder)
    if order["orderHelpDiagnostics"]:
        for diagnosticOrder in order["orderHelpDiagnostics"]:
            order["orderHelpDiagnostics"] = vars(diagnosticOrder)
    hospital.orders.append(order)