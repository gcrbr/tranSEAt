from datetime import datetime, time
import requests, time as _time
from .. import shared
from ..shared.models import *

class Linea2(shared.metro.Metro):
    properties = {
        'averageSpeed': 30,
        'averageFrequency': lambda x, y : 10,
        'averageStopTime': 20,
        'dataFile': 'data/linea2.json',
        'directions': {
            'Pozzuoli': 0,
            'San Giovanni-Barra': -1
        },
        'trainTimeRanges': [
            (time(5, 43), time(23, 18)),
            (time(5, 43), time(23, 18))
        ]
    }

    def getJSTime(self) -> str:
        return _time.strftime('%a %b %d %Y %H:%M:%S %Z%z', _time.gmtime())

    def getOnlineArrivals(self, stop: Stop) -> list[Arrival]:
        api = requests.get(
            f'http://www.viaggiatreno.it/infomobilita/resteasy/viaggiatreno/partenze/S0{stop.id}/{self.getJSTime()}',
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
        ).json()
        trains = []
        for train in api:
            train_time = datetime.strptime(train['compOrarioPartenza'], '%H:%M').time()
            if train_time >= shared.utils.getNow():
                trains.append(
                    Arrival(
                        train['destinazione'],
                        train_time,
                        round(shared.utils.diffTime(train_time, shared.utils.getNow())/60),
                        {
                            'delay': train['ritardo'],
                            'train_type': train['categoria'],
                            'train_number': train['numeroTreno'],
                            'platform': train['binarioEffettivoPartenzaDescrizione'] if train['binarioEffettivoPartenzaDescrizione'] else train['binarioProgrammatoPartenzaDescrizione']
                        }
                    )
                )
        return trains