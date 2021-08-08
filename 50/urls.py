from django.urls import path

from . import views

urlpatterns = [
    path('1/', views.get_datetime, name='1'),
    path('2/', views.multiply, name='2'),
    path('3/', views.get_day, name='3')
]
