# Generated by Django 5.0.4 on 2024-05-02 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_alter_docente_fecha_nacimiento_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webApp.docente'),
        ),
    ]
