from django import forms
from django.forms import ModelForm
from MobikeApp.models import Usuario, Comuna, Banco




class UsuarioForm(ModelForm):

    rut = forms.CharField(min_length=7,max_length=8, required=True, widget = forms.TextInput(attrs={'class':'form-control','placeholder': '24765434'}))
    rut_dv = forms.CharField(min_length=1,max_length=1, required=True  ,widget = forms.TextInput(attrs={'class':'form-control','placeholder': '0'}))
    tarjeta_credito = forms.CharField(min_length=16,max_length=16, required=True  ,widget = forms.TextInput(attrs={'class':'form-control','placeholder': '234567364573654'}))
    mes_expiracion = forms.CharField(min_length=2,max_length=2, required=True,label='Mes'  ,widget = forms.TextInput(attrs={'class':'form-control','placeholder': '07'}))
    anio_expiracion = forms.CharField(min_length=2,max_length=2, required=True,label='Año'  ,widget = forms.TextInput(attrs={'class':'form-control','placeholder': '20'}))
    


    class Meta:
        model = Usuario
        fields = [
        'rut',
        'rut_dv',
        'nombre',
        'apellido',
        'direccion',
        'comuna',
        'correo',
        'tarjeta_credito',
        'mes_expiracion',
        'anio_expiracion',
        'banco',
        'contrasena']#,'tipousuario'
        

        labels ={
                'rut':'Rut',
                'rut_dv':'-',
                'nombre':'Nombre',
                'apellido':'Apellido',
                'direccion':'Direccion',
                'comuna':'Comunas',
                'correo':'Correo',
                'tarjeta_credito':'Numero de Tarjeta',
                'mes_expiracion':'Mes',
                'anio_expiracion':'Año',
                'banco':'Banco',
                'contrasena':'Contraseña',
        }

        

        widgets = {
        	'rut' :forms.TextInput(attrs={'class':'form-control','placeholder': '24765434'}),
        	'rut_dv':forms.TextInput(attrs={'class':'form-control','placeholder': '0'}),
        	'nombre':forms.TextInput(attrs={'class':'form-control','placeholder': 'Juan Andres'}),
        	'apellido':forms.TextInput(attrs={'class':'form-control','placeholder': 'Vera Carvajal'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder': 'Carre 1464, santiago'}),
            'comuna':forms.Select(attrs={'class':'form-control', 'required':'required'}),
        	'correo':forms.TextInput(attrs={'class':'form-control','placeholder': 'ejemplo@gmail.com'}),
        	'tarjeta_credito':forms.TextInput(attrs={'class':'form-control','placeholder': '1234450987361543'}),
            'mes_expiracion':forms.TextInput(attrs={'class':'form-control','placeholder': '07'}),
            'anio_expiracion':forms.TextInput(attrs={'class':'form-control','placeholder': '20'}),
            'banco':forms.Select(attrs={'class':'form-control'}),
        	'contrasena':forms.PasswordInput(attrs={'class':'form-control','placeholder': 'juan123'})
        }



class Buscarid(ModelForm):

    class Meta:
        model = Usuario
        fields = ['rut']




class BancoForm(ModelForm):

    class Meta:
        model = Banco
        fields = ['nombre_banco']

class ComunaForm(ModelForm):
    class Meta:
        model = Comuna
        fields =['nombre_comuna']

        