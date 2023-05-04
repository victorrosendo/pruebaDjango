from django.urls import path
from .views import home, registrar, realizarregistro

urlpatterns = [
    path('', home, name="home"),
    path('registro',registrar,name="regis"),
    path('realizarregistro',realizarregistro,name="realizarregistro"),
]