# Generated by Django 3.2.10 on 2021-12-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=30, null=True, verbose_name='Apellidos:')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('telefono', models.CharField(max_length=10, null=True, verbose_name='Telefono')),
                ('correo', models.CharField(max_length=30, null=True, verbose_name='Correo Electronico')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
                'db_table': 'funcionario',
                'ordering': ['apellidos', '-nombres'],
            },
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Turno',
        ),
    ]
