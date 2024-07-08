# Generated by Django 5.0.4 on 2024-07-08 04:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePlanta', models.CharField(max_length=100)),
                ('codigoPlanta', models.CharField(max_length=5)),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=100)),
                ('codigoProducto', models.CharField(max_length=5)),
                ('tipoProducto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionDiaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estacion', models.CharField(max_length=12)),
                ('turno', models.CharField(max_length=2)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('litrosProduccion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigoPlanta', models.CharField(default='', max_length=5)),
                ('codigoCombustible', models.CharField(default='', max_length=5)),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
