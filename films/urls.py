from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
]

# Здесь будешь писать свой listview