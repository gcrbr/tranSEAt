from ..shared.models import *
from ..shared import metro
from datetime import time

class Centrale(metro.Metro):
    properties = {
        'averageSpeed': 7 * 3.6,
        'averageFrequency': lambda x,y:10,
        'averageStopTime': 10,
        'openTimes': (time(8, 30), time(21, 30)),
        'dataFile': 'data/funicolare-centrale.json',
        'directions': {
            'fuga': 0,
            'augusteo': -1
        },
        'trainTimeRanges': [
            (time(8, 30), time(21, 30)),
            (time(8, 30), time(21, 30))
        ]
    }

class Montesanto(metro.Metro):
    properties = {
        'averageSpeed': 7 * 3.6,
        'averageFrequency': lambda x,y:10,
        'averageStopTime': 10,
        'openTimes': (time(7), time(22)),
        'dataFile': 'data/funicolare-montesanto.json',
        'directions': {
            'fuga': 0,
            'augusteo': -1
        },
        'trainTimeRanges': [
            (time(7), time(22)),
            (time(7), time(22))
        ]
    }

class Mergellina(metro.Metro):
    properties = {
        'averageSpeed': 3.5 * 3.6,
        'averageFrequency': lambda x,y:10,
        'averageStopTime': 10,
        'openTimes': (time(7), time(22)),
        'dataFile': 'data/funicolare-mergellina.json',
        'directions': {
            'fuga': 0,
            'augusteo': -1
        },
        'trainTimeRanges': [
            (time(7), time(22)),
            (time(7), time(22))
        ]
    }