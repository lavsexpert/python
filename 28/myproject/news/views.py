from django.http import HttpResponse
from django.template import loader
from .models import News


def index(request):
    news_list = News.objects.order_by('-date')[:5]
    template = loader.get_template('news/index.html')
    context = {
        'news_list': news_list,
    }
    return  HttpResponse(template.render(context, request))