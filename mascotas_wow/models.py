from django.db import models

# Create your models here.
class Bandas(models.Model):
    id_banda = models.AutoField(primary_key=True)
    tx_nombre = models.CharField(max_length=100, verbose_name='Nombre de la banda')
    tx_expansion = models.CharField(max_length=32, verbose_name='Expansión de la banda')
    bool_acabada = models.BooleanField(default=False, verbose_name='Acabada esta semana')

    class Meta:
        managed = True
        db_table = 'bandas'
        verbose_name = 'Banda semanal'
        verbose_name_plural = 'Bandas semanales'
