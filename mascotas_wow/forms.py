from django.forms import ModelForm
from mascotas_wow.models import Bandas

class BandasForm(ModelForm):
    class Meta:
        model = Bandas
        fields = ['id_banda', 'tx_nombre', 'tx_expansion', 'bool_acabada']