#для преобразования сложных данных в типы данных самого питона (xml и др.)
from rest_framework import serializers
from .models import Device, Engineer, Documents, Metrological, Service, Department, Manufacturer, DeviceManufacturer

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'serial_number', 'manufacturer', 'date_created']

class UserSerializer(serializers.ModelSerializer):#для инженеров
    class Meta:
        model = Engineer
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = 'all'

class MetrologicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrological
        fields = 'all'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = 'all'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class DeviceManufacturerSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = DeviceManufacturer
        fields = '__all__'
