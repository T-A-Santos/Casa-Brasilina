from django.urls import path, include
from .views import home,lista_clientes


urlpatterns = [
    path('', home, name='core_home'),
    path('clientes/', lista_clientes, name="core_lista_clientes")
]
