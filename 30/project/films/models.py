from django.core.validators import MaxLengthValidator
from django.db import models

class Film(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    text = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])
    rating = models.IntegerField()
    image = models.CharField(max_length=256, default="https://upload.wikimedia.org/wikipedia/ru/thumb/9/9d/Matrix-DVD.jpg/325px-Matrix-DVD.jpg")

    def __str__(self):
        return self.name + " (" + str(self.year) + ")"