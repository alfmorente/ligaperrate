import logging
from django.shortcuts import render
from django.forms.models import model_to_dict
from mascotas_wow.models import Bandas
from mascotas_wow.forms import BandasForm


# Create your views here.
def progreso_bandas(request):
    try:
        objeto_bandas = Bandas.objects.all()
        if request.method == 'POST':
            form = BandasForm(request.POST)
            if form.is_valid():
                objeto_bandas.save()
        else:
            form = BandasForm(initial=model_to_dict(objeto_bandas))
            return render(request, 'avance_semanal.html', context={'form': form})
    except Exception as ex:
        logging.exception(str(ex))
