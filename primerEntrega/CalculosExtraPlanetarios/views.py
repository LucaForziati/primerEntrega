from django.shortcuts import render

from .models import Peso_marte

# Create your views here.
def calculo_peso_marte(request, peso):

    mi_peso_marte = Peso_marte.objects.all()

    return render(request, 'marte.html' )