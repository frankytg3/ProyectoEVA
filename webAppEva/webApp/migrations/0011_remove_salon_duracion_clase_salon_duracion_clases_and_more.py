# Generated by Django 5.0.4 on 2024-05-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0010_alter_salon_options_alter_salon_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='duracion_clase',
        ),
        migrations.AddField(
            model_name='salon',
            name='duracion_clases',
            field=models.IntegerField(blank=True, help_text='Horas de duración', null=True),
        ),
        migrations.AlterField(
            model_name='salon',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salon',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
