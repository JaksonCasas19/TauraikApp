from django.db import models

# Create your models here.

class captureUser(models.Model):
    name = models.CharField(max_length=32)
    texto = models.CharField(max_length=32)
    qr = models.CharField(max_length=50)