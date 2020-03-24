from django.urls import path
from . import views


app_name = 'news'
urlpatterns = [
    # /news/
    path('', views.news, name='index'),
]