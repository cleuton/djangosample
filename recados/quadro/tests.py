from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recado, Seguidor

class TesteIndex(TestCase):

    def teste(self):

        # Criando usuários:
        usuario1 = User.objects.create_user(username='usuario1', password='123456')
        usuario2 = User.objects.create_user(username='usuario2', password='123456')

        # Criando recados (2 para usuario1):
        recado1 = Recado.objects.create(titulo="titulo recado 1", \
                         texto="texto recado 1", 
                         autor=usuario1)
        recado2 = Recado.objects.create(titulo="titulo recado 2", \
                         texto="texto recado 2", 
                         autor=usuario1)
        
        # Fazendo usuario2 seguir usuario1: 
        seguindo = Seguidor.objects.create(usuario_seguidor=usuario2,usuario_seguido=usuario1)

        # Logando usuario2:
        login = self.client.login(username='usuario2', password='123456')

        # Invocando a view "index":
        response = self.client.get(reverse('index'))
        print(response.content)

        # Testando se a view do usuario2 tem os dois recados do usuario1:
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "titulo recado 1")
        self.assertContains(response, "titulo recado 2")


