from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Movie
from .models import *


# def welcome(request):
#     return HttpResponse("Welcome to the hell")

class MovieList(ListView):
    model = Movie
    template_name = 'films/movies_list.html'
    context_object_name = 'movies'
    paginate_by = 10

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'films/movie_detail.html'  # Указываем путь к шаблону
    context_object_name = 'movie'  # Название переменной для объекта в шаблоне