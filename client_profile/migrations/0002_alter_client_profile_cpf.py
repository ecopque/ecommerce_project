# Generated by Django 5.1.1 on 2024-10-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_profile',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
    ]
