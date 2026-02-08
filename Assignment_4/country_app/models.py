from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')
    population = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return self.name