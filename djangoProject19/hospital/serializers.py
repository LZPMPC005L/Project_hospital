from rest_framework import serializers
from .models import Hospital, Doctor, Patient, Pharmacy, Prescription ,Medicalrecord


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address']  # 指定你想要序列化的字段


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'department']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'patient_id','adress','phone','age','email']

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['drug classification', 'drug_id','drug_price','drug_quantity']


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [ 'prescription_id','prescription_quantity']

class MedicalrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicalrecord
        fields = [ 'Medicalrecord_id','Medicalrecord_quantity']