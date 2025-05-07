from django.shortcuts import render, redirect
from filmes.forms import FilmeForm

# Create your views here.

def cadastrarFilme(request):
    # Verificar se a requisição será do tipo GET ou POST 
    if request.method ==  'POST':
        form = FilmeForm(request.POST)     
        #Será criado um objeto Usuario(model) com os dados enviados
        # post -> São os campos do forms (nome, sobrenome) preenchidos
        # files -> Contém os arquivos ou e/imagen
        if form.is_valid(): # Se os dados forem válidos, são salvos no BD.
            form.save()
            return redirect('filmes')
    
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        form = FilmeForm()

    return render(
        request,
        'cadastrar.html',
        {'form': form}
    )