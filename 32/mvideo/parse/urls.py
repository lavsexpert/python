from django.urls import path
from parse.views import ParseView

urlpatterns = [
    path('', ParseView.as_view())
]