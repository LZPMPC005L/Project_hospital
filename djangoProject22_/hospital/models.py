from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model): #病人登陆
    name = models.CharField(unique=True, max_length=200, verbose_name="Name", help_text="Name")
    Email = models.CharField(max_length=20, verbose_name="Email", help_text="Emain")
    #phone = models.CharField(max_length=15)
    #address = models.TextField()

    class Meta:
        db_table = 'Patient_projects'

    def __str__(self):
        return self.user.username

class Doctor(models.Model):  #医生
    name = models.CharField(unique=True, max_length=200, verbose_name="Name", help_text="Name")
    Email = models.CharField(max_length=20, verbose_name="Email", help_text="Emain")
    #specialty = models.CharField(max_length=50)

    class Meta:
        db_table = 'Doctor_projects'

    def __str__(self):
        return self.user.username

class Appointment(models.Model):   #预约
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        db_table = 'Appointment_projects'

    def __str__(self):
        return f"Appointment with {self.doctor.user.username} on {self.date}"

class MedicalRecord(models.Model):  #就诊记录
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    record = models.TextField()

    class Meta:
        db_table = 'MedicalRecord_projects'

    def __str__(self):
        return f"Medical record for {self.patient.user.username}"


class Prescription(models.Model):   #处方
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    price= models.TextField()

    class Meta:
        db_table = 'Prescription_projects'

    def __str__(self):
        return f"Appointment with {self.doctor.user.username} on {self.date}"

class Medicine(models.Model):  #药品药房
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'Medicine_projects'

    def __str__(self):
        return self.name

    def is_low_stock(self):
        return self.quantity < 10