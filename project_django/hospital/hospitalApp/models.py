from django.db import models


# Create your models here.

class Employee(models.Model):
    id: int = models.AutoField(primary_key=True)
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
    idPatient: int = models.OneToOneField(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                          db_column='idPatient', related_name='emergencyContact')
    fullName: str = models.CharField(max_length=255)
    relationship: str = models.CharField(max_length=20)
    phoneNumber: str = models.CharField(max_length=20)


class MedicalInsurance(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.OneToOneField(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                          db_column='idPatient', related_name='medicalInsurance')
    nameOfInsuranceCompany: str = models.CharField(max_length=255)
    policyNumber: int = models.BigIntegerField()
    policyState: bool = models.BooleanField()
    policyValidity: str = models.CharField(max_length=80)


class ClinicalHistory(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                  db_column='idPatient', related_name='history_patient')
    idDoctor = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor',
                                 related_name='history_employee')
    consultReason = models.CharField(max_length=255)
    symptomatology = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    date = models.CharField(max_length=80)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    idClinicalHistory = models.ForeignKey(ClinicalHistory, on_delete=models.CASCADE, to_field='id',
                                          db_column='idClinicalHistory')


class VitalData(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient', related_name='vitalData_patient')
    arterialPressure: float = models.FloatField()
    temperature: float = models.FloatField()
    pulse: int = models.IntegerField()
    bloodOxygenLevel: float = models.FloatField()


class MedicalAppointment(models.Model):
    id: int = models.AutoField(primary_key=True)
    idPatient: int = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument',
                                       db_column='idPatient', related_name='appointment_patient')
    idDoctor: int = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idDoctor',
                                      related_name='appointment_employee')
    date: str = models.CharField(max_length=80)


class Invoice(models.Model):
    id: int = models.AutoField(primary_key=True)
    idMedicalAppointment: int = models.ForeignKey(MedicalAppointment, on_delete=models.CASCADE,
                                                  to_field='id', db_column='idMedicalAppointment',
                                                  related_name='invoice_Appointment')


class OrderMedication(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder',
                                     related_name='OrderMedication_Order')
    idMedication: int = models.ForeignKey(Medication, on_delete=models.CASCADE, to_field='id',
                                          db_column='idMedication', related_name='OrderMedication_Medication')
    dose: float = models.FloatField()
    treatmentDuration: str = models.CharField(max_length=100)
    amount: float = models.FloatField()
    item: int = models.IntegerField()


class OrderProcedure(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder',
                                     related_name='OrderProcedure_Order')
    idProcedure: int = models.ForeignKey(Procedure, on_delete=models.CASCADE, to_field='id',
                                         db_column='idProcedure', related_name='OrderProcedure_Procedure')
    amount: float = models.FloatField()
    frequency: str = models.CharField(max_length=100)
    item: int = models.IntegerField()


class OrderProcedureAssistance(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrderProcedure: int = models.ForeignKey(OrderProcedure, on_delete=models.CASCADE, to_field='id',
                                              db_column='idOrderProcedure',
                                              related_name='OrderProcedureAssistance_OrderProcedure')
    idSpecialist: str = models.CharField(max_length=255)


class OrderHelpDiagnostic(models.Model):
    id: int = models.AutoField(primary_key=True)
    idOrder: int = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder',
                                     related_name='OrderHelpDiagnostic_Order')
    nameHelpDiagnostic: str = models.CharField(max_length=255)
    quantity: float = models.FloatField()
    amount: float = models.FloatField()
    item: int = models.IntegerField()


class ClinicalVisit(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='idDocument', db_column='idPatient',
                                  related_name='clinicalVisit_patient')
    date = models.CharField(max_length=30)
    vitalData = models.ForeignKey(VitalData, on_delete=models.CASCADE, to_field='id', db_column='idVitalData',
                                  related_name='clinicalVisit_vitalData')


class OrderMedicationVisit(models.Model):
    idClinicalVisit = models.ForeignKey(ClinicalVisit, on_delete=models.CASCADE, to_field='id',
                                        db_column='idClinicalVisit', related_name='orderMedicationVisit_clinicalVisit')
    idOrder = models.ForeignKey(OrderMedication, on_delete=models.CASCADE, to_field='id', db_column='idOrder',
                                related_name='orderMedicationVisit_order')


class OrderProcedureVisit(models.Model):
    idClinicalVisit = models.ForeignKey(ClinicalVisit, on_delete=models.CASCADE, to_field='id',
                                        db_column='idClinicalVisit', related_name='orderProcedureVisit_clinicalVisit')
    idOrder = models.ForeignKey(OrderProcedure, on_delete=models.CASCADE, to_field='id', db_column='idOrder',
                                related_name='orderProcedureVisit_order')


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    idEmployee = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='id', db_column='idEmployee')
    token = models.CharField(max_length=255)
    date = models.CharField(max_length=30)
