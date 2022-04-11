from django.db import models

class Recado(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    data = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(default='*')
    autor = models.ForeignKey('auth.User', related_name='recados', 
        on_delete=models.CASCADE)

class Seguidor(models.Model):
    usuario_seguidor = models.ForeignKey('auth.User', related_name='+', 
        on_delete=models.CASCADE)
    usuario_seguido = models.ForeignKey('auth.User', related_name='+', 
        on_delete=models.CASCADE)