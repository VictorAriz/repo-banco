# Generated by Django 3.2.10 on 2021-12-23 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_auto_20211222_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'ordering': ['nombres', '-documento'], 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
        migrations.AlterModelTable(
            name='turno',
            table='turno',
        ),
    ]
