# Generated by Django 3.2.10 on 2021-12-23 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0012_alter_turno_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'ordering': ['id', '-documento'], 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
    ]
