from ..shared.models import *
from datetime import time
from . import teleind

def frequency(train_id, direction):
    if train_id < 2 and direction == 0:
        return 10
    elif train_id == 41 and direction == -1:
        return 11
    else:
        return 24

class Circumflegrea(teleind.Teleind):
    properties = {
        'averageSpeed': 30,
        'averageFrequency': frequency,
        'averageStopTime': 15,
        'openTimes': (time(5, 2), time(22, 4)),
        'dataFile': 'data/circumflegrea.json',
        'directions': {
            'montesanto': 0,
            'licola': -1
        },
        'trainTimeRanges': [
            (time(5, 2), time(21, 36)),
            (time(5, 56), time(22, 7))
        ]
    }
    filter = ['licola', 'quarto', 'montesanto']