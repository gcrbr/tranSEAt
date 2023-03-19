from ..shared.models import *
from datetime import datetime
import requests

class InfoClick:
    # This key is static: https://www.anm.it/infoclick/infoclick.php
    key = 'b1c70009e5548f7449e290a689ecd82d928f8f6b7b5ce9e6c2ef3bae62b7a1ea41759a4989ee01c5e18081fa89fa18215469330eec982b7fb3b09d5c47db88f2'
    endpoint = 'https://srv.anm.it/ServiceInfoAnmLinee.asmx/'

    def apiRequest(self, method: str, data: dict) -> list:
        return requests.post(
            self.endpoint + method,
            headers = {
                'User-Agent': 'Mozilla/5.0',
                'Origin': 'https://www.anm.it',
                'Referer': 'https://www.anm.it/',
                'Content-Type': 'application/json; charset=utf-8'
            },
            json = {
                'key': self.key,
                **data
            }
        ).json()['d']

    def parseStops(self, apiContent: dict) -> list[Stop]:
        results = []
        for stop in apiContent:
            if stop['id']:
                results.append(
                    Stop(
                        stop['nome'],
                        (stop['lat'], stop['lon']),
                        stop['stato'] == 'OK',
                        int(stop['id'])
                    )
                )
        return results

    def parseBus(self, apiContent: dict) -> list[Bus]:
        results = []
        for bus in apiContent:
            results.append(
                Bus(
                    bus['linea'].strip(),
                    bus['copertura']
                )
            )
        return results

    def formatBus(self, bus):
        return bus.number if type(bus) == Bus else bus
    
    def formatStop(self, stop):
        return stop.id if type(stop) == Stop else stop

    def searchStopByFilter(self, query: str) -> list[Stop]:
        return self.parseStops(self.apiRequest('getPalineByFilter', {'text': query}))

    def searchStopByBus(self, bus) -> list[Stop]:
        return self.parseStops(self.apiRequest('CaricaPercorsoLinea', {'linea': self.formatBus(bus)}))
    
    def searchBusByStop(self, stop) -> list[Bus]:
        return self.parseStops(self.apiRequest('CaricaTransiti', {'Palina': self.formatStop(stop)}))
    
    def searchBusByFilter(self, query: str) -> list[Bus]:
        return self.parseBus(self.apiRequest('getLineeByFilter', {'text': query}))
    
    def getArrivals(self, stop) -> list[dict]:
        arrivals = []
        for arrival in self.apiRequest('CaricaPrevisioniNuova', {'Palina': self.formatStop(stop)}):
            arrivals.append(
                Arrival(
                    Bus(arrival['linea']),
                    datetime.strptime(arrival['time'], '%H:%M').time(),
                    int(arrival['timeMin'])
                )
            )
        return arrivals if arrivals else None
    
    def getBusDeviations(self, bus) -> dict:
        return self.apiRequest('RilevaAnomalieLinea', {'linea': self.formatBus(bus)})