"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import hospitalApp.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    ##CRUD patients
    path('hospital/patients', views.PatientView.as_view(), name='patient post'),
    path('hospital/patients/<int:idDocument>', views.PatientView.as_view(), name="patient get put"),
    path('hospital/patients/<int:idPatient>/emergencycontact', views.EmergencyContactView.as_view(),
         name="emergency contact get post put"),
    path('hospital/patients/<int:idPatient>/medicalinsurance', views.MedicalInsuranceView.as_view(),
         name="medical insurance get post put"),
    ##CRUD employees
    path('hospital/employees', views.EmployeeView.as_view(), name='employee post'),
    path('hospital/employees/<int:idEmployee>', views.EmployeeView.as_view(),
         name="employee get put"),
    path('hospital/employees/doctor/<int:idDocument>', views.DoctorView.as_view(),
         name="doctor get datapatient"),
    ##@param: patientdata or clinicalhistory or appointmentsMade or appointments or generatehistory
    path('hospital/employees/doctor/<str:param>/<int:idDocument>', views.DoctorView.as_view(),
         name="doctor data patient get"),
    path('hospital/login', views.LoginView.as_view(), name="login"),
    path('hospital/patients/appointments', views.AppointmentView.as_view(), name="appointment post"),
    path('hospital/patients/appointments/<str:date>/<int:idDocument>', views.AppointmentView.as_view(), name="appointment get"),
]
