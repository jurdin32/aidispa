from django.db import models

# Create your models here.
class IndexSlider(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    imagen=models.ImageField(upload_to='slider', help_text='imagen de 1920 x 1080')
    titulo=models.CharField(max_length=100, null=True,blank=True)
    boton=models.CharField(max_length=30,null=True,blank=True)
    enlace_boton=models.TextField(blank=True, null=True)
    estado=models.BooleanField(default=True)
