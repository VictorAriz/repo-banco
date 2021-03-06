# Generated by Django 3.2.10 on 2021-12-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('tipodocumento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('TI', 'Tarjeta de Identidad')], default='CC', max_length=2)),
                ('documento', models.CharField(max_length=20, verbose_name='Numero de Documento')),
            ],
        ),
    ]
