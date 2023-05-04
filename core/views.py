from django.shortcuts import render,redirect
from .models import Mascota, Raza
from django.contrib import messages
# Create your views here.
def home(request):
    mascotas = Mascota.objects.all() #select * from Mascota;
    contexto = {"masc": mascotas}
    return render(request,'core/home.html',contexto)

def registrar(request):
    razas = Raza.objects.all()
    contexto = {"raza": razas}
    return render(request,'core/ingresarMascota.html',contexto)


def realizarregistro(request):
    chip_m = request.POST['chip']
    nombre_m = request.POST['nombre']
    edad_m = request.POST['edad']
    raza_m = request.POST['raza']

    #traer registro completo de la raza
    raza_c = Raza.objects.get(codigo = raza_m)

    #insert
    Mascota.objects.create(codigoChip = chip_m, nombreMascota =  nombre_m, edadMascota = edad_m, raza = raza_c)
    messages.success(request,'Mascota Registrada')
    return redirect('regis')
