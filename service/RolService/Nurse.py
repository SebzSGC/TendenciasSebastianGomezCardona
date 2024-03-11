import datetime
from model.User import VitalData
from model.ClinicalVisit import ClinicalVisit
from service.RolService.AdministrativePersonal import validatePatientId
from service.RolService.Doctor import getMedicine, getProcedure

def getOrdersByIdPatient(hospital, idPatient):
    orders = hospital.orders
    filteredOrders = []
    filteredOrders = [dictionary for dictionary in orders if dictionary.get("idPatient") == idPatient]
    return filteredOrders

def getOrdersMedication(medication, orders):
    if medication is None:
        return None
    order = []
    for actualOrder in orders:
        if actualOrder.get("orderMedications") == []:
            continue
        orderMedications = actualOrder.get("orderMedications", [])  
        if orderMedications["idMedication"] == medication.id:
            order.append(orderMedications)
    if order == []: 
        raise Exception("El procedimiento no existe en ninguna orden")
    return order

def getOrdersProcedures(procedure, orders):
    if procedure is None:
        return None
    order = []
    for actualOrder in orders:
        if actualOrder.get("orderProcedures") == []:
            continue
        orderProcedures = actualOrder.get("orderProcedures", [])  # Obtener el vector de orderMedications para el elemento actual
        if orderProcedures["idProcedure"] == procedure.id:
            order.append(orderProcedures)
    if order == []: 
        raise Exception("El procedimiento no existe en ninguna orden")
    return order

 
def registerVitalDataForPatient(hospital,idUser,arterialPressure,temperature,pulse,bloodOxygenLevel, medication, procedure):
    if validatePatientId(hospital, idUser) == None:
        raise Exception("El paciente no existe")
    
    medication = getMedicine(hospital, medication)
    procedure = getProcedure(hospital, procedure)
    
    orders = getOrdersByIdPatient(hospital, idUser)
    orderMedication = None
    orderProcedure = None
    if orders != [] and medication is not None:                
        orderMedication = getOrdersMedication(medication, orders)
    if orders != [] and procedure is not None:
        orderProcedure = getOrdersProcedures(procedure, orders)
    if orderMedication is None:
        orderMedication = "N/A"
    if orderProcedure is None:
        orderProcedure = "N/A"
    vitalData = VitalData(idUser,arterialPressure,temperature,pulse,bloodOxygenLevel)
    date = datetime.date.today().strftime("%d/%m/%Y")
    clinicalVisit = ClinicalVisit(idUser, date, vitalData)

    print("IDs de ordenes que contienen el medicamento administrado:")
    clinicalVisit.medication = selectDictionaryByOrderId(orderMedication)
    print("IDs de ordenes que contienen el procedimiento realizado:")
    clinicalVisit.procedure = selectDictionaryByOrderId(orderProcedure)
    hospital.patientVisits.append(clinicalVisit)

def selectDictionaryByOrderId(vectors):
    if vectors is None or vectors == [] or vectors == "N/A":
        return "N/A"
    id_positions = {vector["idOrder"]: idx for idx, vector in enumerate(vectors)}
    for id_order in id_positions.keys():
        print(f"Orden #{id_order} = {id_order}")
    selected_id = input("Ingrese el ID de la orden que desea seleccionar: ")
    selected_position = id_positions.get(selected_id)
    if selected_position is not None:
        return vectors[selected_position]
    else:
        return None

def print_all(clinicalVisit):
    print("Datos vitales:")
    print(" Documento del paciente: ",clinicalVisit.vitalData.idUser)
    print(" Presion arterial: ",clinicalVisit.vitalData.arterialPressure)
    print(" Temperatura: ",clinicalVisit.vitalData.temperature)
    print(" Pulso: ",clinicalVisit.vitalData.pulse)
    print(" Nivel de oxigeno en la sangre: ",clinicalVisit.vitalData.bloodOxygenLevel)
    print("Medicina administrada:")
    if clinicalVisit.medication != "N/A":
        printMedicines(clinicalVisit.medication)
    else:
        print(clinicalVisit.medication)
    print("Procedimientos:")
    if clinicalVisit.procedure != "N/A":
        printProcedures(clinicalVisit.procedure)
    else:
        print(clinicalVisit.procedure)

def printMedicines(medication):
        for key, value in medication.items():
             print(f" {key}: {value}")

def printProcedures(procedures):
        for key, value in procedures.items():
            print(f" {key}: {value}")