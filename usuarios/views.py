from django.shortcuts import render, redirect
from sistema.models import Usuario
from usuarios.forms import UsuarioForm

# Create your views here.

def login(request):
    return render(
        request,
        'login.html'
    )

def criarUsuario(request):
    # Verificar se a requisição será do tipo GET ou POST 
    if request.method ==  'POST':
        form = UsuarioForm(request.POST, request.FILES)     
        #Será criado um objeto Usuario(model) com os dados enviados
        # post -> São os campos do forms (nome, sobrenome) preenchidos
        # files -> Contém os arquivos ou e/imagen
        if form.is_valid(): # Se os dados forem válidos, são salvos no BD.
            form.save()
            return redirect('/usuario/login')
    
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        form = UsuarioForm()

    return render(
        request,
        'cadastro.html',
        {'form': form}
    )


def cadastrarUsuario(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)     
        if form.is_valid(): 
            form.save()
            return redirect('listarusuarios')
    else:
        form = UsuarioForm()

    return render(
        request,
        'usuarios/cadastro.html',
        {'form': form},
    )

def listarUsuarios(request):
    usuarios = Usuario.objects.all() 

    context = {
        'usuarios': usuarios,
    }

    return render(
        request,
        'usuarios/listar.html',
        context,
    )