from django.shortcuts import render, redirect
from .models import Patient
from .patient_form import PatientForm


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patient': patients})


def patient_detail(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})


def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'patient_create.html', {'form': form})


def patient_update(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'patient_create.html', {'form': form})


def patient_delete(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_delete.html', {'patient': patient})