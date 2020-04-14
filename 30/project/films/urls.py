from django.urls import path
from . import  views

app_name = 'films'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.detail, name="detail"),
    path('vote/<int:id>', views.vote, name="vote")
]