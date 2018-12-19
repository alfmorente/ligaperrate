from django.shortcuts import render, redirect
from liga.actualiza_clasificacion import actualiza_clasificacion
from liga.models import Jornadas, Partidos, Equipos
from competitions.scheduler.roundrobin import TripleRoundRobinScheduler


def muestra_clasificacion(request):
    clasif = actualiza_clasificacion()
    context = {'clasif': clasif}
    return render(
        request,
        'clasificacion.html',
        context,
        {
            'title': 'Clasificacion',
        }
    )


def presenta_generador(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return render(request, 'generador.html')


def generador(request):
    if request.user.is_superuser:
        if Jornadas.objects.all().exists():
            Jornadas.objects.all().delete()
        equipos = Equipos.objects.all().order_by('id_equipo')
        lista_equipos = equipos.values_list('nombre')
        lista_equipos = [lista_equipos[i][0] for i, v in enumerate(lista_equipos)]
        scheduler = TripleRoundRobinScheduler(lista_equipos)
        lista_partidos = scheduler.generate_schedule()
        for indice, partidos_jornada in enumerate(lista_partidos):
            if indice < 38:
                jornada = Jornadas.objects.create(num_jornada=indice + 1)
                for partido in partidos_jornada:
                    if None not in partido:
                        Partidos.objects.create(equipo_local=Equipos.objects.get(nombre=partido[0]),
                                                equipo_visitante=Equipos.objects.get(nombre=partido[1]),
                                                jornada=jornada)
        return redirect('home/')
