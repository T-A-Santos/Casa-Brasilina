from django.urls import path, include
from .views import (
    home,
    add_customers,
    table,
    create_customers
)


urlpatterns = [
    path('', home, name='core_home'),
    path('table', table, name="core_tables"),
    path('add-cliente', add_customers, name="add_customers"),
    path('add-cliente/create', create_customers, name="create_customers"),
]
