from django.db import models

# Create your models here.
class Base(models.Model):
    publicacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    
