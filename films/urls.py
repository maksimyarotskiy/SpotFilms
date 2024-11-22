from django.shortcuts import redirect
from django.urls import path

from config import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    #    path('', views.welcome, name='welcome'),
    path('', lambda request: redirect('movie-list', permanent=True)),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path("tickets/", TicketsListView.as_view(), name="tickets-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
