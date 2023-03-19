from ..shared.models import *
from ..shared import metro
from datetime import time

def frequency(train_id, direction):
    if direction == 0:
        if train_id > 6 and train_id < 87:
            return 9
        elif train_id >= 87:
            return 14
        else:
            return 10
    elif direction == -1:
        if train_id < 2:
            return 20
        elif train_id >= 2 and train_id < 7:
            return 10
        elif train_id >= 87:
            return 14
        else:
            return 9

class Linea1(metro.Metro):
    properties = {
        'averageSpeed': 32,
        'averageFrequency': frequency,
        'averageStopTime': 20,
        'openTimes': (time(6), time(23)),
        'dataFile': 'data/linea1.json',
        'directions': {
            'piscinola': 0,
            'garibaldi': -1
        },
        'trainTimeRanges': [
            (time(6), time(22)),
            (time(6, 20), time(23))
        ]
    }