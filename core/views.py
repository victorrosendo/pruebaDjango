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


def eliminarMascota(request, codigo):
    mascota1 = Mascota.objects.get(codigoChip = codigo) #obtengo la mascota a eliminar
    mascota1.delete() #elimina el registro obtenido de la BD
    messages.success(request, 'Mascota Eliminada')

    return redirect('home')

def modificarMascota(request,codigo):
    mascota2 = Mascota.objects.get(codigoChip = codigo)#obtengo la mascota a modificar
    raza1 = Raza.objects.all() #obtengo todas las razas

    contexto = {
        "mascota" : mascota2,
        "razas" : raza1
    }

    return render(request,'core/modificarMascota.html',contexto)

def mascotaModificar(request):
    chip_m = request.POST['chip']
    nombre_m = request.POST['nombre']
    edad_m = request.POST['edad']
    raza_m = request.POST['raza']

    #traer registro completo de la raza
    raza_c = Raza.objects.get(codigo = raza_m)

    #buscar el registro original
    mascota = Mascota.objects.get(codigoChip = chip_m)
    #reemplazo por los valores nuevos
    mascota.nombreMascota = nombre_m
    mascota.edadMascota = edad_m
    mascota.raza = raza_c

    #update
    mascota.save()
    messages.success(request, 'Mascota Eliminada')

    return redirect('home')
    