from django.urls import path
from agricola.views import vista_inicio, vista_resultados

urlpatterns = [
    path('', view=vista_inicio, name='inicio'),
    path('resultados/<int:jugadores>/<str:mazo>', vista_resultados, name='resultados')
]