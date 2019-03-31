"""simulador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from liga.views import muestra_clasificacion, presenta_generador, generador, lee_puntuaciones

urlpatterns = [
    path('home/', admin.site.urls, name='index'),
    path('',view=muestra_clasificacion,name='clasificacion'),
    path('generador',view=presenta_generador, name='presenta-generador'),
    path('genera_calendario',view=generador, name='generador'),
    path('lee_puntuacion',view=lee_puntuaciones, name='lee-puntuacion'),
    path('agricola', include('agricola.urls')),
]
