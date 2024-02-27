def searchPatient(hospital,fullName):
    for patient in hospital.patients:
        if patient.fullName==fullName:
            return patient
    return None

def searchEmployee(hospital,userName):
    for employee in hospital.employees:
        if employee.userName==userName:
            return employee
    return None