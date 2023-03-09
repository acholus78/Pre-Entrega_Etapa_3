from django.shortcuts import render
from AppCoder.models import Producto, Cliente, Proveedor
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario, ClienteFormulario, ProveedorFormulario


# Create your views here. Prueba de actualización

def inicio (request):
    #return HttpResponse ("Vista Inicio")
    return render (request, 'inicio.html')

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
    return render(request, 'productos.html', {'miFormulario': miFormulario})


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


