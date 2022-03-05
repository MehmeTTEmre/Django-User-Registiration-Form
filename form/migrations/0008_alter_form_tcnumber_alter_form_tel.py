# Generated by Django 4.0.3 on 2022-03-05 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_form_tcnumber_form_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='TCNumber',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='TC kimlik numarası'),
        ),
        migrations.AlterField(
            model_name='form',
            name='tel',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='Telefon'),
        ),
    ]
