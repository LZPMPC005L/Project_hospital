"""djangoProject22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet, PatientViewSet, DoctorViewSet, AppointmentViewSet, MedicalRecordViewSet, PrescriptionViewSet, MedicineViewSet
#from hospital.views import register
from .import views

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical_records', MedicalRecordViewSet)
router.register(r'medicines', MedicineViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('auth/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('auth/me/', UserViewSet.as_view({'get': 'me'}), name='me'),
   # path('patients/<int:pk>/medical_records/', PatientViewSet.as_view({'get': 'medical_records'}), name='patient-medical-records'),
    #path('doctors/appointments/', DoctorViewSet.as_view({'get': 'appointments'}), name='doctor-appointments'),
    path('appointments/', AppointmentViewSet.as_view({'post': 'make_appointment'}), name='appointments'),
    path('doctors/add_record/', DoctorViewSet.as_view({'post': 'add_record'}), name='doctor-add-record'),
    path('doctors/prescribe_medicine/', DoctorViewSet.as_view({'post': 'prescribe_medicine'}), name='doctor-prescribe-medicine'),
    path('create_prescription/', PrescriptionViewSet.as_view({'post': 'create_prescription'}), name='create_prescription'),
    path('medicines/low_stock/', MedicineViewSet.as_view({'get': 'low_stock'}), name='medicine-low-stock'),
]

# 使用 format_suffix_patterns 来支持 URL 后缀
urlpatterns = format_suffix_patterns(urlpatterns)
