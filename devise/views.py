from django_filters.utils import translate_validation

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DeviceManufacturer, Device, Documents, Metrological, Service, Department, DeviceDepartment, DeviceMetrological, DeviceService
from .serializers import DeviceManufacturerSerializer, DeviceSerializer, DocumentsSerializer, MetrologicalSerializer, ServiceSerializer, DepartmentSerializer
from .filters import DeviceManufacturerFilter, DeviceFilter, MetrologicalFilter, DocumentsFilter
from django.http import HttpResponse
from django.http import JsonResponse

def rest_dev(request):#обработка http-запросов
    return JsonResponse({'message': 'колхозно пытаюсь избавиться от ошибки'})

def test(request):
    # print("------------> a")
    # number = random.randint(1,1000)
    # m = Manufacturer.objects.create(name=f"{number}")
    # m.name="ask;djh"
    # #m.name = 
    # #print(f"----------->{number} ")
    # m.save()
    params = request.GET
    print(params['v'])
    return HttpResponse()

@api_view(["GET", "POST"])
def manufacturers(request):
    if request.method == "GET":
        # DeviceManufacturerFilter использует django-filter для обработки
        # параметров get-запроса  https://django-filter.readthedocs.io/en/stable/
        filters = DeviceManufacturerFilter(request.query_params, queryset=DeviceManufacturer.objects.all())
        if not filters.is_valid():
            raise translate_validation(filters.errors)
        serializer = DeviceManufacturerSerializer(filters.qs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DeviceManufacturerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        manufacturer = serializer.save()
        return Response(data={"id": manufacturer.id}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["PATCH"])
def manufacturer(request, pk):
    if request.method == "PATCH":
        serializer = new_func(request, pk)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def new_func(request, pk):
    serializer = DeviceManufacturerSerializer(DeviceManufacturer.objects.get(pk=pk), data=request.data, partial=True)
    return serializer

@api_view(["GET", "POST"])
def devices_models(request):
    if request.method == "GET":
        filters = DeviceFilter(request.query_params, queryset=Device.objects.all())
        if not filters.is_valid():
            raise translate_validation(filters.errors)
        serializer = DeviceSerializer(filters.qs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DeviceSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        device = serializer.save()
        return Response(data={"id": device.id}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["PATCH"])
def devices_models(request, pk):
    if request.method == "PATCH":
        serializer = DeviceSerializer.objects.get(manufacturer, pk=pk,  data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "POST"])
def documents_list(request):
    if request.method == "GET":
        filters = DocumentsFilter(request.query_params, queryset=Documents.objects.all())
        documents = Documents.objects.all()
        if not filters.is_valid():
            raise translate_validation(filters.errors)
        serializer = DocumentsSerializer(documents, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view (["PATCH"])
def documents_list(request, pk):
    if request.method =="PATCH":
        serializer = DocumentsSerializer.objects.get(Documents, pk=pk, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "POST"])
def metrological_list(request):
    if request.method == "GET":
        filters = MetrologicalFilter(request.query_params, queryset=Metrological.objects.all())
        metrological_records = Metrological.objects.all()
        if not filters.is_valid():
            serializer = MetrologicalSerializer(metrological_records, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = MetrologicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["PATCH"])
def metrological_list(request, pk):
    if request.method == "PATCH":
        serializer = MetrologicalSerializer(DeviceMetrological.object.get(pk=pk),data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "POST"])#скорее всего нужно поправить
def service_list(request):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(["PATCH"])
def service_list(request, pk):
    if request.method == "PATCH":
        serializer = ServiceSerializer(DeviceService.object.get(pk=pk), data=request.data, partial=True)
        if not serializer.is_valid():
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "POST"])#и тут тоже поправить. 
def department_list(request):
    if request.method == "GET":
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["PATCH"])
def department_list(request, pk):
    if request.method == "PATCH":
        serializer = DepartmentSerializer(DeviceDepartment.object.get(pk=pk), data=request.data, partial=True)
        if not serializer.is_valid():
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
