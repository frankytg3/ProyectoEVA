# Generated by Django 5.0.4 on 2024-05-03 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0022_alter_evaluaciones_options_alter_evaluaciones_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregunta',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.AlterModelTable(
            name='pregunta',
            table='preguntas',
        ),
    ]