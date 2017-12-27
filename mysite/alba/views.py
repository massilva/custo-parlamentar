from django.shortcuts import render
from django.http import HttpResponse
from .models import Deputados, GastoMensal
import datetime

def DeputadoView(request):
    return HttpResponse(request)

def IndexView(request, slug='', ano='', mes=''):
    todos_deputados = Deputados.objects.all().exclude(mandato_atual=False)
    context = {'deputados': todos_deputados}
    try:
        if Deputados.objects.get(slug=slug) and slug != 'favicon.ico':
            deputado_atual = Deputados.objects.get(slug=slug)
            id_do_deputado = Deputados.objects.get(slug=slug).id_deputado
            context['deputado_atual'] = deputado_atual
    except Exception as e:
        deputado_atual = 'Alba'

    if deputado_atual != 'Alba' and mes !='' and ano !='':
        gastos_mes = GastoMensal.objects.filter(ano=ano, mes=mes, id_deputado=id_do_deputado)
        for item in gastos_mes:
            print(str(item.id_categoria) + ' ' + str(item.valor))
            print(id_do_deputado)
    elif deputado_atual != 'Alba' and (mes =='' or ano ==''):
        gastos_mes = GastoMensal.objects.filter(ano=ano, mes=mes, id_deputado=id_do_deputado)

    return render(request, 'index.html', context)
