from django.shortcuts import render
from .models import Contato


def home(request):
    return render(request,'website/index.html')

def promocoes(request):
    return render(request, 'website/promo.html')

def formContato(request):
    mensagem = ''
    if request.method == "POST":
        try:
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['email']= request.POST.get('email')
            contato['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contato)
        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = "contato realizado"
    return render(request, 'website/form.html', {'mensagem':mensagem})