from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),  # здесь подключается urls для приложения films(пути писать там !!!!)
]

# !!! здесь писать listview НЕЛЬЗЯ , перейди в films/urls.py!!!