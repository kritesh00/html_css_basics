from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='vehicle_photos/')
    description = models.TextField()

    def __str__(self):
        return self.name
