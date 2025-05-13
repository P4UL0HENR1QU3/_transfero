from django.shortcuts import render, redirect
from produto.models import Produto
from produto.forms import ProdutoForm

def cadastroproduto(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('listar')  
    else:
        form = ProdutoForm()

        return render(
            request,
            'produtos/cadastro.html', 
            {'form': form},
        )

def listarproduto(request):
    produto = Produto.objects.all() 

    context = {
        'produto': produto,
    }

    return render(
        request,
        'produtos/listar.html',
        context,
        )
