from django.db import models

# Create your models here.

class Peso_marte(models.Model): 

    nombre= models.CharField( max_length=20)
    apellido= models.CharField(max_length=20)
    peso= models.FloatField()

    def peso_marte(self, pesoM):
        tu_peso_en_marte = (pesoM * 3.72) / 9.80

        return tu_peso_en_marte