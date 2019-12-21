from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente

from .forms import ClienteForm
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def table(request):
    clientes = Cliente.objects.all()
    return render(request, 
    'core/tables.html',
    {'clientes': clientes}
    )

def add_customers(request):
    form = ClienteForm()
    return render(request, 'core/create_cliente.html', {'form': form})

def create_customers(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_tables')

