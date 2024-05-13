from rest_framework import serializers
from hospital.models import Hospital, Doctor,Patient


# hospital下的models.py文件下写的有个Doctor的模型
class DoctorSerializer(serializers.ModelSerializer):
    # 要修改的模型为Doctor
    model = Doctor
    # 访问127.0.0.1:8000/hospital/Doctor/时
    # 页面上显示id s_name s_tel 三项内容
    fields = ['id', 's_name', 's_tel']
    # 显示拓展信息表中的i_addr内容
    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
        # Doctor.i_addr是医生的拓展信息
            data['s_addr'] = instance.Doctor.i_addr
        # 异常处理
        except Exception as e:
            data['s_addr'] = ''
        return data

class PatientSerializer(serializers.ModelSerializer):

    model = Patient
    fields = ['id', 's_name','s_doctor', 's_history','s_time']
    # 显示拓展信息表中的i_addr内容
    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:

            data['s_addr'] = instance.Patient.i_addr
        # 异常处理
        except Exception as e:
            data['s_addr'] = ''
        return data




class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address']  # 指定你想要序列化的字段

