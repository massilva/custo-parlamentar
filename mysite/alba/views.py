from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Deputados, GastoMensal, Categorias
import time


def retorna_gastos(slug_deputado, ano, mes=''):

    deputado_id = Deputados.objects.get(slug=str(slug_deputado)).id_deputado
    dados = GastoMensal.objects.filter(ano=str(ano), id_deputado=deputado_id)
    gastos = {}
    gastos = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}, '10': {}, '11': {}, '12': {}}
    # gastos[ano] = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}, '10': {}, '11': {}, '12': {}}
    categorias = ['10', '11', '12', '13', '14', '15']

    for(k, v) in gastos.items():
        for cat in categorias:
            gastos[k][cat] = {}

    for gasto in dados:
        gastos[str(gasto.mes)][str(gasto.id_categoria.id_categoria)] = str(gasto.valor)

    if mes == '':
        mes = time.strftime("%m")

    print('____________')
    print(ano)

    if ano == '':
        print('==========')
        ano_mais_recente = GastoMensal.objects.all()
        print(ano_mais_recente)
        ano = time.strftime("%Y")
        

    print('a')
    print(gastos[mes])


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

    #if ano == '' or mes == '':
    #    mes = time.strftime("%m")
    #    ano = time.strftime("%Y")

    print(type(ano))
    print(type(mes))
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
            gastos = retorna_gastos(slug_deputado, ano, mes)
            context['gastos'] = gastos['gastos']


    except Exception as e:
        print('aqui')
        print(e)

    return render(request, 'index.html', context)
