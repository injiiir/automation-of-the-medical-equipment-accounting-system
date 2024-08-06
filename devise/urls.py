from django.urls import path
from .views import rest_dev

urlpatterns = [
    path('rest_dev/', rest_dev, name='rest_dev'),
]
