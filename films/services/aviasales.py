import requests
from django.conf import settings

AVIASALES_API_V3_URL = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

def get_tickets(origin, destination, currency="rub", sorting="price", limit=30, page=1, one_way=True, direct=False):
    """
    Получение билетов с использованием Aviasales API (v3).

    :param origin: Код аэропорта вылета (например, 'MOW').
    :param destination: Код аэропорта назначения (например, 'DXB').
    :param currency: Валюта (по умолчанию 'rub').
    :param sorting: Сортировка (по умолчанию 'price').
    :param limit: Лимит результатов (по умолчанию 30).
    :param page: Номер страницы (по умолчанию 1).
    :param one_way: Только в одну сторону (True/False).
    :param direct: Только прямые рейсы (True/False).
    :return: Список билетов или пустой список при ошибке.
    """
    headers = {"Accept": "application/json"}
    params = {
        "origin": origin,
        "destination": destination,
        "currency": currency,
        "sorting": sorting,
        "limit": limit,
        "page": page,
        "one_way": str(one_way).lower(),
        "direct": str(direct).lower(),
        "unique": "false",
        "token": settings.AVIASALES_API_KEY,
    }

    try:
        response = requests.get(AVIASALES_API_V3_URL, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return []
