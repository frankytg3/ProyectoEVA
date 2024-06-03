# Generated by Django 5.0.4 on 2024-06-03 04:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0037_pregunta_puntos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monitoreoexamen',
            options={'verbose_name': 'monitoreo_examen', 'verbose_name_plural': 'monitoreo_examenes'},
        ),
        migrations.AddField(
            model_name='monitoreoexamen',
            name='inicio_evaluacion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Inicio de Evaluación'),
        ),
        migrations.AlterModelTable(
            name='monitoreoexamen',
            table='monitoreo_examenes',
        ),
    ]
