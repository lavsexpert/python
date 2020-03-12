from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_text.short_description = 'Текст вопроса'
    pub_date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.question_text
    def was_published(self):
        now = timezone.now()
        return self.pub_date <= now
    was_published.admin_order_field = 'pub_date'
    was_published.boolean = True
    was_published.short_description = 'Уже опубликовано?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text