from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def Inicial(request):
    return render(request,"portafolioApp/index.html")

def Sobre_mi(request):
    return render(request,"portafolioApp/index.html")

def Proyect(request):
    return render(request,"portafolioApp/index.html")

def Skills(request):
    return render(request,"portafolioApp/index.html")

def Formacion(request):
    return render(request,"portafolioApp/index.html")

def Contacto(request):
    return render(request,"portafolioApp/index.html")
