from django.shortcuts import render
from django.http import HttpResponse

def DeputadoView(request):

    return HttpResponse(request)

def IndexView(request):
    context = {'deputado':'bom'}
    return render(request, 'index.html', context)
