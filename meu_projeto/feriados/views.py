from datetime import date
from django.shortcuts import render
from .models import Feriado


def feriado_hoje(request):
    hoje = date.today()
    feriado = Feriado.objects.filter(data=hoje).first()

    if feriado:
        mensagem = f"Hoje é {feriado.nome}"
    else:
        mensagem = "Hoje não é um feriado"

    contexto = {"mensagem": mensagem}
    return render(request, "feriados/feriado_hoje.html", contexto)
