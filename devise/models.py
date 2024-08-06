from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Engineer(models.Model):
    name=models.OneToOneField(User, on_delete=models.CASCADE)
    position=models.CharField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)

class Manufacturer(models.Model):
    name=models.CharField(max_length=255, unique=True)

class Department(models.Model):#номера отделений, к которому прикреплено оборудование
    name=models.CharField(max_length=255, unique=True)

class Device(models.Model):
    name = models.CharField(max_length=100)
    status=models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=50)
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)#здесь указано, когда произведен девайс, то есть инф-ия от производителя

class Documents(models.Model):
    manual=models.CharField(max_length=250)
    registration_document=models.CharField(max_length=250)
    sertificate=models.CharField(max_length=250)
    name=models.ForeignKey(Device, on_delete=models.CASCADE)

class Metrological(models.Model):
    history=models.CharField(max_length=255, unique=True)#то есть "в ремонте", "вышел из ремонта"
    name_device=models.ForeignKey(Device, on_delete=models.CASCADE)
    name_engineer=models.ForeignKey(Engineer.__name__, on_delete=models.CASCADE)

class Service(models.Model):
    history=models.CharField(max_length=255, unique=True)#то есть "в ремонте", "вышел из ремонта"
    time=models.DateTimeField()
    name_device=models.ForeignKey(Device.__name__, on_delete=models.CASCADE)
    name_engineer=models.ForeignKey(Engineer.__name__, on_delete=models.CASCADE)

class DeviceManufacturer(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('device', 'manufacturer')
    def __str__(self):
        return f"{self.device.name} - {self.manufacturer.name}"#для верного отображения имени-производителя


class DeviceDepartment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('device', 'department')
    def __str__(self):
        return f"{self.device.name} - {self.department.name}"

class DeviceMetrological(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    metrological = models.ForeignKey(Metrological, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('device', 'metrological')
    def __str__(self):
        return f"{self.device.name} - {self.metrological.name}"
    
class DeviceService(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('device', 'service')
    def __str__(self):
        return f"{self.device.name} - {self.service}"
