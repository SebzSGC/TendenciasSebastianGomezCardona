def searchPatient(hospital,fullName):
    for patient in hospital.patients:
        if patient.fullName==fullName:
            print("Paciente encontrado")
            return patient
    return None

def searchEmployee(hospital,userName):
    for employee in hospital.employees:
        if employee.userName==userName:
            print("Empleado encontrado")
            return employee
    return None