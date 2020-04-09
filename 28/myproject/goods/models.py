from django.db import models
from django.db.models import DO_NOTHING


class Goods(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    price = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    count = models.IntegerField()
    total = models.FloatField(default=0)
    goods_id = models.ForeignKey(Goods, on_delete=DO_NOTHING, default=0)

    def __str__(self):
        return self.name
