from django.shortcuts import render

from Home.models import IndexSlider


# Create your views here.
def index(request):
    slider=IndexSlider.objects.filter(estado=True).order_by('-creado_en')
    contexto={
        'slider':slider,
    }
    return render(request,'index.html',contexto)

def contact(request):
    return render(request,'contact.html')