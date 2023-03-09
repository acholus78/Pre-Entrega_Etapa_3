from django import forms


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


    