from django.core.validators import MaxLengthValidator
from django.db import models

class Film(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    text = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])
    rating = models.IntegerField()
    image = models.CharField(max_length=256, default="https://yastatic.net/s3/home/logos/citylogos/distance/ru.png")

    def __str__(self):
        return self.name + " (" + str(self.year) + ")"