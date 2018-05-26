from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from .models import Deputados, GastoMensal, Categorias
from django.views.decorators.csrf import ensure_csrf_cookie
import time
import datetime
import os


def gasto_mais_recente(deputado_id):
    """Retorna o ano e o mês dos gastos mais recentes cadastrados na base de dados

    Arguments:
        deputado_id {int} -- Id do deputado

    Returns:
        dict -- estrutura no formato {'ano': `{int}`, 'mes': `{int}` }.
    """
    data = GastoMensal.objects.filter(id_deputado = deputado_id)\
        .values('ano','mes')\
        .order_by('-ano')\
        .order_by('-mes')\
        .first()

    return data

def retorna_gastos(id_deputado, ano, mes):

    anos = range(2007, 2018)
    meses = range(1, 13)
    numeros_categorias = range(10, 16)
    dados_brutos = {}

    for _ano in anos:
        dados_brutos[str(_ano)] = {}
        for _mes in meses:
            dados_brutos[str(_ano)][str(_mes)] = {}
            for cat in numeros_categorias:
                dados_brutos[str(_ano)][str(_mes)][str(cat)] = {}

    # Utiliza dict_comprehension
    # (https://python-reference.readthedocs.io/en/latest/docs/comprehensions/dict_comprehension.html)
    gastos_mensal_por_categoria = { str(_mes):{} for _mes in meses }

    # Utiliza list_comprehension
    # (https://python-reference.readthedocs.io/en/latest/docs/comprehensions/list_comprehension.html)
    categorias = [ str(categoria) for categoria in numeros_categorias ]

    for (k, v) in gastos_mensal_por_categoria.items():
        for cat in categorias:
            gastos_mensal_por_categoria[k][cat] = {}

    for gasto in GastoMensal.objects.filter(id_deputado=id_deputado):
        dados_brutos[str(gasto.ano)][str(gasto.mes)][str(gasto.categoria.id_categoria)] = str(gasto.valor) if gasto.valor else '0'
        if str(gasto.ano) == str(ano):
            gastos_mensal_por_categoria[str(gasto.mes)][str(gasto.categoria.id_categoria)] = dados_brutos[str(gasto.ano)][str(gasto.mes)][str(gasto.categoria.id_categoria)]

    # Utiliza o unpacking (https://www.python.org/dev/peps/pep-3132/)
    aluguel_imoveis,\
    material_expediente,\
    locacao_software,\
    consultoria,\
    divulgacao,\
    hospedagem_locomocao = gastos_mensal_por_categoria[str(mes)].values()

    context = {
        'dados_brutos': dados_brutos,
        'gastos': gastos_mensal_por_categoria,
        'gasto_atual': {
            'aluguel_imoveis': aluguel_imoveis,
            'material_expediente': material_expediente,
            'locacao_software': locacao_software,
            'consultoria': consultoria,
            'divulgacao': divulgacao,
            'hospedagem_locomocao': hospedagem_locomocao
        }
    }

    return context


def DadosDeputadoView(request, mes=""):
    try:
        slug_deputado = request.POST.get('slug_deputado')
        ano = request.POST.get('ano')
        id_do_deputado = Deputados.objects.get(slug=slug_deputado).id_deputado
    except Exception as e:
        print(e)
        return HttpResponse('Não foi possível salvar informações.', status=401)

    data_mais_recente = gasto_mais_recente(id_do_deputado)

    if not ano:
        ano = data_mais_recente['ano']

    if not mes:
        mes = data_mais_recente['mes']

    gastos = retorna_gastos(id_do_deputado, ano, mes)

    return JsonResponse(gastos)

def IndexView(request, slug='', ano='', mes=''):

    todos_deputados = Deputados.objects.all().exclude(mandato_atual=False)
    context = {'deputados': todos_deputados}
    id_do_deputado = None

    try:

        deputado_atual = Deputados.objects.get(slug=slug)
        if slug != 'favicon.ico' and deputado_atual:
            id_do_deputado = deputado_atual.id_deputado
            context['deputado_atual'] = deputado_atual

    except Exception as e:
        deputado_atual = "Alba"

    try:
        print('===========a===========')
        if id_do_deputado:


            if not(ano) or not(mes):

                data_mais_recente = gasto_mais_recente(id_do_deputado)

                if not ano:
                    ano = data_mais_recente['ano']

                if not mes:
                    mes = data_mais_recente['mes']

            gastos = retorna_gastos(id_do_deputado, ano, mes)

            context['mes'] = datetime.datetime.strptime(str(mes), "%m").date()
            context['ano'] = ano
            context['gasto_atual'] = gastos['gasto_atual']
            context['gastos'] = gastos['gastos']

    except Exception as e:
        print(e)
        print('aqui')
        pass

    return render(request, "index.html", context)
