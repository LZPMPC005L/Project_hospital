from django.db import models


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Docter(models.Model):
    Docter_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Administrator(models.Model):
    Administrator_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
