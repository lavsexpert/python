from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    # /vote/
    path('', views.index, name='index'),
    # /vote/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /vote/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /vote/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]