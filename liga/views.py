from django.shortcuts import render, redirect
from django.http import Http404
from liga.actualiza_clasificacion import actualiza_clasificacion
from liga.models import Jornadas, Partidos, Equipos
from competitions.scheduler.roundrobin import TripleRoundRobinScheduler
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL_BIWENGER = 'https://biwenger.as.com/login'

DICC_USUARIOS = {'Joselillo': 'JoseAngel', 'Ale': 'Ale', 'Karre': 'Carre', 'Pepe': 'Pepe', 'Moren': 'Moren',
                       'Nando':'Nando','Vega':'Vega','Manuel':'Baeza','Francisco':'Paco','Jose':'Jose',
                       'Frangallego':'Fran','Daniel':'Dani','Manolo':'Manolo'}


def muestra_clasificacion(request):
    clasif = actualiza_clasificacion()
    context = {'clasif': clasif}
    return render(
        request,
        'clasificacion.html',
        context,
        {
            'title': 'Clasificacion',
        }
    )


def presenta_generador(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return render(request, 'generador.html')


def generador(request):
    if request.user.is_superuser:
        if Jornadas.objects.all().exists():
            Jornadas.objects.all().delete()
        equipos = Equipos.objects.all().order_by('id_equipo')
        lista_equipos = equipos.values_list('nombre')
        lista_equipos = [lista_equipos[i][0] for i, v in enumerate(lista_equipos)]
        scheduler = TripleRoundRobinScheduler(lista_equipos)
        lista_partidos = scheduler.generate_schedule()
        for indice, partidos_jornada in enumerate(lista_partidos):
            if indice < 38:
                jornada = Jornadas.objects.create(num_jornada=indice + 1)
                for partido in partidos_jornada:
                    if None not in partido:
                        Partidos.objects.create(equipo_local=Equipos.objects.get(nombre=partido[0]),
                                                equipo_visitante=Equipos.objects.get(nombre=partido[1]),
                                                jornada=jornada)
        return redirect('home/')


def lee_puntuaciones(request):
    if request.user.is_superuser:
        try:
            if platform.system() == 'Darwin':
                driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_mac')
            elif platform.system() == 'Windows':
                driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
            elif platform.system() == 'Linux':
                driver = webdriver.Chrome(executable_path='drivers/chromedriver_linux')
            else:
                return redirect(Http404)
            driver.implicitly_wait(4)

            driver.get(URL_BIWENGER)
            driver.find_element_by_tag_name('button').click()
            cuadro_email = driver.find_element_by_name('email')
            cuadro_email.send_keys('lephor2@yahoo.es')
            cuadro_password = driver.find_element_by_name('password')
            cuadro_password.send_keys('bvdhkj')
            boton_acceder = driver.find_element_by_tag_name('button')
            boton_acceder.send_keys(Keys.RETURN)
            driver.find_element('id', 'nav-round').click()
            tabla_resultados = driver.find_element_by_css_selector('table.table.condensed.text-right.selectable')
            filas = tabla_resultados.find_elements_by_tag_name('tr')
            for fila in filas:
                if fila.text.split()[1] in DICC_USUARIOS:
                    # TODO guardar información en base de datos
                    print('{} tiene {} puntos'.format(DICC_USUARIOS[fila.text.split()[1]], fila.text.split()[-2]))
            driver.quit()
            return redirect('home/')
        except Exception as ex:
            print(str(ex))
            # driver.quit()
            return redirect(Http404)
