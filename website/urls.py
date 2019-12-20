from django.urls import path, include
from .views import home, promocoes, formContato


urlpatterns = [
    path('', home, name='website_home'),
    path('promocoes/', promocoes, name='website_promo'),
    path('contact/', formContato, name="website_contato")
]