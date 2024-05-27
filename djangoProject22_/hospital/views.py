from django.http import JsonResponse
from rest_framework import viewsets,permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Patient, Doctor, Appointment, MedicalRecord, Prescription, Medicine
from .serializers import UserSerializer, RegisterSerializer,PatientSerializer, DoctorSerializer, AppointmentSerializer, MedicalRecordSerializer, PrescriptionSerializer, MedicineSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse({'status': 'User registered successfully'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'User logged in successfully'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_data = UserSerializer(user).data
            if hasattr(user, 'patient'):
                role = 'patient'
                extra_data = PatientSerializer(user.patient).data
            elif hasattr(user, 'doctor'):
                role = 'doctor'
                extra_data = DoctorSerializer(user.doctor).data
            else:
                role = 'admin'
                extra_data = {}

            user_data['role'] = role
            user_data.update(extra_data)
            return JsonResponse(user_data)
        return JsonResponse({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=True, methods=['get'])
    def medical_records(self, request, pk=None):
        patient = self.get_object()
        records = MedicalRecord.objects.filter(patient=patient)
        serializer = MedicalRecordSerializer(records, many=True)
        return JsonResponse(serializer.data)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['get'])
    def appointments(self, request, pk=None):
        doctor = self.get_object()
        appointments = Appointment.objects.filter(doctor=doctor)
        serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data)

    @action(detail=True, methods=['post'])
    def add_record(self, request, pk=None):
        doctor = self.get_object()
        patient_id = request.data.get('patient_id')
        appointment_id = request.data.get('appointment_id')
        record = request.data.get('record')
        patient = Patient.objects.get(id=patient_id)
        appointment = Appointment.objects.get(id=appointment_id)
        MedicalRecord.objects.create(patient=patient, doctor=doctor, appointment=appointment, record=record)
        return JsonResponse({'status': 'record added'})

    @action(detail=True, methods=['post'])
    def prescribe_medicine(self, request, pk=None):
        doctor = self.get_object()
        patient_id = request.data.get('patient_id')
        medicine_name = request.data.get('medicine_name')
        quantity = request.data.get('quantity')
        medicine, created = Medicine.objects.get_or_create(name=medicine_name)
        if not created:
            medicine.quantity -= int(quantity)
            if medicine.quantity < 0:
                return JsonResponse({'status': 'not enough stock'}, status=400)
            medicine.save()
        return JsonResponse({'status': 'medicine prescribed'})

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['post'])
    def make_appointment(request):
        if request.method == 'POST':
            doctor_id = request.POST.get('doctor')
            patient_id = request.POST.get('patient')
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')

            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(id=patient_id)

            appointment = Appointment(doctor=doctor, patient=patient, appointment_date=appointment_date,
                                      appointment_time=appointment_time)
            appointment.save()

            return JsonResponse(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED) # 跳转到预约成功页面

        #doctors = Doctor.objects.all()
        #patients = Patient.objects.all()

        else:

                return JsonResponse({'error': 'Doctor not found'}, status=status.HTTP_400_BAD_REQUEST)



class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    @action(detail=True, methods=['post'])
    def make_appointment(request):
        if request.method == 'POST':
            doctor_id = request.POST.get('doctor')
            patient_id = request.POST.get('patient')
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')

            doctor = Doctor.objects.get(id=doctor_id)
            patient = Patient.objects.get(id=patient_id)

            appointment = Appointment(doctor=doctor, patient=patient, appointment_date=appointment_date,
                                      appointment_time=appointment_time)
            appointment.save()

            return JsonResponse(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED)  # 跳转到预约成功页面

        # doctors = Doctor.objects.all()
        # patients = Patient.objects.all()

        else:

            return JsonResponse({'error': 'Doctor not found'}, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    medications = PrescriptionSerializer(many=True, source='prescription_set')

    class Meta:
        model = Prescription
        fields = '__all__'

    @action(detail=True, methods=['post'])
    def create_prescription(self, validated_data):

        medications_data = validated_data.pop('prescription_set')
        prescription = Prescription.objects.create(**validated_data)
        for medication_data in medications_data:
            Prescription.objects.create(prescription=prescription, **medication_data)
        return prescription

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        medicines = Medicine.objects.filter(quantity__lt=10)
        serializer = MedicineSerializer(medicines, many=True)
        return JsonResponse(serializer.data)


