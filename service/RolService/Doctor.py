import datetime
from hmac import new
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
    for medication in hospital.stockMedicine:
        if medication.name == medicine:
            return medication
    return None

def getProcedure(hospital, procedure):
    for procedure in hospital.procedures:
        if procedure.name == procedure:
            return procedure
    return None

def getAppointmentByDate(hospital):
    date = input("Ingrese la fecha de la cita (dd/mm/yyyy):\n")
    if date not in hospital.appointments:
        raise Exception("No hay citas programadas para esta fecha")
    for appointment in hospital.appointments:
        if hospital.appointments.date == date:
            return appointment
    raise Exception("No hay citas programadas para esta fecha")

def getAllPatientInfo():
    pass

def generateHistory(hospital,patientDocument,doctorDocument, procedure, medicine, helpDiagnostic, date, consultReason, symptomatology, diagnosis):
    patient = validatePatientId(hospital, patientDocument)
    validMedicine = getMedicine(hospital, medicine)
    validProcedure = getProcedure(hospital, procedure)
    if patient is None or patient not in hospital.patients:
        raise Exception("El documento del paciente no es valido o no existe")
    doc = validDoctorId(hospital, doctorDocument)
    if doc is None or doc not in hospital.employees:
        raise Exception("El documento del doctor no es valido o no existe")
    if typeValidator.validDate(date) == ValueError:
        raise Exception(str(ValueError))
    if validMedicine is not None and medicine != "N/A":
        medicine = validMedicine
    else:
        medicine = "N/A"
    if validProcedure is not None and procedure != "N/A":
        procedure = validProcedure
    else:
        procedure = "N/A"
    
    newClinicalHistory = {}
    newClinicalHistory["Date"] = date
    newClinicalHistory["DoctorDocument"] = doctorDocument
    newClinicalHistory["consultReason"] = consultReason
    newClinicalHistory["symptomatology"] = symptomatology
    newClinicalHistory["diagnosis"] = diagnosis
    newClinicalHistory["order"] = None

    if procedure == "N/A" and medicine == "N/A" and helpDiagnostic == "N/A":
        print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
        hospital.clinicalHistories[str(patientDocument)][date] = newClinicalHistory
        return
    idOrder = len(hospital.orders) + 1
    actualOrder = Order.Order(idOrder, patientDocument, doctorDocument, date)

    if helpDiagnostic != "N/A" and procedure == "N/A" and medicine == "N/A":
        idOrder = actualOrder.id
        nameHelpDiagnostic = input("Ingrese el nombre del diagnostico de ayuda:\n")
        quantity = input("Ingrese la cantidad:\n")
        amount = input("Ingrese el valor:\n")
        specialAssistance = input("Requiere de asistencia por especialista:\n")
        if specialAssistance.lower == "si":
            specialAssistance = True
            idSpecialist = input("Ingrese el id del especialista:\n")
        else:
            idSpecialist = None
            specialAssistance = False
        actualDiagnostic =  Order.OrderHelpDiagnostic(idOrder, nameHelpDiagnostic, quantity, amount, specialAssistance, idSpecialist)
        actualOrder.orderHelpDiagnostics.append(actualDiagnostic)
        print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
        print(f"Ayuda diagnostica agregada a la orden #{actualOrder.id}")
    
    if helpDiagnostic == "N/A" and medicine != "N/A":
        idMedicine = medicine.id
        dose = input("Ingrese la dosis:\n")
        treatmentDuration = input("Ingrese la duración del tratamiento:\n")
        amount = input("Ingrese la cantidad:\n")
        frequency = input("Ingrese la frecuencia:\n")
        specialAssistance = input("Requiere de asistencia por especialista:\n")
        if specialAssistance.lower == "si":
            specialAssistance = True
            idSpecialist = input("Ingrese el id del especialista:\n")
        else:
            idSpecialist = None
            specialAssistance = False
        actualMedication = Order.OrderMedication(idOrder, idMedicine, dose, treatmentDuration, amount)
        actualOrder.orderMedications.append(actualMedication)
        print(f"La orden #{idOrder} del paciente se le ha asignado el medicamento {medicine.name} y sus respectivos datos con exito")

    if helpDiagnostic == "N/A" and procedure != "N/A":
        idProcedure = procedure.id
        amount = input("Ingrese la cantidad:\n")
        frequency = input("Ingrese la frecuencia:\n")
        specialAssistance = input("Requiere de asistencia por especialista:\n")
        if specialAssistance.lower == "si":
            specialAssistance = True
            idSpecialist = input("Ingrese el id del especialista:\n")
        else:
            idSpecialist = None
            specialAssistance = False
        actualProcedure = Order.OrderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist)
        actualOrder.orderProcedures.append(actualProcedure)
        print(f"La orden #{idOrder} del paciente se le ha asignado el procedimiento {procedure.name} y sus respectivos datos con exito")

    newClinicalHistory["order"] = vars(actualOrder)
    if newClinicalHistory["order"]["orderMedications"] != []:
        for medicantionOrder in newClinicalHistory["order"]["orderMedications"]:
            newClinicalHistory["order"]["orderMedications"] = vars(medicantionOrder)
    if newClinicalHistory["order"]["orderProcedures"] != []:
        for procedureOrder in newClinicalHistory["order"]["orderProcedures"]:
             newClinicalHistory["order"]["orderProcedures"] = vars(procedureOrder)
    if newClinicalHistory["order"]["orderHelpDiagnostics"] != []:
        for diagnosticOrder in newClinicalHistory["order"]["orderHelpDiagnostics"]:
            newClinicalHistory["order"]["orderHelpDiagnostics"] = vars(diagnosticOrder)
    hospital.clinicalHistories[str(patientDocument)][date] = newClinicalHistory
    print(f"La historia clinica del paciente {patientDocument} ha sido generada con exito")
    clinicalHistory = hospital.clinicalHistories[str(patientDocument)][date]
    printClinicalHistory(clinicalHistory)