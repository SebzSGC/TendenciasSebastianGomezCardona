import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .service.RolService import AdministrativePersonal


# Create your views here.
class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            body = json.loads(request.body)
            idDocument = body.get("idDocument")
            fullName = body.get("fullName")
            bornDate = body.get("bornDate")
            genre = body.get("genre")
            address = body.get("address")
            phoneNumber = body.get("phoneNumber")
            email = body.get("email")
            AdministrativePersonal.createPatient(
                idDocument, fullName, bornDate, genre, address, phoneNumber, email
            )
            message = f'Paciente {fullName} creado satisfactoriamente'
            status = 200
        except ObjectDoesNotExist:
            message = "Paciente no encontrado"
            status = 404
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)

    def get(self, request, idDocument=None):
        try:
            if idDocument is not None:
                response = AdministrativePersonal.getPatient(idDocument)
            else:
                response = AdministrativePersonal.getPatients()
            status = 200
        except ObjectDoesNotExist:
            message = "Paciente no encontrado"
            status = 404
            response = {"message": message}
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
        return JsonResponse(response, status=status, safe=False)

    def put(self, request, idDocument):
        try:
            body = json.loads(request.body)
            fullName = body.get("fullName")
            bornDate = body.get("bornDate")
            genre = body.get("genre")
            address = body.get("address")
            phoneNumber = body.get("phoneNumber")
            email = body.get("email")
            print(fullName, bornDate, genre, address, phoneNumber, email)
            AdministrativePersonal.updatePatient(
                idDocument, fullName, bornDate, genre, address, phoneNumber, email
            )
            message = f'Paciente {fullName} actualizado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)


# class EmergencyContactView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args: any, **kwargs: any):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         try:
#             body = json.loads(request.body)
#             idPatient = body.get("idPatient")
#             fullName = body.get("fullName")
#             relationship = body.get("relationship")
#             phoneNumber = body.get("phoneNumber")
#             AdministrativePersonal.createEmergencyContact(
#                 fullName, relationship, phoneNumber, idPatient
#             )
#             message = f'Paciente{fullName} creado satisfactoriamente'
#             status = 200
#         except ObjectDoesNotExist:
#             message = "Paciente no encontrado"
#             status = 404
#         except Exception as error:
#             message = str(error)
#             status = 400
#         response = {"message": message}
#         return JsonResponse(response, status=status)
#
#     def get(self, request, id):
#         pass
