from django.db import models


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.country}" if self.city else self.country


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    origin = models.CharField(max_length=100)  # Место отправления
    destination = models.ForeignKey(Location, on_delete=models.CASCADE)  # Связь с локацией
    airline = models.CharField(max_length=100)  # Авиакомпания
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена билета
    departure_date = models.DateField()  # Дата вылета
    return_date = models.DateField(blank=True, null=True)  # Дата обратного вылета (если есть)
    created_at = models.DateTimeField(auto_now_add=True)  # Время добавления записи

    def __str__(self):
        return f"Ticket to {self.destination} from {self.origin} - {self.price}$"

