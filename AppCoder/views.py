from django.shortcuts import render
from AppCoder.models import Producto, Cliente, Proveedor
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario, ClienteFormulario, ProveedorFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppCoder.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here. Prueba de actualización

#class ClaseQueNecesitaLogin (LoginRequiredMixin):


@login_required
def inicio (request):
    return render(request, 'inicio.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid ():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get ('password')

            user = authenticate (username = usuario, password = contras)
            if user is not None:
                login (request, user)
                return render (request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render (request, 'inicio.html', {"mensaje":"Error, datos incorrectos."})
        else:
            return render (request, 'inicio.html', {"mensaje":"Error, formulario erroneo."})

    form = AuthenticationForm()
    return render (request, 'login.html', {"form":form})


def register (request):
    if request.method == 'POST':
        #form = UserCreationForm (request.POST)
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render (request, 'inicio.html', {'mensaje': 'Usuario creado. '})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm ()
    return render (request, 'registro.html', {'form': form} )     









#def inicio (request):
    #return HttpResponse ("Vista Inicio")
#    return render (request, 'inicio.html')

def entregables (request):
    #return HttpResponse ("Vista Entregables")
    return render (request, 'entregables.html')  

def productos (request):
    if request.method == 'POST':
        
        miFormulario = ProductoFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto=Producto(nombre=informacion['nombre'],anio_fabricacion=informacion['anio_fabricacion'],descripcion=informacion['descripcion'],precio=informacion['precio'])
            producto.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProductoFormulario()

    miFormulario = ProductoFormulario()
    return render(request, 'Productos.html', {'miFormulario': miFormulario})


def clientes (request):
    if request.method == 'POST':
        
        miFormulario = ClienteFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],direccion=informacion['direccion'] )
            cliente.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()

    miFormulario = ClienteFormulario()
    return render(request, 'clientes.html', {'miFormulario': miFormulario})

def clienteFormulario (request):
    if request.method == 'POST':
        
        miFormulario = ClienteFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],
                            apellido=informacion['apellido'],
                            email=informacion['email'],
                            direccion=informacion['direccion'])
            cliente.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()

    miFormulario = ClienteFormulario()
    return render(request, 'clienteFormulario.html', {'miFormulario': miFormulario})



def proveedores (request):
    if request.method == 'POST':
        
        miFormulario = ProveedorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proveedor=Proveedor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            proveedor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProveedorFormulario()

    miFormulario = ProveedorFormulario()
    return render(request, 'proveedores.html', {'miFormulario': miFormulario})


def proveedorFormulario (request):
    if request.method == 'POST':
        
        miFormulario = ProveedorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proveedor = Proveedor(nombre=informacion['nombre'],
                                  apellido=informacion['apellido'],
                                  email=informacion['email'])
            proveedor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProveedorFormulario()

    miFormulario = ProveedorFormulario()
    return render(request, 'proveedorFormulario.html', {'miFormulario': miFormulario})



def busquedaProducto(request):
    return render (request, 'busquedaProducto.html')


def buscar (request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        producto = Producto.objects.filter(nombre__icontains=nombre)

        return render(request, 'inicio.html', {"productos":producto, "nombre":nombre}) 
    else:
        respuesta = "No enviaste datos."
        
    #return HttpResponse (respuesta)
    return render (request, 'inicio.html', {"respuesta":respuesta})


def leerProductos (request):
    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render(request, "LeerProductos.html", contexto)



def eliminarProducto (request, producto_nombre):
    producto = Producto.objects.get (nombre=producto_nombre)
    producto.delete()

    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render (request, "leerProductos.html", contexto)


def editarProducto (request, producto_nombre):
    producto = Producto.objects.get(nombre=producto_nombre)
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto.nombre = informacion ['nombre']
            producto.anio_fabricacion = informacion ['anio_fabricacion']
            producto.descripcion = informacion ['descripcion']
            producto.precio = informacion ['precio']

            producto.save()
            #return render(request, "inicio.html")
            contexto = {"productos":Producto.objects.all()}
            return render(request, "leerProductos.html", contexto )
    else:
        miFormulario = ProductoFormulario(initial={'nombre': producto.nombre, 
                                                   'anio_fabricacion': producto.anio_fabricacion, 
                                                   'descripcion': producto.descripcion, 
                                                   'precio': producto.precio})
        return render(request, "editarProducto.html", {"miFormulario": miFormulario, "producto_nombre": producto_nombre})


class ClienteList (ListView):
    model = Cliente
    template_name = "cliente_list.html"

class ClienteDetalle (DetailView):
    model = Cliente
    template_name = "cliente_detalle.html"

class ClienteCreacion (CreateView):
    model = Cliente
    template_name = "clientes_form.html"
    success_url = reverse_lazy ("AppCoder:List")
    fields = ['nombre','apellido', 'email', 'direccion']

class ClienteUdpdate (UpdateView):
    model = Cliente
    success_url = "AppCoder/cliente/List"
    template_name = "clientes_form.html"
    fields = ['nombre','apellido', 'email', 'direccion']


class ClienteDelete (DeleteView):
    model = Cliente
    template_name = "cliente_confirm_delete.html"
    success_url = "AppCoder/cliente/List"



def leerProveedores (request):
    proveedores = Proveedor.objects.all()
    contexto = {"proveedores":proveedores}
    return render(request, "leerProveedores.html", contexto)



def eliminarProveedor (request, proveedor_nombre):
    proveedor = Proveedor.objects.get(nombre=proveedor_nombre)
    proveedor.delete()

    proveedores = Proveedor.objects.all()
    contexto = {"proveedores":proveedores}
    return render (request, "leerProveedores.html", contexto)


def editarProveedor (request, proveedor_nombre):
    proveedor = Proveedor.objects.get(nombre=proveedor_nombre)
    if request.method == 'POST':
        miFormulario = ProveedorFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            proveedor.nombre = informacion ['nombre']
            proveedor.apellido = informacion ['apellido']
            proveedor.email = informacion ['email']
            
            proveedor.save()
            #return render(request, "inicio.html")
            contexto = {"proveedores":Proveedor.objects.all()}
            return render(request, "leerProveedores.html", contexto)
    else:
        miFormulario = ProveedorFormulario(initial={'nombre': proveedor.nombre, 
                                                   'apellido': proveedor.apellido, 
                                                   'email': proveedor.email})
        return render(request, "editarProveedor.html", {"miFormulario": miFormulario, "proveedor_nombre": proveedor_nombre})
    




    
def leerClientes (request):
    clientes = Cliente.objects.all()
    contexto = {"clientes":clientes}
    return render(request, "leerClientes.html", contexto)



def eliminarCliente (request, cliente_nombre):
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()

    clientes = Cliente.objects.all()
    contexto = {"clientes":clientes}
    return render (request, "leerClientes.html", contexto)


def editarCliente (request, cliente_nombre):
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cliente.nombre = informacion ['nombre']
            cliente.apellido = informacion ['apellido']
            cliente.email = informacion ['email']
            cliente.direccion = informacion ['direccion']
            
            cliente.save()
            #return render(request, "inicio.html")
            contexto = {"clientes":Cliente.objects.all()}
            return render(request, "leerClientes.html", contexto)
    else:
        miFormulario = ClienteFormulario(initial={'nombre': cliente.nombre, 
                                                   'apellido': cliente.apellido, 
                                                   'email': cliente.email,
                                                   'direccion': cliente.direccion})
        return render(request, "editarCliente.html", {"miFormulario": miFormulario, "cliente_nombre": cliente_nombre})