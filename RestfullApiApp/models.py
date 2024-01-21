from django.db import models

class Model1(models.Model):
    pole1 = models.CharField(max_length=100)
    pole2 = models.IntegerField()