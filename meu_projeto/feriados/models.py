from django.db import models

class Feriado(models.Model):
    nome = models.CharField(max_length=255)

class DataFeriado(models.Model):
    data = models.DateField()
    feriado = models.ForeignKey(Feriado, on_delete=models.CASCADE)
