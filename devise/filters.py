import django_filters
from .models import DeviceManufacturer, Device, Metrological, Documents

class DeviceManufacturerFilter(django_filters.FilterSet):
    device_name = django_filters.CharFilter(field_name='device__name', lookup_expr='icontains')#для нормального поиска по первым нескольким буквам
    manufacturer_name = django_filters.CharFilter(field_name='manufacturer__name', lookup_expr='icontains')

    class Meta:
        model = DeviceManufacturer
        fields = ['device_name', 'manufacturer_name']

class DeviceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Device
        fields = ['name']

class MetrologicalFilter(django_filters.FilterSet):
    parameter = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Metrological
        fields = ['parameter']

class DocumentsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Documents
        fields = ['title']
