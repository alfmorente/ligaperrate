# Generated by Django 2.1.4 on 2018-12-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga', '0004_jornadas_jornada_jugada'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='partidos_empatados',
            field=models.IntegerField(default=0, verbose_name='Partidos empatados'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='partidos_ganados',
            field=models.IntegerField(default=0, verbose_name='Partidos ganados'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='partidos_perdidos',
            field=models.IntegerField(default=0, verbose_name='Partidos perdidos'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='puntos_contra',
            field=models.IntegerField(default=0, verbose_name='Puntos recibidos'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='puntos_favor',
            field=models.IntegerField(default=0, verbose_name='Puntos a favor'),
        ),
    ]
