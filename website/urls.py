from django.urls import path, include
from .views import home, promocoes, formContato


urlpatterns = [
    path('', home, name="website_home"),
    path('promocoes', promocoes, name="website_promo"),
    path('contato', formContato, name="website_contact")
]