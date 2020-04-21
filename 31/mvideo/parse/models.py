from django.db import models

class Comp(models.Model):
    image = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + " - " + str(self.price)