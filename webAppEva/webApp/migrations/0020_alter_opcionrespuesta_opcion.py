# Generated by Django 5.0.4 on 2024-05-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0019_rename_texto_opcionrespuesta_respuesta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcionrespuesta',
            name='opcion',
            field=models.CharField(choices=[('A', 'opcion A'), ('B', 'opcion B'), ('C', 'opcion C'), ('D', 'Opcion D')], max_length=1),
        ),
    ]
