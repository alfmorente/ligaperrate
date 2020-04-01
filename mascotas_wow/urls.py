from django.urls import path
from mascotas_wow.views import progreso_bandas

urlpatterns = [
    path('', progreso_bandas, name='progreso_bandas'),
]