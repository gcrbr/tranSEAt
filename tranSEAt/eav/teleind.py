from ..shared import utils, metro
from ..shared.models import *
from datetime import datetime, time
import requests, math, json

class Teleind(metro.Metro):
    def getEavDate(self) -> str:
        now = datetime.now()
        return math.floor((now.day + now.month + now.year)/2)

    def getEavService(self, stop: Stop) -> dict:
        return requests.get(
            f'https://statocorsa.eavsrl.it/DatiCorsaRest.svc/Percorsi/{stop.id}/{self.getEavDate()}',
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
        ).json()

    def getOnlineArrivals(self, stop: Stop) -> list[Arrival]:
        trains = []
        for train in self.getEavService(stop):
            if train['DESTINAZIONE'].lower() in self.filter:
                trains.append(
                    Arrival(
                        train['DESTINAZIONE'],
                        train_time := datetime.strptime(train['PARTENZA'],'%Y-%m-%d %H:%M:%S').time(),
                        round(utils.diffTime(train_time, utils.getNow())/60),
                        {
                            'departing': train['PARTENZA'] == 'In partenza',
                            'delay': train['RITARDO'],
                            'train_number': train['TR']
                        }
                    )
                )
        return trains