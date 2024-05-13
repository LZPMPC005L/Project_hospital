"""djangoProject20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from hospital.views import hospital_user_list, doctor_login,add_doctor,doctor_list,write_medical_record
from rest_framework.routers import SimpleRouter
from hospital.views import DoctorEdit

# 创建路由
router = SimpleRouter()
# 给路由绑定一个url
router.register(r'doctor', DoctorEdit)
# django 默认到urlpatterns中查找url, 故把次路由加到urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('user_list/', hospital_user_list, name='hospital_user_list'),
    #path('doctor/', doctor_login, name='doctor_login'),
    path('add_doctor/',add_doctor, name='add_doctor'),
    path('responsible_doctor/', doctor_list, name='doctor_list'),#√#责任医生
    path('medical_record/', write_medical_record, name='write_medical_record')





]


urlpatterns += router.urls