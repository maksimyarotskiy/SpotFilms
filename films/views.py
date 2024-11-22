from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView
from .models import Movie
from .models import *
from films.services.aviasales import get_tickets, get_iata_code


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

        # Получение параметров из GET-запроса
        origin_name = self.request.GET.get("origin", "Москва")
        destination_name = self.request.GET.get("destination", "Дубай")
        currency = self.request.GET.get("currency", "rub")  # Валюта
        sorting = self.request.GET.get("sorting", "price")  # Сортировка
        limit = int(self.request.GET.get("limit", 30))  # Лимит
        page = int(self.request.GET.get("page", 1))  # Страница
        one_way = self.request.GET.get("one_way", "true").lower() == "true"  # Только в одну сторону
        direct = self.request.GET.get("direct", "false").lower() == "true"  # Только прямые рейсы

        origin = get_iata_code(origin_name)
        destination = get_iata_code(destination_name)

        if not origin or not destination:
            context["error"] = "Не удалось найти IATA-коды для указанных городов."
            context["tickets"] = []
            return context

        # Получение данных о билетах
        tickets = get_tickets(
            origin=origin,
            destination=destination,
            currency=currency,
            sorting=sorting,
            limit=limit,
            page=page,
            one_way=one_way,
            direct=direct,
        )

        # Передача данных в контекст
        context.update({
            "tickets": tickets,
            "origin": origin,
            "destination": destination,
            "origin_name": origin_name,
            "destination_name": destination_name,
            "currency": currency,
            "sorting": sorting,
            "limit": limit,
            "page": page,
            "one_way": one_way,
            "direct": direct,
            "error": not tickets,
        })

        return context
