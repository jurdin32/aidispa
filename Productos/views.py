from django.shortcuts import render

from Productos.models import Producto, ProductoPagina


# Create your views here.
def productos(request, id):
    producto=Producto.objects.get(id=id)
    contexto={
        'productos':Producto.objects.all(),
        'items':ProductoPagina.objects.filter(producto=producto),
    }
    print(ProductoPagina.objects.filter(producto=producto))
    return render(request, 'paginas_datos.html',contexto)