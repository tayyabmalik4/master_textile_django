from django.db import models

# Create your models here.
class dht11(models.Model):
    temperature = models.CharField(max_length=122)
    humidity = models.CharField(max_length=122)
    time = models.TimeField()
    date = models.DateField()
