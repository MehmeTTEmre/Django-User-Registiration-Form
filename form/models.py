from django.db import models

# Create your models here.

class Form(models.Model):
    
    Id = models.AutoField(primary_key=True)
    TCNumber = models.CharField(max_length=11, verbose_name="TC kimlik numarası")
    name = models.CharField(max_length=120, verbose_name="İsim")
    surname = models.CharField(max_length=120, verbose_name="Soyisim")
    tel = models.CharField(max_length=11, verbose_name="Telefon")
    city = models.CharField(max_length=120, verbose_name="Şehir")
    state = models.CharField(max_length=120, verbose_name="İlçe")
    
    def __str__(self):
        return str(self.Id)
   
