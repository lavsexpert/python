from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import News

def create_news(title, text, date):
    return News.objects.create(title=title, text=text, date=date)

class NewsModelTests(TestCase):

    def test_str_is_title(self):
        testnews = News()
        testnews.title = "test"
        self.assertIs(testnews.__str__(),"test")

    def test_no_news(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['news_list'], [])

    def test_one_news(self):
        create_news("title", "text", timezone.now())
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news_list']), 1)