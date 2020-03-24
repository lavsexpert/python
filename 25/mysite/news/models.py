from django.db import models


# Create your models here.

class News(models.Model):
    objects = models.Manager()
    news_title = models.CharField(max_length=50)
    news_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.news_text
