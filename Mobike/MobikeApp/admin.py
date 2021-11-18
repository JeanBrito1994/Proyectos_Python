from django.contrib import admin
from .models import Tipousuario, Usuario, Administrador, Funcionario, Comuna, Banco
 #Register your models here.
admin.site.register(Tipousuario)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Funcionario)
admin.site.register(Comuna)
admin.site.register(Banco)