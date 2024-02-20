def searchPatient(hospital,userName):
    for person in hospital.patients:
        if person.userName==userName:
            return person
    return None

def searchEmployee(hospital,userName):
    for person in hospital.employees:
        if person.userName==userName:
            return person
    return None