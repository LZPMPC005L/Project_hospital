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
        return self.name

    class Meta:
        db_table = 'user_list'


#class Doctor(models.Model):   #医生登陆
    #name = models.CharField(max_length=255)
    #specialization = models.CharField(max_length=255)
    #hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
     # 允许字段为空
  # 存储额外的医生信息，如教育背景、工作经验等

        # def __str__(self):
    #  return self.name
    #class Meta:
# db_table = 'doctor'
class Doctor(models.Model):
    # 设置id为主键
    #id = models.AutoField(primary_key=True, verbose_name="id主键", help_text="id主键")
    name = models.CharField(unique=True, max_length=200, verbose_name="Name", help_text="Name")
    Email = models.CharField(max_length=20, verbose_name="Email", help_text="Emain",default='')
    Administrative_office = models.CharField(max_length=20, verbose_name="Administrative office", help_text="Administrative office", default="")
    Curriculum_vitae = models.TextField(max_length=200, verbose_name="Curriculum vitae", help_text="Curriculum vitae", blank=True, null=True,
                            default="")

    class Meta:
        db_table = 'doctor_projects'
        verbose_name = 'Doctor'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Patient(models.Model):   #病人登陆

    name = models.CharField(unique=True, max_length=200, verbose_name="Name", help_text="Name")
    Email = models.CharField(max_length=20, verbose_name="Email", help_text="Emain")
    date_of_birth = models.DateField(max_length=20, verbose_name="Date of birth", help_text="Date of birth")
    Doctor_appointment = models.CharField(max_length=20, verbose_name="Doctor appointment", help_text="Doctor appointment")
    Time_appointment = models.CharField(max_length=20, verbose_name="Time appointment",help_text="Time appointment")
    Registered_department= models.CharField(max_length=20, verbose_name="Registered department", help_text="Registered department")
    Disease_history = models.TextField(max_length=200, verbose_name="medical history", help_text="medical history",
                                       blank=True, null=True,
                                       default="")

    class Meta:
        db_table = 'patient_projects'
        verbose_name = 'Patient'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Pharmacy(models.Model):   #药房
    Drug_name = models.CharField(unique=True, max_length=200, verbose_name="Drug name", help_text="Drug name")
    Drug_price = models.CharField(max_length=20, verbose_name="Drug price", help_text="Drug price")
    Shelf_life = models.DateField(max_length=20, verbose_name="Shelf life", help_text="Shelf life")
    Pieces_in_stock= models.CharField(max_length=20, verbose_name="Pieces in stock",
                                          help_text="Pieces in stock")
    Specification = models.TextField(max_length=200, verbose_name="Specification", help_text="Specification",
                                        blank=True, null=True,
                                        default="")
    #药品清单
    class Meta:
        db_table = 'pharmacy_projects'
        verbose_name = 'Pharmacy'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class Prescription(models.Model):   #处方
    Responsible_doctor = models.CharField(max_length=20, verbose_name="Responsible doctor", help_text="Responsible doctor")
    Patient_name = models.CharField(max_length=20, verbose_name="Patient name", help_text="Patient name")
    Prescription_time = models.DateField(unique=True, max_length=200, verbose_name="Prescription time",
                                         help_text="Prescription time")
    Prescription_content= models.TextField(max_length=200, verbose_name="Prescription content", help_text="Prescription content",
                                     blank=True, null=True,
                                     default="")


    class Meta:
        db_table = 'prescription_projects'
        verbose_name = 'Prescription'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Medicalrecord(models.Model):   #就诊记录
    Historical_visit_time = models.DateField(unique=True, max_length=200, verbose_name="PHistorical visit time",
                                         help_text="Historical visit time", default="")
    Historical_medical_record = models.TextField(max_length=200, verbose_name="Historical medical record",
                                            help_text="Historical medical record",
                                            blank=True, null=True,
                                            default="")

    Latest_visit_time = models.DateField(max_length=20, verbose_name="Latest visit time", help_text="Latest visit time", default="")
    Latest_medical_records = models.TextField(max_length=200, verbose_name="Latest medical records",
                                              help_text="Latest medical records",
                                              blank=True, null=True,
                                              default="")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'medicalrecord'

