from django.contrib import admin
from django.db.models import Q
from .models import Equipos,Partidos,Jornadas


admin.site.site_header = 'Liga Perrateña'
admin.site.index_title = 'Liga perrateña'

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

    def has_add_permission(self, request, obj):
        return False

@admin.register(Jornadas)
class JornadasAdmin(admin.ModelAdmin):
    actions = None
    ordering = ('id_jornada',)
    inlines = (PartidosInline,)

    def save_related(self, request, form, formsets, change):
        super(JornadasAdmin, self).save_related(request, form, formsets, change)
        partidos_jornada = Partidos.objects.filter(jornada=form.instance)
        puntos_jugadores = 0
        for partido in partidos_jornada:
            if partido.equipo_local.nombre == 'IA':
                puntos_jugadores += partido.puntos_equipo_visitante
            elif partido.equipo_visitante.nombre == 'IA':
                puntos_jugadores += partido.puntos_equipo_local
            else:
                puntos_jugadores += partido.puntos_equipo_local + partido.puntos_equipo_visitante
        partido_ia = partidos_jornada.get(Q(equipo_local__nombre='IA')|Q(equipo_visitante__nombre='IA'))
        if partido_ia.equipo_local.nombre == 'IA':
            partido_ia.puntos_equipo_local = round(puntos_jugadores/13)
        else:
            partido_ia.puntos_equipo_visitante = round(puntos_jugadores / 13)
        partido_ia.save()

