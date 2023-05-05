from django.urls import path
from .views import lista_raza


urlpatterns = [
    path('lista', lista_raza, name="lista"),    
]