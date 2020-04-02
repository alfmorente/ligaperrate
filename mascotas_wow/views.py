import logging
from django.shortcuts import render
from django.forms import modelformset_factory
from django import forms
from mascotas_wow.models import Bandas
from mascotas_wow.forms import BandasForm


# Create your views here.
def progreso_bandas(request):
    try:
        Formset = modelformset_factory(Bandas, fields=('tx_nombre', 'bool_acabada'),
                                       widgets={'tx_nombre': forms.TextInput, 'bool_acabada': forms.CheckboxInput})
        if request.method == 'POST':
            formset = Formset(request.POST)
            if formset.is_valid():
                formset.save()
        return render(request, 'avance_semanal.html', context={'formset': Formset})

    except Exception as ex:
        logging.exception(str(ex))
