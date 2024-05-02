import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from hospitalApp.service import validatorService, loginService
from hospitalApp.service.RolService import AdministrativePersonal, HumanResources, Doctor


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
                response = validatorService.getPatientById(idDocument)
            else:
                response = validatorService.getPatients()
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
            AdministrativePersonal.updatePatient(
                idDocument, fullName, bornDate, genre, address, phoneNumber, email
            )
            message = f'Paciente {fullName} actualizado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)


class AppointmentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            body = json.loads(request.body)
            idPatient = body.get("idPatient")
            idDoctor = body.get("idDoctor")
            date = body.get("date")
            AdministrativePersonal.generateAppointment(idPatient, idDoctor, date)
            message = "Cita creada satisfactoriamente"
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)

    def get(self, request, date=None, idPatient=None):
        try:
            if idPatient is not None and date is not None:
                response = validatorService.getAppointment(idPatient, date)
            else:
                response = validatorService.getAppointments()
            status = 200
        except ObjectDoesNotExist:
            message = "Cita no encontrada"
            status = 404
            response = {"message": message}
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
        return JsonResponse(response, status=status, safe=False)


class EmployeeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            body = json.loads(request.body)
            fullName = body.get("fullName")
            email = body.get("email")
            phoneNumber = body.get("phoneNumber")
            bornDate = body.get("bornDate")
            address = body.get("address")
            rol = body.get("rol")
            userName = body.get("userName")
            password = body.get("password")
            HumanResources.createEmployee(
                fullName, email, phoneNumber, bornDate, address, rol, userName, password
            )
            message = f'Empleado {fullName} creado satisfactoriamente'
            status = 200
        except ObjectDoesNotExist:
            message = "Empleado no encontrado"
            status = 404
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)

    def get(self, request, id=None):
        try:
            if id is not None:
                response = validatorService.getEmployeeById(id)
            else:
                response = validatorService.getEmployees()
            status = 200
        except ObjectDoesNotExist:
            message = "Empleado no encontrado"
            status = 404
            response = {"message": message}
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
        return JsonResponse(response, status=status, safe=False)

    def put(self, request, id):
        try:
            body = json.loads(request.body)
            fullName = body.get("fullName")
            email = body.get("email")
            phoneNumber = body.get("phoneNumber")
            bornDate = body.get("bornDate")
            address = body.get("address")
            rol = body.get("rol")
            userName = body.get("userName")
            password = body.get("password")
            HumanResources.updateEmployee(
                id, fullName, email, phoneNumber, bornDate, address, rol, userName, password
            )
            message = f'Empleado {fullName} actualizado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)

    def delete(self, request, id):
        try:
            HumanResources.deleteEmployee(id)
            message = "Empleado eliminado satisfactoriamente"
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)


class EmergencyContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, idPatient):
        try:
            body = json.loads(request.body)
            fullName = body.get("fullName")
            relationship = body.get("relationship")
            phoneNumber = body.get("phoneNumber")
            AdministrativePersonal.createEmergencyContact(
                fullName, relationship, phoneNumber, idPatient
            )
            message = f'Contacto {fullName} creado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)

    def put(self, request, idPatient):
        try:
            body = json.loads(request.body)
            fullName = body.get("fullName")
            relationship = body.get("relationship")
            phoneNumber = body.get("phoneNumber")
            AdministrativePersonal.updateEmergencyContact(
                idPatient, fullName, relationship, phoneNumber
            )
            message = f'contacto {fullName} actualizado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)

    def get(self, request, idPatient=None):
        try:
            if validatorService.validatePatientById(idPatient):
                response = validatorService.getEmergencyContactById(idPatient)
                status = 200
            else:
                raise ObjectDoesNotExist
        except ObjectDoesNotExist:
            message = "Contacto no encontrado"
            status = 404
            response = {"message": message}
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
        return JsonResponse(response, status=status, safe=False)


class MedicalInsuranceView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, idPatient):
        try:
            body = json.loads(request.body)
            nameOfInsuranceCompany = body.get("nameOfInsuranceCompany")
            policyNumber = body.get("policyNumber")
            policyState = body.get("policyState")
            policyValidity = body.get("policyValidity")
            AdministrativePersonal.createMedicalInsurance(
                idPatient, nameOfInsuranceCompany, policyNumber, policyState, policyValidity
            )
            message = f'Seguro medico {nameOfInsuranceCompany} creado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)

    def put(self, request, idPatient):
        try:
            body = json.loads(request.body)
            nameOfInsuranceCompany = body.get("nameOfInsuranceCompany")
            policyNumber = body.get("policyNumber")
            policyState = body.get("policyState")
            policyValidity = body.get("policyValidity")
            AdministrativePersonal.updateMedicalInsurance(
                idPatient, nameOfInsuranceCompany, policyNumber, policyState, policyValidity
            )
            message = f'Seguro medico {nameOfInsuranceCompany} actualizado satisfactoriamente'
            status = 200
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)

    def get(self, request, idPatient):
        try:
            if validatorService.validatePatientById(idPatient):
                response = validatorService.getMedicalInsuranceById(idPatient)
                status = 200
            else:
                raise ObjectDoesNotExist
        except ObjectDoesNotExist:
            message = "seguro medico no encontrado"
            status = 404
            response = {"message": message}
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
        return JsonResponse(response, status=status, safe=False)


class DoctorView(View):
    PARAM_GENERATE_HISTORY = "generatehistory"
    PARAM_GENERATE_ORDER = "generateorder"
    PARAM_GENERATE_ORDER_HELP_DIAGNOSTIC = "generateorderhelpdiagnostic"
    PARAM_GENERATE_ORDER_MEDICATION = "generateordermedication"
    PARAM_GENERATE_ORDER_PROCEDURE = "generateorderprocedure"
    PARAM_CLINICAL_HISTORY = "clinicalhistory"
    PARAM_BASIC_PATIENT_INFO = "patientdata"
    PARAM_APPOINTMENTS_MADE = "appointmentsmade"
    PARAM_APPOINTMENTS = "appointments"
    PARAM_ORDERS = "orders"

    def _handle_post_request(self, param, idDocument, body):
        body = json.loads(body)
        if param == self.PARAM_GENERATE_HISTORY:
            doctorDocument = body.get("doctorDocument")
            date = body.get("date")
            consultReason = body.get("consultReason")
            symptomatology = body.get("symptomatology")
            diagnosis = body.get("diagnosis")
            Doctor.generateHistory(
                idDocument, doctorDocument, date, consultReason, symptomatology, diagnosis
            )
            return "Historia clínica generada satisfactoriamente", 200
        elif param == self.PARAM_GENERATE_ORDER:
            idDoctor = body.get("idDoctor")
            idClinicalHistory = body.get("idClinicalHistory")
            Doctor.generateOrder(
                idDocument, idDoctor, idClinicalHistory
            )
            return "Orden generada satisfactoriamente", 200
        elif param == self.PARAM_GENERATE_ORDER_HELP_DIAGNOSTIC:
            idOrder = body.get("idOrder")
            idHistory = body.get("idHistory")
            helpDiagnostic = body.get("helpDiagnostic")
            item = body.get("item")
            quantity = body.get("quantity")
            amount = body.get("amount")
            Doctor.generateOrderHelpDiagnostic(
                idDocument, idHistory, idOrder, item, helpDiagnostic, quantity, amount
            )
            return "ayuda diagnostica para la orden generada satisfactoriamente", 200
        elif param == self.PARAM_GENERATE_ORDER_MEDICATION:
            idOrder = body.get("idOrder")
            idHistory = body.get("idHistory")
            item = body.get("item")
            idMedication = body.get("idMedication")
            dose = body.get("dose")
            treatmentDuration = body.get("treatmentDuration")
            amount = body.get("amount")
            Doctor.generateOrderMedication(
                idDocument, idHistory, idOrder, item, idMedication, dose, treatmentDuration, amount
            )
            return "Medicamento para la orden generada satisfactoriamente", 200
        elif param == self.PARAM_GENERATE_ORDER_PROCEDURE:
            idOrder = body.get("idOrder")
            item = body.get("item")
            idProcedure = body.get("idProcedure")
            amount = body.get("amount")
            frequency = body.get("frequency")
            Doctor.generateOrderProcedure(idDocument, idOrder, item, idProcedure, amount, frequency)
            return "Procedimiento para la orden generada satisfactoriamente", 200
        else:
            return "Parametro no valido", 400

    def _handle_get_request(self, param, idDocument):
        if idDocument is None:
            raise Exception("Falta un parametro")
        if param == self.PARAM_CLINICAL_HISTORY:
            return Doctor.getPatientClinicalHistory(idDocument)
        elif param == self.PARAM_BASIC_PATIENT_INFO:
            return Doctor.getBasicPatientInfo(idDocument)
        elif param == self.PARAM_APPOINTMENTS_MADE:
            return Doctor.getAppointmentsMade(idDocument)
        elif param == self.PARAM_APPOINTMENTS:
            return Doctor.getAppointments(idDocument)
        elif param == self.PARAM_ORDERS:
            return validatorService.getOrdersByIdPatient(idDocument)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, param, idDocument=None):
        try:
            response = self._handle_get_request(param, idDocument)
        except Exception as error:
            return JsonResponse({"message": str(error)}, status=400)
        return JsonResponse(response, status=200, safe=False)

    def post(self, request, param, idDocument):
        try:
            message, status = self._handle_post_request(param, idDocument, request.body)
        except Exception as error:
            message = str(error)
            status = 400
        return JsonResponse({"message": message}, status=status, safe=False)


class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            body = json.loads(request.body)
            session = loginService.login(body.get("userName"), body.get("password"))
            response = {"message": "Inicio de sesión exitoso", "token": session.token}
            status = 200
        except Exception as error:
            response = {"message": str(error)}
            status = 400
        return JsonResponse(response, status=status)

    def get(self, request):
        try:
            token = request.META.get("HTTP_TOKEN")
            session = loginService.getSession(token)
            rol = session.idEmployee.rol
            status = 200
            response = {"message": "Sesión activa", "rol": rol}
        except Exception as error:
            response = {"message": str(error)}
            status = 400
        return JsonResponse(response, status=status)

    def delete(self, request):
        try:
            token = request.META.get("HTTP_TOKEN")
            session = loginService.getSession(token)
            session.delete()
            response = {"message": "Sesión cerrada"}
            status = 200
        except Exception as error:
            response = {"message": str(error)}
            status = 400
        return JsonResponse(response, status=status)
