from django.db import models


# Create your models here.

class Employee(models.Model):
    id: int = models.BigIntegerField(primary_key=True)
    fullName: str = models.CharField(max_length=255)
    email: str = models.EmailField()
    phoneNumber: str = models.CharField(max_length=20)
    bornDate: str = models.CharField(max_length=80)
    address: str = models.CharField(max_length=200)
    rol: str = models.CharField(max_length=30)
    userName: str = models.CharField(max_length=80)
    password: str = models.CharField(max_length=128)


class Medication(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    price: float = models.FloatField()
    dosage: float = models.FloatField()


class Procedure(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=255)


class Patient(models.Model):
    idDocument: int = models.BigIntegerField(primary_key=True)
    fullName: str = models.CharField(max_length=255)
    bornDate: str = models.CharField(max_length=80)
    genre: str = models.CharField(max_length=50)
    address: str = models.CharField(max_length=255)
    phoneNumber: str = models.CharField(max_length=20)
    email: str = models.EmailField()


class EmergencyContact(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient')
    fullName: str = models.CharField(max_length=255)
    relationship: str = models.CharField(max_length=20)
    phoneNumber: str = models.CharField(max_length=20)


class MedicalInsurance(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient')
    nameOfInsuranceCompany: str = models.CharField(max_length=255)
    policyNumber: int = models.BigIntegerField()
    policyState: bool = models.BooleanField()
    policyValidity: str = models.CharField(max_length=80)


class Order(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient')
    idDoctor: int = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')


class ClinicalHistory(models.Model):
    id: int = models.BigIntegerField(primary_key=True)
    idPatient: Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                           db_column='idPatient')
    idDoctor: Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')
    idOrder: Order = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    consultReason: str = models.CharField(max_length=255)
    symptomatology: str = models.CharField(max_length=255)
    diagnosis: str = models.CharField(max_length=255)
    date: str = models.CharField(max_length=80)


class VitalData(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient')
    arterialPressure: float = models.FloatField()
    temperature: float = models.FloatField()
    pulse: int = models.IntegerField()
    bloodOxygenLevel: float = models.FloatField()


class MedicalAppointment(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient')
    idDoctor: int = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')
    date: str = models.CharField(max_length=80)


class Invoice(models.Model):
    id: int = models.AutoField(primary_key=True)
    idMedicalAppointment: int = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE,
                                                  to_field='id', db_column='idMedicalAppointment')


class OrderMedication(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    idMedication: int = models.ForeignKey(Medication, on_delete=models.CASCADE, to_field='id',
                                          db_column='idMedication')
    dose: float = models.FloatField()
    treatmentDuration: str = models.CharField(max_length=100)
    amount: float = models.FloatField()
    item: int = models.IntegerField()


class OrderProcedure(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    idProcedure: int = models.ForeignKey(Procedure, on_delete=models.CASCADE, to_field='id',
                                         db_column='idProcedure')
    amount: float = models.FloatField()
    frequency: str = models.CharField(max_length=100)
    item: int = models.IntegerField()


class OrderProcedureAssistance(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrderProcedure: int = models.ForeignKey(OrderProcedure, on_delete=models.CASCADE, to_field='id',
                                              db_column='idOrderProcedure')
    idSpecialist: str = models.CharField(max_length=255)


class OrderHelpDiagnostic(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    nameHelpDiagnostic: str = models.CharField(max_length=255)
    quantity: float = models.FloatField()
    amount: float = models.FloatField()
    item: int = models.IntegerField()

# Create your mongomodels here.


# class ClinicalVisit(mongomodels.Model):
#     id = models.BigIntegerField(primary_key=True)
#     idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date = models.CharField(max_length=30)
#     medication = []
#     procedure = []
#     vitalData = models.ForeignKey(VitalData, on_delete=models.CASCADE)

# class Hospital(mongomodels.Model):
#     patients=[]
#     employees=[]
#     appointments=[]
#     clinicalHistories={}
#     stockMedicine=[]
#     procedures=[]
#     orders=[]
#     patientVisits=[]
