from django.contrib import admin
from django.urls import path
from liga.views import muestra_clasificacion, presenta_generador, generador, lee_puntuaciones

urlpatterns = [
    # path('home/', admin.site.urls, name='index'),
    path('',view=muestra_clasificacion,name='clasificacion'),
    path('generador',view=presenta_generador, name='presenta-generador'),
    path('genera_calendario',view=generador, name='generador'),
    path('lee_puntuacion',view=lee_puntuaciones, name='lee-puntuacion')
]