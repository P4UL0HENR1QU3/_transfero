from django.shortcuts import render

from sistema.models import Filme

def listarFilmes(request):
    filmes = Filme.objects.all()

    context = {
        'filmes': filmes,
    }

    return render(
        request,
        'filmes/listar.html',
        context, 
    )