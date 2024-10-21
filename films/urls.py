from django.urls import path
from .views import *

urlpatterns = [
    #    path('', views.welcome, name='welcome'),
    path('', MovieList.as_view(), name='movie-list'),
]
