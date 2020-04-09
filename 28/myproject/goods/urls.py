from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('', views.index, name='index'),
    path('basket', views.basket, name='basket'),
    path('result', views.result, name='result'),
    path('add', views.add, name='add')
]