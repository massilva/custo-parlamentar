from django.shortcuts import render
from django.http import HttpResponse
from .models import Deputados

def DeputadoView(request):
    print(request)
    return HttpResponse(request)

def IndexView(request, slug=''):
    todos_deputados = Deputados.objects.all()
    try:
        deputado_atual = Deputados.objects.get(slug=slug)
    except Exception as e:
        deputado_atual = 'Alba'
        print(e)

    context = {'deputados': todos_deputados,'deputado_atual': deputado_atual}
    return render(request, 'index.html', context)
