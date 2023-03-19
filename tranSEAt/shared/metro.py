from datetime import datetime, time, timedelta
from .models import *
from . import utils
import json, os

class Metro:
    '''properties = {
        'averageSpeed': 0, # In kilometers per hour
        'averageFrequency': lambda x:30, # Function that returns time in minutes
        'averageStopTime': 0, # How much time the metro stops to let people leave/enter
        'dataFile': 'example.json', # File in which you store the stops data
        'directions': {
            'dir1': 0,
            'dir2': -1
        },
        'trainTimeRanges': [
            (time(0), time(1)), # First and last train FROM direction 1
            (time(0, 20), time(2)) # First and last train FROM direction 2
        ]
    }'''
    def __init__(self):
        self.loadStops()

    def loadStops(self):
        self.stops = []
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), self.properties['dataFile']), 'r')
        data = json.loads(file.read())
        self.color = data['color']
        for stop in data['stops']:
            self.stops.append(Stop(stop['name'], tuple(stop['coordinates']), True, stop.get('id')))
        file.close()

    def getStops(self) -> list[Stop]:
        return self.stops

    def getStopByName(self, name: str) -> Stop:
        for stop in self.getStops():
            if stop.name.lower() == name.lower():
                return stop
        return None

    def getColor(self) -> str:
        return self.color

    def isOpen(self) -> bool:
        return utils.getNow() >= self.properties['trainTimeRanges'][0][0] and utils.getNow() <= self.properties['trainTimeRanges'][1][1]
    
    def getAverageFrequency(self, train_id: int, direction: int) -> float:
        return self.properties['averageFrequency'](train_id, direction)

    def getAverageSpeed(self) -> float:
        return self.properties['averageSpeed']

    def getDistanceBetweenStops(self, stop1: Stop, stop2: Stop) -> float:
        return 100 * ((stop1.coordinates[1] - stop2.coordinates[1])**2 + (stop1.coordinates[0] - stop2.coordinates[0])**2)**(1/2)
    
    def getTimeBetweenAdjacentStops(self, stop1: Stop, stop2: Stop) -> float:
        return (60 * (self.getDistanceBetweenStops(stop1, stop2) / self.getAverageSpeed())) + self.properties['averageStopTime']/60

    def getTimeBetweenStops(self, stop1: Stop, stop2: Stop) -> float:
        index1 = self.getStops().index(stop1)
        index2 = self.getStops().index(stop2)
        if abs(index1 - index2) == 1:
            return self.getTimeBetweenAdjacentStops(stop1, stop2)
        else:
            if index1 > index2:
                temp = index1
                index1 = index2
                index2 = temp
                del temp
            elapsed = 0
            for i in range(index1, index2):
                elapsed += self.getTimeBetweenAdjacentStops(self.getStops()[i], self.getStops()[i+1])
            return elapsed

    def getTotalTravelTime(self) -> float:
        return self.getTimeBetweenStops(self.getStops()[0], self.getStops()[-1])

    def addMinutes(self, time: time, minutes: float) -> time:
        return (datetime.combine(datetime.today(), time) + timedelta(minutes=minutes)).time()

    def getTimeTable(self, direction: int):
        first_train = self.properties['trainTimeRanges'][direction][0]
        trains = [first_train]
        train_id = 1
        while first_train < self.properties['trainTimeRanges'][direction][1]:
            first_train = self.addMinutes(first_train, self.getAverageFrequency(train_id, direction))
            trains.append(first_train)
            train_id += 1
        return trains

    def getNearestTime(self, direction: int, stop: Stop) -> datetime.time:
        timetable = self.getTimeTable(0 if direction == -1 else -1)
        stop_time = self.getTimeBetweenStops(self.getStops()[0 if direction == -1 else -1], stop)
        train = self.addMinutes(timetable[0], stop_time)
        difference = utils.diffTime(self.addMinutes(timetable[0], stop_time), utils.getNow())
        for i in range(1, len(timetable)):
            time_to_stop = self.addMinutes(timetable[i], stop_time)
            _diff = utils.diffTime(time_to_stop, utils.getNow())
            if _diff < difference and time_to_stop >= utils.getNow():
                difference = _diff
                train = time_to_stop
        return train

    def getArrivals(self, direction: int, stop: Stop) -> Arrival:
        if self.getStops().index(stop) == direction or (self.getStops().index(stop) == len(self.getStops()) - 1 and direction == -1):
            return None
        if not self.isOpen():
            return None
        next = self.getNearestTime(direction, stop)
        return Arrival(
            list(self.properties['directions'].keys())[direction], 
            next, 
            round(utils.diffTime(next, utils.getNow())/60)
        )