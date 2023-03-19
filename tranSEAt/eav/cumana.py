from ..shared.models import *
from datetime import time
from . import teleind

class Cumana(teleind.Teleind):
    properties = {
        'averageSpeed': 30,
        'averageFrequency': lambda x, y : 20,
        'averageStopTime': 15,
        'openTimes': (time(5, 20), time(22, 50)),
        'dataFile': 'data/cumana.json',
        'directions': {
            'montesanto': 0,
            'torregaveta': -1
        },
        'trainTimeRanges': [
            (time(5, 20), time(22, 40)),
            (time(5, 34), time(22, 25))
        ]
    }
    filter = ['torregaveta', 'fuorigrotta', 'montesanto']