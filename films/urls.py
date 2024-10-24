from django.urls import path

from config import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    #    path('', views.welcome, name='welcome'),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
