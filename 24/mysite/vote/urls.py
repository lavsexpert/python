from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    # /vote/
    path('', views.IndexView.as_view(), name='index'),
    # /vote/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /vote/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /vote/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]