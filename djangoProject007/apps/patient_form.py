from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'patient_id']
        labels = {
            'name': '姓名',
            'patient_id': '号码'
        }
        widgets = {
            'time': forms.DateInput(attrs={'type': 'date'})
        }