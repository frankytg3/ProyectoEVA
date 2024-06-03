# Generated by Django 5.0.4 on 2024-06-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0031_respuestacorrecta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcionrespuesta',
            name='opcion',
            field=models.CharField(choices=[('A', 'opcion A'), ('B', 'opcion B'), ('C', 'opcion C'), ('D', 'opcion D')], max_length=1),
        ),
        migrations.DeleteModel(
            name='RespuestaCorrecta',
        ),
    ]
