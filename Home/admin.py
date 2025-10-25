from django.contrib import admin
from django.utils.html import format_html

from Home.models import IndexSlider, IndexOfrecemos


# Register your models here.
@admin.register(IndexSlider)
class IndexSliderAdmin(admin.ModelAdmin):
    list_display = [
        'creado_en','actualizado_en','titulo','boton', 'enlace_boton','mostrar_imagen','estado'
    ]
    list_display_links = [
        'creado_en', 'actualizado_en', 'titulo'
    ]
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 5px;" />',
                obj.imagen.url
            )
        return "Sin imagen"

    mostrar_imagen.short_description = "Vista previa"

@admin.register(IndexOfrecemos)
class IndexOfrecemosAdmin(admin.ModelAdmin):
    list_display = [
        'creado_en', 'actualizado_en', 'titulo','estado','mostrar_imagen',
    ]
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 5px;" />',
                obj.imagen.url
            )
        return "Sin imagen"

    mostrar_imagen.short_description = "Vista previa"