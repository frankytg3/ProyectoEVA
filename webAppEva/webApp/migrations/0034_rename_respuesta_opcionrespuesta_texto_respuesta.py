# Generated by Django 5.0.4 on 2024-06-03 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0033_opcionrespuesta_es_correcta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opcionrespuesta',
            old_name='respuesta',
            new_name='texto_respuesta',
        ),
    ]
