from liga.models import Partidos,Jornadas,Equipos

def actualiza_clasificacion():
    partidos_jugados = Partidos.objects.filter(jornada__jornada_jugada=True)
    dict_equipos = {}
    for equipo in Equipos.objects.all():
        dict_equipos[equipo.nombre] = {'Puntos':0,'Victorias':0,'Derrotas':0,'Empates':0,'A_Favor':0,'En_Contra':0,'Golaverage':0}
    for partido in partidos_jugados:
        eq_local = partido.equipo_local.nombre
        eq_visit = partido.equipo_visitante.nombre
        dict_equipos[eq_local]['A_Favor'] += partido.puntos_equipo_local
        dict_equipos[eq_local]['En_Contra'] += partido.puntos_equipo_visitante
        dict_equipos[eq_visit]['A_Favor'] += partido.puntos_equipo_visitante
        dict_equipos[eq_visit]['En_Contra'] += partido.puntos_equipo_local
        dict_equipos[eq_local]['Golaverage'] += partido.puntos_equipo_local - partido.puntos_equipo_visitante
        dict_equipos[eq_visit]['Golaverage'] += partido.puntos_equipo_visitante - partido.puntos_equipo_local
        if partido.puntos_equipo_local > partido.puntos_equipo_visitante:
            dict_equipos[eq_local]['Puntos'] += 3
            dict_equipos[eq_local]['Victorias'] += 1
            dict_equipos[eq_visit]['Derrotas'] += 1
        elif partido.puntos_equipo_local == partido.puntos_equipo_visitante:
            dict_equipos[eq_local]['Puntos'] += 1
            dict_equipos[eq_visit]['Puntos'] += 1
            dict_equipos[eq_local]['Empates'] += 1
            dict_equipos[eq_visit]['Empates'] += 1
        else:
            dict_equipos[eq_visit]['Puntos'] += 3
            dict_equipos[eq_local]['Derrotas'] += 1
            dict_equipos[eq_visit]['Victorias'] += 1
    return sorted(dict_equipos.items(),key=lambda k: (-k[1]['Puntos'],-k[1]['Golaverage']))