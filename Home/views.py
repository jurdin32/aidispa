from django.shortcuts import render

from Home.models import IndexSlider, IndexOfrecemos, IndexLineaProductos


# Create your views here.
def index(request):

    contexto={
        'slider':IndexSlider.objects.filter(estado=True).order_by('-creado_en'),
        'ofrecemos':IndexOfrecemos.objects.filter(estado=True),
        'lineaProductos':IndexLineaProductos.objects.filter(estado=True),
    }
    return render(request,'index.html',contexto)

def contact(request):
    return render(request,'contact.html')