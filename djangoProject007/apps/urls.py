from django.contrib import admin
from django.urls import path,include

#import os
#import sys

#father_path = os.path.abspath(os.path.join(os.getcwd(), "..", "apps"))
#sys.path.append(father_path)
from apps import views as patient_views

urlpatterns = [
    path('apps/add/', patient_views.patient_create, name='patient_create'),
    path('apps/<int:patient_id>/update/', patient_views.patient_update, name='patient_update'),
    path('apps/<int:patient_id>/delete/', patient_views.patient_delete, name='patient_delete'),
    path('apps/<int:patient_id>/', patient_views.patient_detail, name='patient_detail'),
    path('apps/', patient_views.patient_list, name='patient_list'),

]