from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from Recetas.models import AuthUser
from Recetas.forms import UserCreationForm, registro, Buscarid, modificar
from django.contrib.auth.decorators import login_required
#from django.db.models import Q
from django.contrib import messages

def home(request):
    return render(request,'Recetas/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user:
            login(request, user)
            return redirect ('home')
        else:
            
            return render(request,'Recetas/Login.html', {'error':'Credenciales invalidas'})
    return render(request,'Recetas/Login.html')

def recetas(request):
    return render(request,'Recetas/Recetas.html')

def entradas(request):
    return render(request,'Recetas/Entradas.html')

def fondo(request):
    return render(request,'Recetas/Fondo.html')




def postres(request):
    return render(request,'Recetas/Postres.html')

def acerca(request):
    return render(request,'Recetas/Acerca.html')

def formulario(request):
    data = {
        'form': registro()
    }
    if request.method == 'POST':
        formulario = registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect ('home')
            messages.success(request, "Registrado Correctamente")
        else:
            messages.error(request, "Intente nuevamente")
            return redirect ('formulario')

    return render(request,'Recetas/formulario.html', data)

@login_required
def administracion(request):
    return render(request,'Recetas/Administracion.html')

@login_required
def eliminar_usuario(request, id):
    usuario = AuthUser.objects.get(username=id)
    usuario.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listado")

@login_required
def filtrar(request):
    busqueda = request.GET.get('buscar')
    usuario = AuthUser.objects.all()  
    data = {
        'user':usuario
    }
    if busqueda:
        usuario = AuthUser.objects.filter(
            Q(username__icontains = busqueda)
        ).distinct()
    return render(request, 'Recetas/Listado_usuario.html',{'usuario': usuario})

@login_required
def modificar_usuario(request, id):
    usuario = AuthUser.objects.get(username=id)
    data = {
        'form':modificar(instance=usuario)
    }
    if request.method == 'POST':
        formulario = modificar(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            data['form'] = formulario
            return redirect(to="listado")
    return render(request,'Recetas/modificar_usuario.html', data)
    