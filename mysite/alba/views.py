from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Deputados, GastoMensal, Categorias
import time


def retorna_gastos(slug_deputado, ano):
    print(slug_deputado)
    print(ano)

    deputado_id = Deputados.objects.get(slug=str(slug_deputado)).id_deputado
    dados = GastoMensal.objects.filter(ano=str(ano), id_deputado=deputado_id)
    gastos = {}
    gastos[ano] = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}, '10': {}, '11': {}, '12': {}}
    categorias = ['10', '11', '12', '13', '14', '15']

    for(k, v) in gastos[ano].items():
        for cat in categorias:
            gastos[ano][k][cat] = {}

    for gasto in dados:
        gastos[ano][str(gasto.mes)][str(gasto.id_categoria.id_categoria)] = str(gasto.valor)

    print(gastos)

    return gastos

def DadosDeputadoView(request):

    try:
        slug_deputado = request.POST.get('slug_deputado')
        ano = request.POST.get('ano')
    except Exception as e:
        print(e)
        return HttpResponse('Não foi possível salvar informações.', status=401)
    gastos = retorna_gastos(slug_deputado, ano)

    return JsonResponse(gastos)

def IndexView(request, slug='', ano='', mes=''):
    todos_deputados = Deputados.objects.all().exclude(mandato_atual=False)
    context = {'deputados': todos_deputados}

    if ano == '' or mes == '':
        mes = time.strftime("%m")
        ano = time.strftime("%Y")
    try:
        if slug != 'favicon.ico' and Deputados.objects.get(slug=slug):
            deputado_atual = Deputados.objects.get(slug=slug)
            id_do_deputado = Deputados.objects.get(slug=slug).id_deputado
            context['deputado_atual'] = deputado_atual
    except Exception as e:
        deputado_atual = 'Alba'

    try:
        if slug != 'favicon.ico' and Deputados.objects.get(slug=slug):
            slug_deputado = slug
            context['gastos'] = retorna_gastos(slug_deputado, ano)
            print(retorna_gastos(slug_deputado, ano))
    except Exception as e:
        print(e)

    return render(request, 'index.html', context)
