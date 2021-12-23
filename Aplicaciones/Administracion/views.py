from django.shortcuts import redirect, render
from .models import Turno

def home(request):
    turnosListados = Turno.objects.all().order_by('id')
    turnosListados = Turno.objects.filter(estado='ACT') 
    return render(request,"listadoturnos.html", {"turnos": turnosListados})


def registrarTurno(request):
    nombres=request.POST['txtNombre']
    tipodocumento=request.POST['txtTipoDocumento']
    documento=request.POST['numNumerodeDocumento']
    imagen=request.FILES['txtImagen']
    
    turno = Turno.objects.create(nombres=nombres, tipodocumento=tipodocumento, documento=documento, imagen=imagen)
    return redirect('/')


def home2(request):
    turnosListados = Turno.objects.all
    return render(request,"solicitarturnos.html")
