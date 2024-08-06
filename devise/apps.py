from django.apps import AppConfig


class ApiConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


class DeviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'device'
