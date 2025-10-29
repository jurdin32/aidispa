from django.contrib import admin

from Productos.models import Producto, ProductoPagina


# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(ProductoPagina)
class ProductoPaginaAdmin(admin.ModelAdmin):
    list_display = ['producto','datos_pagina']

    class Media:
        css = {
            'all': ('css/ckeditor_word_style.css',)  # ruta desde static
        }