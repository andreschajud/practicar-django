from django.shortcuts import render
# De aquí para abajo lo hice yo siguiendo el tutorial del
# Calvo gringo de yt
# Create your views here.
from django.http import HttpResponse

# Voy a hacer una función que diga "olaaa caracolaa camaron sin cola"

def saludo_especial(request):
    return render(request, 'hello.html', {'name': 'Chajud'})
