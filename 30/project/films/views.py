from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Film


def index(request):
    film_list = Film.objects.order_by('-rating')[:10]
    template = loader.get_template("films/index.html")
    context = {
        'film_list': film_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    film = get_object_or_404(Film, pk=id)
    template = loader.get_template("films/detail.html")
    context = {
        'film':film
    }
    return HttpResponse(template.render(context, request))
