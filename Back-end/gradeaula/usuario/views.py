from typing import Any, Dict
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import InsereUsuarioForm, UsuarioLoginForm, criaNivel, criaMenu
from .models import Usuario,NivelAcesso, MenuEntrada
from datetime import date



def index(request):
      
    form = UsuarioLoginForm(request)
    context = {
        'form': form
    }
    if request.method == "GET":
        
        return render(request, 'usuario/index.html', context)
    elif request.method == "POST":    
        form = UsuarioLoginForm()              
        #if form.is_valid():   
        #             
        user = request.POST['usuario']        
        password = request.POST['senha']
        baseusuario = Usuario.objects.filter(usuario = user)
        
        basesenha = Usuario.objects.filter(senha = password)
        
        #confirmacao = authenticate(request, usuario=user, senha=password)
        
        #if form.is_valid():
            #login(request, confirmacao)
            
            #form = InsereUsuarioForm()
            # context = {
            #'form': form
            #}  
        print("primeiro aqui")
        if (baseusuario.first() and basesenha.first()):
            print("Depois aqui")
            return redirect('usuario/')
    return render(request, 'usuario/index.html')

@csrf_protect
def homeUsuario(request):
    if request.method == "GET":
        form = InsereUsuarioForm()
        context = {
            'form': form
        }
        render(request, 'usuario/CadastroUsuario.html', context)
    elif request.method == "POST": 
        novo_usuario = Usuario()
        nivelUsuario = NivelAcesso.objects.get(pk=10)      

        novo_usuario.nome = request.POST["nome"]
        novo_usuario.usuario = request.POST["usuario"]
        novo_usuario.senha = request.POST["senha"]
        novo_usuario.status = request.POST["status"]
        novo_usuario.inclusao = date.today()       
        

        baseusuario = Usuario.objects.filter(usuario = novo_usuario.usuario)       

        if (baseusuario.exists()):
            #messages.info(request, 'O respectivo usuário já existe!')
            messages.info(request, 'Nivel já existe')
        elif novo_usuario.nome == "" or novo_usuario.senha == "" or novo_usuario.usuario == "":
            messages.info(request, 'Por favor preencha todos os campos!')
        else:
            novo_usuario.save()
            novo_usuario.id_niveis.add(nivelUsuario)            
            print(novo_usuario.id_niveis)        

        return render(request, 'usuario/CadastroUsuario.html')
        
    return render(request, 'usuario/CadastroUsuario.html')


def cadastroNivel(request):
    if request.method == "POST": 
        novonivel = NivelAcesso()
        novonivel.ds_nivelAcesso = request.POST["nivel"]

        basenivel = NivelAcesso.objects.filter(ds_nivelAcesso = novonivel.ds_nivelAcesso)
        

        if (basenivel.exists()):
            messages.info(request, 'Nivel já existe')
        elif novonivel.ds_nivelAcesso == "":
            messages.info(request, 'Por favor insira o nome do nivel!')
        else:
            novonivel.save()
            return redirect('usuarios')
    
    elif request.method == "GET":
        form = criaNivel()
        context = {
            'form': form
        }
        return render(request, 'usuario/CadastroNivel.html', context)
    
    return redirect('niveisacesso')



def cadastroTela(request):
    if request.method == "GET":
        form = criaMenu()
        context = {
            'form': form
        }
        return render(request, 'usuario/CadastroMenu.html', context)

    elif request.method == "POST":
        novomenu = MenuEntrada()
        nivelMenu = NivelAcesso.objects.get(pk=10)

        novomenu.ds_MenuEntrada = request.POST['ds_menu']
        novomenu.nivel_MenuEntrada = request.POST['nivel_menu']
        novomenu.ordem = request.POST['ordem']
        novomenu.nomePagina = request.POST['nome']

        novomenu.save()
        novomenu.id_niveis.add(nivelMenu)

        return render(request, 'usuario/CadastroMenu.html', context)

    return redirect('cadastromenu')




def alteraUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    niveis_disponiveis = NivelAcesso.objects.all()
    niveis_selecionados = usuario.id_niveis.values_list('pk', flat=True)  # Obtém os IDs dos níveis selecionados

    if request.method == 'POST':
        niveis_selecionados_post = request.POST.getlist('nivel_acesso')

        # Remove todos os níveis de acesso existentes
        usuario.id_niveis.clear()

        print(niveis_selecionados)
        # Adiciona os novos níveis de acesso selecionados
        for nivel_id in niveis_selecionados_post:
            nivel = get_object_or_404(NivelAcesso, pk=nivel_id)
            usuario.id_niveis.add(nivel)

        # Atualiza os dados do usuário
        usuario.nome = request.POST["nome"]
        usuario.usuario = request.POST["usuario"]
        usuario.senha = request.POST["senha"]
        usuario.status = request.POST["status"]
        usuario.save()

        return redirect('usuarios')

    context = {
        'usuario': usuario,
        'niveis_disponiveis': niveis_disponiveis,
        'niveis_selecionados': niveis_selecionados,  # Passa os IDs dos níveis selecionados para o template
    }
    return render(request, 'usuario.html', context)



class usuarios(ListView):
    model = Usuario
    template = ''


class niveisAcesso(ListView):
    model = NivelAcesso
    template = ''


class Telas(ListView):
    model = MenuEntrada
    template = ''

