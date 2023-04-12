from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Feriado


class FeriadoHojeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("feriados:feriado_hoje")
        self.hoje = date.today()
        Feriado.objects.create(data=self.hoje, nome="Feriado de Teste")

    def test_feriado_hoje_com_feriado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hoje é Feriado de Teste")

    def test_feriado_hoje_sem_feriado(self):
        Feriado.objects.filter(data=self.hoje).delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hoje não é um feriado")
