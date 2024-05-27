from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Patient, Doctor, Appointment, MedicalRecord, Prescription, Medicine




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']  # is_staff 用于区分管理员


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=['patient', 'doctor', 'admin'], write_only=True)
    phone = serializers.CharField(write_only=True, required=False)
    address = serializers.CharField(write_only=True, required=False)
    specialty = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']#, 'phone', 'address', 'specialty'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        if role == 'patient':
            Patient.objects.create(user=user, phone=validated_data.get('phone'), address=validated_data.get('address'))
        elif role == 'doctor':
            Doctor.objects.create(user=user, specialty=validated_data.get('specialty'))
        elif role == 'admin':
            user.is_staff = True
            user.save()

        return user

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['user', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'email']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'description']

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'appointment', 'record']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'doctor', 'description']

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'quantity']
