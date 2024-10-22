from django.urls import path

from config import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    #    path('', views.welcome, name='welcome'),
    path('', MovieList.as_view(), name='movie-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
