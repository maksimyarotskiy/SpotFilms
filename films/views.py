from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView
from .models import Movie
from .models import *
from films.services.aviasales import get_tickets


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


class TicketsListView(TemplateView):
    template_name = "films/tickets_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        origin = self.request.GET.get("origin", "MOW")  # Код вылета (по умолчанию Москва)
        destination = self.request.GET.get("destination", "DXB")  # Код назначения

        tickets = get_tickets(origin, destination)

        context["tickets"] = tickets
        context["origin"] = origin
        context["destination"] = destination

        return context
