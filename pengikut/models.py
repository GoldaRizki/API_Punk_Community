from django.db import models

# Create your models here.

class Pengikut(models.Model):
    nama_asli = models.CharField(max_length = 255)
    nama_samaran = models.CharField(max_length = 50)


