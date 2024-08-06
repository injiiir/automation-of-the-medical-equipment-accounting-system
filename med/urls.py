from django.contrib import admin
from django.urls import path, include
from device.views import test, rest_dev

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', router.urls),
    path('devices/', rest_dev),
    # path('admin/', admin.site.urls),
    # path('test', test),
    # path('api-auth/', include ('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
