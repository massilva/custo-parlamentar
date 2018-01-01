from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Deputados, GastoMensal
import time

def DadosDeputadoView(request):
    # slug = request
    print("=============")
    print(request.POST.get('slug_deputado'))
    print(request.POST.get('ano'))
    try:
        slug_deputado = request.POST.get('slug_deputado')
        ano = request.POST.get('ano')
    except Exception as e:
        print(e)
        return HttpResponse('Não foi possível salvar informações.', status=401)

    deputado_id = Deputados.objects.get(slug=slug_deputado).id_deputado
    dados = GastoMensal.objects.filter(ano=str(ano), id_deputado=deputado_id)
    gastos = {}
    print(dados)
    for gasto in dados:
        i =  str(gasto.ano)+ "%02d" % (gasto.mes,)+str(gasto.id_categoria.id_categoria)
        gastos[i] = {}
        gastos[i]['id_categoria'] =  gasto.id_categoria.id_categoria
        gastos[i]['categoria'] = gasto.id_categoria.categoria
        gastos[i]['valor'] = str(gasto.valor)
    print(gastos)
    return JsonResponse({'gastos':gastos})

def IndexView(request, slug='', ano='', mes=''):
    todos_deputados = Deputados.objects.all().exclude(mandato_atual=False)
    context = {'deputados': todos_deputados}

    if ano == '' or mes == '':
        mes = time.strftime("%m")
        ano = time.strftime("%Y")
    try:
        if Deputados.objects.get(slug=slug) and slug != 'favicon.ico':
            deputado_atual = Deputados.objects.get(slug=slug)
            id_do_deputado = Deputados.objects.get(slug=slug).id_deputado
            context['deputado_atual'] = deputado_atual
    except Exception as e:
        deputado_atual = 'Alba'

    def retorna_valores_items(gastos_mes):
        gastos = {}
        for item in gastos_mes:
            i = item.id_categoria.id_categoria
            gastos[i] = {}
            gastos[i]['id_deputado'] = item.id_deputado
            gastos[i]['mes'] = item.mes
            gastos[i]['id_categoria'] = item.id_categoria.id_categoria
            gastos[i]['valor'] = str(item.valor)
            gastos[i]['ano'] = item.ano
        return gastos

    try:
        month = int(mes)
        year = int(ano)
    except Exception as e:
        #print(e)
        pass

    if deputado_atual != 'Alba' and ((type(month) == int and (month > 0 and month < 13)) and (type(year) == int and (year > 2007 and year < 2018))):
        # print('==========')
        gastos_mes = GastoMensal.objects.filter(ano=str(ano), mes=str(mes), id_deputado=id_do_deputado)
        gastos = retorna_valores_items(gastos_mes)
        # print(gastos)

    # elif deputado_atual == 'Alba':
    #     gastos_mes = GastoMensal.objects.filter(ano=ano_atual, mes=mes_atual, id_deputado=id_do_deputado)
    #     gastos = retorna_valores_items(gastos_mes)
    #     print(gastos)

    return render(request, 'index.html', context)
