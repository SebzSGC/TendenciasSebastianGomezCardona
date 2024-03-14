import validator.typeValidator as typeValidator
from service.RolService.AdministrativePersonal import validatePatientId, validDoctorId, getMedicine, getProcedure
import model.Order as Order

def printDictItem(item, indent):
    indentation = "  " * indent
    for key, value in item.items():
        if isinstance(value, dict):
            print(f"{indentation}{key}:")
            printDictItem(value, indent + 1)
        elif isinstance(value, list):
            print(f"{indentation}{key}:")
            printListItems(value, indent + 1)
        else:
            print(f"{indentation}{key}: {value}")

def printListItems(items, indent):
    indentation = "  " * indent
    for idx, item in enumerate(items):
        print(f"{indentation}Item {idx + 1}:")
        printDictItem(item, indent + 1)

def printClinicalHistory(history):
    printDictItem(history, 0)

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
    if patient is None:
        raise Exception("El paciente no existe")
    if hospital.patientVisits == []:
        raise Exception("El paciente no tiene visitas registradas")
    print("Fechas disponibles:")
    for visit in hospital.patientVisits:
        print(visit.date)
    chosenDate = input("Por favor, ingrese una fecha con la hora para visualizar:\n")
    for visit in hospital.patientVisits:
        if chosenDate == visit.date:
            return visit
    else:
        print("La fecha seleccionada no está disponible. Por favor, elija una fecha con la hora válida.")

def getAppointmentsByPatient(hospital, patientDocument):
    patient = validatePatientId(hospital, patientDocument)
    if patient is None:
        raise Exception("El paciente no existe")
    if hospital.appointments == []:
        raise Exception("El paciente no tiene citas para poder generar la factura")
    print("Fechas de citas disponibles para asociar la factura:")
    for dateAppointment in hospital.appointments:
        if dateAppointment.idPatient == patientDocument:
            print(dateAppointment.date)
    chosenDate = input("Por favor, ingrese una fecha:\n")
    for appointment in hospital.clinicalHistories[patientDocument]:
        if chosenDate == appointment:
            return hospital.clinicalHistories[patientDocument][chosenDate]
    else:
        raise Exception("La fecha seleccionada no coincide con la cita correcta. Por favor, elija una fecha válida o valide los datos.")   

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
            handleMedication(actualOrder, medicine, hospital)
        elif helpDiagnostic == "N/A" and medicine == "N/A" and procedure != "N/A":
            handleProcedure(actualOrder, procedure, hospital)
        elif procedure != "N/A" and medicine != "N/A" and helpDiagnostic == "N/A":
            handleMedication(actualOrder, medicine, hospital)
            handleProcedure(actualOrder, procedure, hospital)
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

def handleMedication(actualOrder, medicine, hospital):
    while True:
        item = len(actualOrder.orderMedications) + 1
        idMedicine = medicine.id
        dose = input("Ingrese la dosis del medicamento:\n")
        treatmentDuration = input("Ingrese la duración del tratamiento:\n")
        amount = medicine.price
        actualMedication = Order.OrderMedication(actualOrder.id, idMedicine, dose, treatmentDuration, amount, item)
        actualOrder.orderMedications.append(actualMedication)
        print(f"La orden #{actualOrder.id} del paciente se le ha asignado el medicamento {medicine.name} y sus respectivos datos con exito")
        if input("Desea agregar otro medicamento? (si/no)\n").lower() == "no":
            break
        medicine = input("Ingrese el nombre del medicamento:\n")
        medicine = getMedicine(hospital, medicine)
        if medicine is None:
            print("El medicamento no existe")
            break

def handleProcedure(actualOrder, procedure, hospital):
    while True:
        item = len(actualOrder.orderProcedures) + 1
        idProcedure = procedure.id
        amount = input("Ingrese la cantidad del procedimiento:\n")
        frequency = input("Ingrese la frecuencia del procedimiento:\n")
        specialAssistance = input("Requiere de asistencia por especialista:\n").lower() == "si"
        idSpecialist = input("Ingrese el id del especialista:\n") if specialAssistance else None
        actualProcedure = Order.OrderProcedure(actualOrder.id, idProcedure, amount, frequency, specialAssistance, idSpecialist, item)
        actualOrder.orderProcedures.append(actualProcedure)
        print(f"La orden #{actualOrder.id} del paciente se le ha asignado el procedimiento {procedure.name} y sus respectivos datos con exito")
        if input("Desea agregar otro procedimiento? (si/no)\n").lower() == "no":
            break
        procedure = input("Ingrese el nombre del procedimiento:\n")
        procedure = getProcedure(hospital, procedure)
        if procedure is None:
            print("El procedimiento no existe")
            break
        
def setOrderDetails(hospital, newClinicalHistory):
    order = newClinicalHistory["order"]
    if order["orderMedications"]:
        for index, medicationOrder in enumerate(order["orderMedications"]):
            order["orderMedications"][index] = (vars(medicationOrder)) 
    if order["orderProcedures"]:
        for index, procedureOrder in enumerate(order["orderProcedures"]):
            order["orderProcedures"][index] = (vars(procedureOrder))
    if order["orderHelpDiagnostics"]:
        for index, diagnosticOrder in enumerate(order["orderHelpDiagnostics"]):
            order["orderHelpDiagnostics"][index] = (vars(diagnosticOrder)) 
    hospital.orders.append(order)