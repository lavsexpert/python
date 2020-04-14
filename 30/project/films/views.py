from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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
        'film':film,
        'range':range(0,10)
    }
    return HttpResponse(template.render(context, request))


def vote(request, id):
    film = get_object_or_404(Film, pk=id)
    try:
        selected_choice = request.POST['choice']
        film.rating = selected_choice
        film.save()
    except(KeyError):
        return HttpResponseRedirect(reverse('films:detail', args=(id,)))
    return HttpResponseRedirect(reverse('films:detail', args=(id,)))