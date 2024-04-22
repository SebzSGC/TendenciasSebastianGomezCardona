from django.core.management.base import BaseCommand
from hospitalApp import models


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):
        # Insertar datos en la base de datos
        patients_data = [
            {
                "idDocument": 1040570286,
                "fullName": "Sebastian Gomez Cardona",
                "bornDate": "27/02/2004",
                "genre": "Masculino",
                "address": "Direccion",
                "phoneNumber": "3008254738",
                "email": "correo1@example.com"
            },
            {
                "idDocument": 12345,
                "fullName": "Paula Pérez",
                "bornDate": "01/01/2000",
                "genre": "Femenino",
                "address": "Dirección del paciente 2",
                "phoneNumber": "987654321",
                "email": "correo2@example.com"
            },
            # Agrega más diccionarios de datos para crear más pacientes
        ]

        for data in patients_data:
            models.Patient.objects.create(**data)

        employee_data = [
            {
                "fullName": "Duvan Gomez Cardona",
                "email": "correo1@example.com",
                "phoneNumber": "123456789",
                "bornDate": "28/01/1998",
                "address": "Dirección 1",
                "rol": "Doctor",
                "userName": "usuario1",
                "password": "contraseña1"
            },
            {
                "fullName": "Juan David Gomez",
                "email": "correo2@example.com",
                "phoneNumber": "987654321",
                "bornDate": "28/01/1998",
                "address": "Dirección 2",
                "rol": "Administrador",
                "userName": "usuario2",
                "password": "contraseña2"
            },
            # Agrega más diccionarios de datos para crear más pacientes
        ]

        for data in employee_data:
            models.Employee.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
