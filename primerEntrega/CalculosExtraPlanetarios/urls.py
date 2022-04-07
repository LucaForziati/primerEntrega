from django.urls import path
from CalculosExtraPlanetarios import views


urlpatterns = [
    path('marte/', views.calculo_peso_marte),
]
