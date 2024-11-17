import requests
from django.conf import settings

AVIASALES_API_URL = "https://api.travelpayouts.com/v2/prices/latest"

def get_tickets(origin, destination, currency="usd"):
    """
    Функция для получения информации о билетах.

    :param origin: Код аэропорта вылета (например, 'MOW' для Москвы).
    :param destination: Код аэропорта назначения (например, 'NYC' для Нью-Йорка).
    :param currency: Валюта (по умолчанию 'usd').
    :return: Список билетов.
    """
    headers = {"Accept": "application/json"}
    params = {
        "origin": origin,
        "destination": destination,
        "currency": currency,
        "token": settings.AVIASALES_API_KEY,
    }

    try:
        response = requests.get(AVIASALES_API_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        print(data)


        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []
