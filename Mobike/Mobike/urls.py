
from django.urls import path, include
from django.contrib import admin
from MobikeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('login/', views.login_usuario, name='Login'),
    path('registro/', views.registrate, name='Registro'),
    path('modificar/<id>/', views.modificar_usuario, name='Modificar'),
    path('eliminar_usuario/<id>/', views.eliminar_usuario, name='Eliminar_usuario'),
    path('home_sesion/', views.home_sesion, name='Home_sesion'),
    path('administracion/',views.administracion,name='Administracion'),
]
