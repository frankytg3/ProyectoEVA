# Generated by Django 5.0.4 on 2024-05-31 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0027_docente_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docente',
            old_name='usuario',
            new_name='user',
        ),
    ]
