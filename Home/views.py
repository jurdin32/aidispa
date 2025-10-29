from django.shortcuts import render

from Home.models import IndexSlider, IndexOfrecemos, IndexLineaProductos, IndexCertificaciones
from Productos.models import Producto


# Create your views here.
def index(request):

    contexto={
        'slider':IndexSlider.objects.filter(estado=True).order_by('-creado_en'),
        'ofrecemos':IndexOfrecemos.objects.filter(estado=True),
        'lineaProductos':IndexLineaProductos.objects.filter(estado=True),
        'certificaciones':IndexCertificaciones.objects.filter(estado=True),
        'productos':Producto.objects.all(),

    }
    return render(request,'index.html',contexto)

def contact(request):
    contexto={
        'productos': Producto.objects.all(),
    }
    return render(request,'contact.html',contexto)