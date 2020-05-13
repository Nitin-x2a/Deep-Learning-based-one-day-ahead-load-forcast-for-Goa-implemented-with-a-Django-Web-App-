from django.db import models

# Create your models here.
class Megawatts(models.Model):
    datafile = models.FileField(upload_to ='basic/data', null=True)

class Festival(models.Model):
    datafile = models.FileField(upload_to ='basic/data', null=True)
