from django import forms # Importa o módulo dos formulários do django.
from sistema.models import Usuario

class UsuarioForm(forms.ModelForm):
    model = Usuario # Define qual é o model que o form representa.
    fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'imagem',] # São os campos que serão exibidos no form (HTML)