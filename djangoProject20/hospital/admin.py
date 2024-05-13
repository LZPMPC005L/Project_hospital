from django.contrib import admin
from .models import Doctor,Patient,Prescription,Pharmacy,Medicalrecord


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Medicalrecord)
admin.site.register(Pharmacy)

