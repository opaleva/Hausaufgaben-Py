from django.http import HttpResponse
from datetime import datetime


def get_datetime(request):
    now = datetime.now()
    return HttpResponse(f"{now.strftime('%d-%m-%Y %H:%M')}")


def multiply(request):
    return HttpResponse(["_____".join([f'{x} * {y} = {x * y} ' for x in range(1, 11)]) for y in range(1, 11)])


def get_day(request):
    year = datetime.now().year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return HttpResponse("В этом году день программиста – 12 сентября.")
    else:
        return HttpResponse("В этом году день программиста – 13 сентября.")
