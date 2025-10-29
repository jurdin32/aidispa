from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Producto(models.Model):
    nombre=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nombre.upper()


class ProductoPagina(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE,)
    datos_pagina=CKEditor5Field('contenido',null=True,blank=True, config_name='default')

