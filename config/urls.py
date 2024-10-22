from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),  # здесь подключается urls для приложения films(пути писать там !!!!)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# !!! здесь писать listview НЕЛЬЗЯ , перейди в films/urls.py!!!