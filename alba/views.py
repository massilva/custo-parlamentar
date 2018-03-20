from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from .models import Deputados, GastoMensal, Categorias
import time
import os


def gasto_mais_recente(deputado_id):
    ano = 0
    mes = 0
    data = {}
    for gasto in GastoMensal.objects.filter(id_deputado = deputado_id):
        if gasto.ano > ano:
            ano = gasto.ano
        if gasto.mes > mes:
            mes = gasto.mes

    data['ano'] = ano
    data['mes'] = mes
    
    return(data)

def retorna_gastos(id_deputado, ano, mes):
    # # print(deputado_id)
    # print(ano)
    # print(mes)
    # # print(type(ano))
    # # print(type(mes))
    # print(id_deputado)
    dados = GastoMensal.objects.filter(ano=str(ano), id_deputado=id_deputado)
    # print(dados)
    gastos = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}, '10': {}, '11': {}, '12': {}}
    # print(gastos)

    categorias = ['10', '11', '12', '13', '14', '15']

    for(k, v) in gastos.items():
        for cat in categorias:
            gastos[k][cat] = {}

    for gasto in dados:
        gastos[str(gasto.mes)][str(gasto.id_categoria.id_categoria)] = str(gasto.valor)

    print(gastos)
    aluguel_imoveis = gastos[mes]['10']
    material_expediente = gastos[mes]['11']
    locacao_software = gastos[mes]['12']
    consultoria = gastos[mes]['13']
    divulgacao = gastos[mes]['14']
    hospedagem_locomocao = gastos[mes]['15']
    context = {'gastos': gastos, 'gasto_atual':[aluguel_imoveis, material_expediente, locacao_software, consultoria, divulgacao, hospedagem_locomocao]}
    
    return context

def DadosDeputadoView(request):
    try:
        slug_deputado = request.POST.get('slug_deputado')
        ano = request.POST.get('ano')
    except Exception as e:
        print('aca')
        print(e)
        return HttpResponse('Não foi possível salvar informações.', status=401)
    gastos = retorna_gastos(slug_deputado, ano)

    return JsonResponse(gastos['gastos'])

def IndexView(request, slug='', ano='', mes=''):
    todos_deputados = Deputados.objects.all().exclude(mandato_atual=False)
    context = {'deputados': todos_deputados}
    try:
        if slug != 'favicon.ico' and Deputados.objects.get(slug=slug):
            deputado_atual = Deputados.objects.get(slug=slug)
            id_do_deputado = Deputados.objects.get(slug=slug).id_deputado
            context['deputado_atual'] = deputado_atual
    except Exception as e:
        deputado_atual = 'Alba'

    try:
        if slug != 'favicon.ico' and Deputados.objects.get(slug=slug):        
            # print('-------')
            # print(ano)
            # print(mes)
            data_mais_recente = gasto_mais_recente(id_do_deputado)
            if ano == '':
                ano = data_mais_recente['ano']
            if mes == '':
                mes = data_mais_recente['mes']    
            # print('&&&&&&&')
            # print(ano)
            # print(mes)
            gastos = retorna_gastos(id_do_deputado, ano, mes)
            # print('=======')
            # print(gastos)
            # print('+++++++')
            context['gastos'] = gastos['gastos']
            
    except Exception as e:
        print('aqui')

    return render(request, 'index.html', context)
