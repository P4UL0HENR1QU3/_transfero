from django.utils import timezone
from django.db import models

# Aqui vai ficar a classe modelo do Usuário
# nome, sobrenome, cpf, telefone, email, foto, endereço.
#data_cadastro, ativo
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # foto = 