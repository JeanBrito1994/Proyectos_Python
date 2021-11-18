from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from MobikeApp.models import Usuario, Funcionario, Administrador, Comuna
from MobikeApp.forms import UsuarioForm, Buscarid
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,"MobikeApp/index.html")


def login_usuario(request):
    if request.method == "POST":
        correo = request.POST['correo']
        contraseña = request.POST['contrasena']
        admin = Administrador.objects.filter(
            Q(correo = correo) & Q(contrasena = contraseña) & Q(tipousuario_admin = 1))

        usuario = Usuario.objects.filter(
            Q(correo = correo) & Q(contrasena = contraseña) & Q(tipousuario = 2))

        if admin:
            return redirect(to='Administracion')
            pass
        if usuario:
            return redirect(to= 'Home_sesion')
        else:
            messages.warning(request, 'Correo o contraseñas invalidas')
            pass
    return render(request,"MobikeApp/login.html")


def login_funcionario(request):
    if request.method == "POST":
        rut = request.POST['rut']
        contrasena = request.POST['contrasena_funcionario']
        funcionario = Funcionario.objects.filter(
            Q(rut = rut) & Q(contrasena = contrasena) & Q(tipousuario = 3))
        if funcionario:
            return redirect(to= 'Home_funcionario')
            pass
        else:
            messages.error(request, "Correo o contrasena invalidas")
        pass
    return render(request, "MobikeApp/home_funcionario.html")




def registrate(request):
    data = {
        'form':UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario ingresado con exito')
            return redirect(to="Login")
        else:
            pass
            messages.danger(request, 'Error no se ha podido guardar el usuario')
    return render(request,"MobikeApp/registro.html", data)



def modificar_usuario(request, id):
    usuario = Usuario.objects.get(rut=id)
    data = {
        'form':UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
    return render(request,"MobikeApp/modificar_usuario.html", data)

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(rut=id)
    usuario.delete()
    return redirect(to="Administracion")



def administracion(request):
    busqueda = request.GET.get('buscar')
    usuario = Usuario.objects.all()  
    data = {
        'usuario':usuario
    }
    if busqueda:
        usuario = Usuario.objects.filter(
            Q(rut__icontains = busqueda)|
            Q(nombre__icontains = busqueda)
        ).distinct()
    return render(request, "MobikeApp/administracion.html",{'usuario': usuario})



def home_sesion(request):
    return render(request, "MobikeApp/home_sesion.html")

