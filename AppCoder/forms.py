from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    anio_fabricacion = forms.IntegerField()
    descripcion = forms.CharField(max_length=50)
    precio = forms.CharField(max_length=50)


class ProveedorFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    

class ClienteFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=30)


class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
