from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50, unique=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_editor', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=255, unique=True)),
                ('time', models.DateTimeField()),
                ('name_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('name_engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.engineer')),
            ],
        ),
        migrations.CreateModel(
            name='Metrological',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=255, unique=True)),
                ('name_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('name_engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.engineer')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual', models.CharField(max_length=250)),
                ('registration_document', models.CharField(max_length=250)),
                ('sertificate', models.CharField(max_length=250)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.manufacturer'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.question')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.service')),
            ],
            options={
                'unique_together': {('device', 'service')},
            },
        ),
        migrations.CreateModel(
            name='DeviceMetrological',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('metrological', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.metrological')),
            ],
            options={
                'unique_together': {('device', 'metrological')},
            },
        ),
        migrations.CreateModel(
            name='DeviceManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.manufacturer')),
            ],
            options={
                'unique_together': {('device', 'manufacturer')},
            },
        ),
        migrations.CreateModel(
            name='DeviceDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.department')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
            options={
                'unique_together': {('device', 'department')},
            },
        ),
    ]
