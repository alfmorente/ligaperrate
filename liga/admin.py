from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.urls import path
from .models import Equipos,Partidos,Jornadas
from django.contrib.admin.views.decorators import staff_member_required



# admin.site.register(Equipos)
@admin.register(Equipos)
class EquiposAdmin(admin.ModelAdmin):
    actions = None
    ordering = ('nombre',)
    exclude = ('partidos_ganados','partidos_perdidos','partidos_empatados','puntos_favor','puntos_contra',)

admin.site.register(Partidos)

class PartidosInline(admin.TabularInline):
    model = Partidos
    extra = 0
    fields = ('equipo_local','puntos_equipo_local','equipo_visitante','puntos_equipo_visitante')
    readonly_fields = ('equipo_local','equipo_visitante',)
    fk_name = 'jornada'
    verbose_name = 'Partido'
    verbose_name_plural = 'Partidos'

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Jornadas)
class JornadasAdmin(admin.ModelAdmin):
    actions = None
    ordering = ('id_jornada',)
    inlines = (PartidosInline,)
