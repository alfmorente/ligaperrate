import logging
from random import sample
from django.shortcuts import render

# Create your views here.
def vista_inicio(request):
    try:
        return render(request, 'index.html')
    except Exception as ex:
        logging.exception(str(ex))


def vista_resultados(request, jugadores, mazo):
    adqDict = obtieneAdq(jugadores, mazo)
    oficiosDict = obtieneOficios(jugadores)
    cartas_jugador = {}
    i = 1
    while i <= jugadores:
        cartas_jugador[i] = {'adq': adqDict[i], 'oficios': oficiosDict[i]}
        i += 1
    return render(request, 'resultados.html', context={'cartas':cartas_jugador})


def obtieneAdq(numJugads, mazoSeleccionado):
    mazoE = list(range(11,63))+[338]
    mazoI = list(range(63,105))+[337]
    mazoK = list(range(105,147))+[339]

    if mazoSeleccionado == 'E':
        adqTotales = mazoE
    elif mazoSeleccionado == 'I':
        adqTotales = mazoE + mazoI
    else:
        adqTotales = mazoE + mazoI + mazoK

    i = 1
    adqDict = {}
    while i <= numJugads:
        adqAux = sample(adqTotales,7)
        adqAux.sort()
        adqDict[i] = adqAux
        adqTotales = [e for e in adqTotales if e not in adqAux]
        i += 1

    return adqDict


def obtieneOficios(numJugads):
    e1 = [150, 151, 153, 154, 162, 171, 172, 173, 174, 175, 176, 184, 187, 188, 189, 190, 191, 194, 195, 199, 200, 202,
          210, 218]
    i1 = [219, 220, 225, 226, 227, 231, 233, 235, 238, 241, 242, 243, 244, 247, 248, 256, 262, 265]
    k1 = [267, 268, 270, 272, 274, 278, 279, 281, 283, 286, 290, 292, 293, 300, 306]
    e3 = [147, 148, 152, 155, 156, 157, 158, 161, 165, 168, 170, 177, 182, 197, 205, 209, 211, 214, 217, 341]
    i3 = [221, 224, 228, 236, 240, 245, 258, 259]
    k3 = [276, 277, 280, 282, 285, 291, 294, 296, 297]
    e4 = [149, 159, 160, 163, 166, 167, 181, 183, 185, 186, 192, 193, 201, 203, 204, 206, 212, 213]
    i4 = [222, 229, 232, 246, 249, 250, 252, 253, 254, 257, 264, 340]
    k4 = [266, 271, 275, 287, 288, 295, 298, 302, 303, 305, 309, 311, 342]

    if numJugads < 3:
        oficiosTotales = e1 + i1 + k1
    elif numJugads == 3:
        oficiosTotales = e1 + i1 + k1 + e3 + i3 + k3
    else:
        oficiosTotales = e1 + i1 + k1 + e3 + i3 + k3 + e4 + i4 + k4

    i = 1
    oficiosDict = {}
    while i<=numJugads:
        oficiosAux = sample(oficiosTotales,7)
        oficiosAux.sort()
        oficiosDict[i] = oficiosAux
        oficiosTotales = [e for e in oficiosTotales if e not in oficiosAux]
        i+=1

    return oficiosDict