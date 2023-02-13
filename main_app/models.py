from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=100)
    pricing = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name
