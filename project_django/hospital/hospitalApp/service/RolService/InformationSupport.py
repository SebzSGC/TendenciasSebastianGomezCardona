from hospitalApp import models


def updateProcedures(id: int, name: str, description: str):
    models.Procedure.objects.filter(id=id).update(name=name, description=description)


def updateDrugInventory(id: int, name: str, price: float, dosage: float):
    models.Medication.objects.filter(id=id).update(price=price, dosage=dosage, name=name)


def registerDrugInventory(name: str, price: float, dosage: float):
    models.Medication.objects.create(name=name, price=price, dosage=dosage)


def registerProcedures(name: str, description: str):
    models.Procedure.objects.create(name=name, description=description)


def deleteProcedure(id: int):
    models.Procedure.objects.filter(id=id).delete()


def deleteDrug(id: int):
    models.Medication.objects.filter(id=id).delete()
