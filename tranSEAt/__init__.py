from .shared.models import *
from .shared import metro
from .shared import utils

from .trenitalia import linea2
from .eav import cumana, circumflegrea, arcobaleno
from .anm import linea1, funicolari, infoclick

linea2 = linea2.Linea2()

cumana = cumana.Cumana()
circumflegrea = circumflegrea.Circumflegrea()
arcobaleno = arcobaleno.Arcobaleno()

bus = infoclick.InfoClick()
linea1 = linea1.Linea1()
funicolare_centrale = funicolari.Centrale()
funicolare_montesanto = funicolari.Montesanto()
funicolare_mergellina = funicolari.Mergellina()

def drawMap(transport_group):
    import matplotlib.pyplot as plt
    import mplleaflet
    for transport in transport_group:
        x = [i.coordinates[1] for i in transport.getStops()]
        y = [i.coordinates[0] for i in transport.getStops()]
        plt.plot(x, y, '-,', color=transport.getColor(), linewidth=5)
    mplleaflet.show()