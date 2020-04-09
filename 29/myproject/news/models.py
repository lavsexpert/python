from django.db import models


class News(models.Model):
    objects = models.Manager
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date = models.DateField("Дата публикации")

    def __str__(self):
        return self.title