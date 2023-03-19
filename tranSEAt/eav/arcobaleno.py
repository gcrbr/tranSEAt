from ..shared.models import *
from datetime import time
from . import teleind

def frequency(train_id, direction):
    if train_id <= 2 or (train_id >= 11 and train_id <= 28) or train_id >= 37:
        return 30
    else:
        return 15

class Arcobaleno(teleind.Teleind):
    properties = {
        'averageSpeed': 52.2,
        'averageFrequency': frequency,
        'averageStopTime': 20,
        'openTimes': (time(6), time(21, 57)),
        'dataFile': 'data/arcobaleno.json',
        'directions': {
            'aversa': 0,
            'piscinola': -1
        },
        'trainTimeRanges': [
            (time(6), time(21, 42)),
            (time(6, 15), time(21, 57))
        ]
    }
    filter = ['aversa', 'piscinola scampia']