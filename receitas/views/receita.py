from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from receitas.models import Receita  # importando a classe Receita de models.py
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jinja2 import Template


# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)  # acessando tudo de Receita
    paginator = Paginator(receitas, 3)  # exibe 3 receitas por pagina
    page = request.GET.get('page')  # identifica a pagina no momento da navegacao
    receitas_por_pagina = paginator.get_page(page)  # define as receitas por pagina

    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, 'receitas/index.html', dados)  # aponta para o arquivo 'index.html'


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)  # pegar obj do id

    # passando informacao pra pagina
    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_a_exibir)


def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)  # acessando tudo de Receita

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes,
                                         modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento,
                                         categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria-receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'receitas/edita-receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']  # pega a receita referente ao ID
        r = Receita.objects.get(pk=receita_id)  # receita que se quer editar
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.rendimento = request.POST['rendimento']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.categoria = request.POST['categoria']

        if 'foto_receita' in request.FILES:  # verifica se tem foto
            r.foto_receita = request.FILES['foto_receita']

        r.save()

        return redirect('dashboard')
