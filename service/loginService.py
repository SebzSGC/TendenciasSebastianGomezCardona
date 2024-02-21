def searchPatient(hospital,userName):
    for patient in hospital.patients:
        if patient.fullName==userName:
            return patient
    return None

def searchEmployee(hospital,userName):
    for employee in hospital.employees:
        if employee.userName==userName:
            return employee
    return None