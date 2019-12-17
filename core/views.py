from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.

def home(request):
    context = {'mensagem' : 'ola mundo'}
    return HttpResponse('Ola mundo')
    #return render(request, 'core/index.html', context)

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,
     'core/lista_clientes.html',
     {'clientes': clientes}
    )