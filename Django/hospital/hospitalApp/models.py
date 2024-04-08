from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fullName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    bornDate = models.DateField()
    address = models.CharField(max_length=200)
    rol = models.CharField(max_length=30)
    userName = models.CharField(max_length=80)
    password = models.CharField(max_length=128)


class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    dosage = models.FloatField()


class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Patient(models.Model):
    idDocument = models.BigIntegerField(primary_key=True)
    fullName = models.CharField(max_length=255)
    bornDate = models.DateField()
    genre = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField()


class EmergencyContact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    fullName = models.CharField(max_length=255)
    relationship = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)


class MedicalInsurance(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    nameOfInsuranceCompany = models.CharField(max_length=255)
    policyNumber = models.BigIntegerField()
    policyState = models.BooleanField()
    policyValidity = models.DateField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    idDoctor = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')
    creationDate = models.DateField()


class ClinicalHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    idDoctor = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    consultReason = models.CharField(max_length=255)
    symptomatology = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    date = models.DateField()


class VitalData(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    arterialPressure = models.FloatField()
    temperature = models.FloatField()
    pulse = models.IntegerField()
    bloodOxygenLevel = models.FloatField()


class MedicalAppointment(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient')
    idDoctor = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor')
    date = models.DateField()


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    idMedicalAppointment = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE, to_field='id', db_column='idMedicalAppointment')


class OrderMedication(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    idMedication = models.ForeignKey(Medication, on_delete=models.CASCADE, to_field='id',   db_column='idMedication')
    dose = models.FloatField()
    treatmentDuration = models.CharField(max_length=100)
    amount = models.FloatField()
    item = models.IntegerField()


class OrderProcedure(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    idProcedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, to_field='id', db_column='idProcedure')
    amount = models.FloatField()
    frequency = models.CharField(max_length=100)
    item = models.IntegerField()


class OrderProcedureAssistance(models.Model):
    id = models.AutoField(primary_key=True)
    idOrderProcedure = models.ForeignKey(OrderProcedure, on_delete=models.CASCADE, to_field='id', db_column='idOrderProcedure')
    idSpecialist = models.CharField(max_length=255)


class OrderHelpDiagnostic(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder')
    nameHelpDiagnostic = models.CharField(max_length=255)
    quantity = models.FloatField()
    amount = models.FloatField()
    item = models.IntegerField()

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
