from django.db import models
from django.contrib.auth.models import User


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32, unique=True, verbose_name='Nombre del equipo')
    usuario = models.ForeignKey(User, db_column='usuario', on_delete=models.DO_NOTHING)
    partidos_ganados = models.IntegerField(verbose_name='Partidos ganados',default=0)
    partidos_perdidos = models.IntegerField(verbose_name='Partidos perdidos',default=0)
    partidos_empatados = models.IntegerField(verbose_name='Partidos empatados',default=0)
    puntos_favor = models.IntegerField(verbose_name='Puntos a favor',default=0)
    puntos_contra = models.IntegerField(verbose_name='Puntos recibidos',default=0)

    class Meta:
        managed = True
        db_table = 'equipos'
        verbose_name = 'Equipo de la liga'
        verbose_name_plural = 'Equipos de la liga'

    def __str__(self):
        return self.nombre


class Jornadas(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    num_jornada = models.IntegerField(verbose_name='Jornada',unique=True)
    jornada_jugada = models.BooleanField(verbose_name='Jornada ya jugada',default=False)

    class Meta:
        managed = True
        db_table = 'jornadas'
        verbose_name = 'Jornada de liga'
        verbose_name_plural = 'Jornadas de liga'

    def __str__(self):
        return 'Jornada {}'.format(self.num_jornada)


class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_local = models.ForeignKey(Equipos, verbose_name='equipo_local',related_name='equipo_local', on_delete=models.DO_NOTHING)
    puntos_equipo_local = models.IntegerField(verbose_name='Puntos equipo local',default=0)
    equipo_visitante = models.ForeignKey(Equipos, verbose_name='equipo_visitante',related_name='equipo_visitante',on_delete=models.DO_NOTHING)
    puntos_equipo_visitante = models.IntegerField(verbose_name='Puntos equipo visitante',default=0)
    jornada = models.ForeignKey(Jornadas, verbose_name='jornada',on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'partidos'
        verbose_name = 'Partido de liga'
        verbose_name_plural = 'Partidos de liga'

    def __str__(self):
        return '{} - {}'.format(self.equipo_local,self.equipo_visitante)