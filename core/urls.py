from django.urls import path
from .views import home, registrar, realizarregistro, eliminarMascota, modificarMascota, mascotaModificar

urlpatterns = [
    path('', home, name="home"),
    path('registro',registrar,name="regis"),
    path('realizarregistro',realizarregistro,name="realizarregistro"),
    path('eliminar/<int:codigo>',eliminarMascota,name="eliminar"),
    path('modificar/<int:codigo>',modificarMascota,name="modificar"),
    path('mascotaModificar',mascotaModificar,name="mascotaModificar"),
]