class Bus:
    def __init__(self, number, area=None):
        self.number = number
        self.area = area
    def __repr__(self):
        return f'<tranSEAt.Bus[{self.number}]>'

class Stop:
    def __init__(self, name, coordinates, status=True, id=-1):
        self.id = id
        self.name = name
        self.status = status
        self.coordinates = coordinates
    def __repr__(self):
        return f'<tranSEAt.Stop[{self.id}, \'{self.name}\']>'

class Arrival:
    def __init__(self, transport, time, minutes, extra_info={}):
        self.transport = transport
        self.time = time
        self.minutes = minutes
        self.extra_info=extra_info
    def __repr__(self):
        return f'<tranSEAt.Arrival[{self.transport.upper() if type(self.transport) == str else self.transport}, {self.time.strftime("%H:%M")}, {self.minutes}min]'
