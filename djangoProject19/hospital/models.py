from django.db import models
#from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField


class Hospital(models.Model):  #医院登陆界面
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    contact_info = JSONField()  # 用于存储电话、邮箱等联系信息

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_list'


class Doctor(models.Model):   #医生登陆
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    #hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
     # 允许字段为空
  # 存储额外的医生信息，如教育背景、工作经验等

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'doctor'

class Patient(models.Model):   #病人登陆
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medical_history = JSONField()  # 存储病史、过敏史等信息

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'patient'

class Pharmacy(models.Model):   #药房
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medical_history = JSONField()  # 存储病史、过敏史等信息

    #药品清单
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pharmacy'


class Prescription(models.Model):   #处方
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'prescription'



class Medicalrecord(models.Model):   #就诊记录
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    Record = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medicalrecord'


