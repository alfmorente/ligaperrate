import os
import django


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simulador.settings')
    django.setup()

    from liga.models import Jornadas, Partidos, Equipos
    from competitions.scheduler.roundrobin import DoubleRoundRobinScheduler


    def rellena_partidos():
        if Jornadas.objects.all().exists():
            Jornadas.objects.all().delete()
        equipos = Equipos.objects.all().order_by('id_equipo')
        lista_equipos = equipos.values_list('nombre')
        lista_equipos = [lista_equipos[i][0] for i,v in enumerate(lista_equipos)]
        scheduler = DoubleRoundRobinScheduler(lista_equipos)
        lista_partidos = scheduler.generate_schedule()
        for indice,partidos_jornada in enumerate(lista_partidos):
            jornada = Jornadas.objects.create(num_jornada=indice+1)
            for partido in partidos_jornada:
                if None not in partido:
                    Partidos.objects.create(equipo_local=Equipos.objects.get(nombre=partido[0]),
                                            equipo_visitante=Equipos.objects.get(nombre=partido[1]), jornada=jornada)


    rellena_partidos()