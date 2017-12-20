from django.shortcuts import render
from django.http import HttpResponse
from .models import Deputados

def DeputadoView(request):
    print(request)
    return HttpResponse(request)

def IndexView(request, slug):
    print(request)
    todos_deputados = Deputados.objects.all()
    # if(request):
    #     deputado_atual = 'ALBA'
    # else:
    #     deputado_atual = 'Outro'
    print(request.GET)
    print(request.GET.get('q'))
    print('==========')

    context = {'deputados': todos_deputados,}
    return render(request, 'index.html', context)
