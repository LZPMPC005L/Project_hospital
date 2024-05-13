from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
#from rest_framework.response import JsonResponse
from .models import Doctor
from django.http import HttpResponseNotAllowed
import json
from rest_framework import viewsets




from rest_framework import mixins
from hospital.serializers import DoctorSerializer
# 定义views方法
class DoctorEdit(
                  # 实现查(GET) 、改(PATCH(部分)/PUT(全部))、 增(POST)、 删(DELETE)
                  # 功能（postman和页面中都可以使用）
                  mixins.ListModelMixin,       # 查
                  mixins.RetrieveModelMixin,  # 改
                  mixins.DestroyModelMixin,   # 删
                  mixins.CreateModelMixin,   # 增
                  viewsets.GenericViewSet):
    # 查询医生表中的信息
    queryset = Doctor.objects.all()
    # 将查询到的信息序列化  DoctorSerializer是serializers.py中定义的类
    serializer_class = DoctorSerializer



@csrf_exempt
def hospital_user_list(request):
    if request.method == 'POST':
        # 获取POST请求中的数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户名和密码
        doctor = authenticate(request, username=username, password=password)

        if doctor is not None:
            # 登录用户
            login(request, doctor)
            # 返回成功登录的JSON响应
            return JsonResponse({'status': 'success', 'message': 'Doctor logged in successfully'})
        else:
            # 返回登录失败的JSON响应
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
    else:
        # 如果请求方法不是POST，则返回错误信息
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def doctor_login(request):
    if request.method == 'POST':
        # 获取POST请求中的数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户名和密码
        doctor = authenticate(request, username=username, password=password)

        if doctor is not None:
            # 登录用户
            login(request, doctor)
            # 返回成功登录的JSON响应
            return JsonResponse({'status': 'success', 'message': 'Doctor logged in successfully'})
        else:
            # 返回登录失败的JSON响应
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
    else:
        # 如果请求方法不是POST，则返回错误信息
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add_doctor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Doctor added successfully'}, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        # 对于非POST请求，返回一个HttpResponseNotAllowed响应
        return HttpResponseNotAllowed(['POST'], content='This view only accepts POST requests.')


@csrf_exempt
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        doctor_data = []

        for doctor in doctors:
            doctor_data.append({
                'name' : doctor.name,
                'department' : doctor.department,
                'position':doctor.position
            })

        return JsonResponse({'doctors' : doctor_data})
    else:
        return JsonResponse({'error':'Invalid Request Method'}, status = 400)


@csrf_exempt
def write_medical_record(request):
    def write_medical_record(request):
        try:
            data = json.loads(request.body)
            # Rest of your code...
        except json.JSONDecodeError:
            # Handle the JSON decoding error if the body is not valid JSON
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

            # Your processing code here...

        response_data = {
            'status': 'success',
            'message': '病历已成功写入',
            # Add any additional data you want to return
        }
        return JsonResponse(response_data)

