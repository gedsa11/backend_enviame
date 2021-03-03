from django.db import models

# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    business_sector = models.CharField(max_length=200)
    legal_representative  = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
