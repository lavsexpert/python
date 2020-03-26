from django.db import models

class Goods(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.name
