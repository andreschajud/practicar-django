# Este lo hice yop como dijo el calvo de yt
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo_especial)
]
