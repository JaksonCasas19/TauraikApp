from django.db import models

# Create your models here.

class captureUser(models.Model):
    name = models.CharField(max_length=32)
    estado = models.CharField(max_length=32)
    qr = models.CharField(max_length=50)

    def __str__(self):
        return self.name