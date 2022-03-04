from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


# Create your models here.

class Form(models.Model):
    
    Id = models.AutoField(primary_key=True)
    TCNumber = models.CharField(max_length=11, validators=[MinLengthValidator(11)], verbose_name="TC kimlik numarası")
    name = models.CharField(max_length=120, verbose_name="İsim")
    surname = models.CharField(max_length=120, verbose_name="Soyisim")
    tel = models.CharField(max_length=11, validators=[MinLengthValidator(11)], verbose_name="Telefon")
    city = models.CharField(max_length=120, verbose_name="Şehir")
    state = models.CharField(max_length=120, verbose_name="İlçe")

    def __str__(self):
        return str(self.Id)

    def name_valid(self):
        if self.name.isalpha() == True:
            return self.name
        else:
            raise ValidationError("Wrong input")

    def surname_valid(self):
        if self.surname.isalpha() == True:
            return self.surname
        else:
            raise ValidationError("Wrong input")
   
    def city_valid(self):
        if self.city.isalpha() == True:
            return self.city
        else:
            raise ValidationError("Wrong input")

    def state_valid(self):
        if self.state.isalpha() == True:
            return self.state
        else:
            raise ValidationError("Wrong input")


    def TC_valid(self):
        if self.TCNumber.isnumeric() == True:
            return self.TCNumber
        else:
            raise ValidationError("Wrong input")

    def tel_valid(self):
        if self.tel.isnumeric() == True:
            return self.tel
        else:
            raise ValidationError("Wrong input")