from datetime import datetime, time

def getNow() -> datetime.time:
    return datetime.now().time()

def diffTime(time1: time, time2: time) -> float:
    if time1 < time2:
        temp = time1
        time1 = time2
        time2 = temp
        del temp
    return (datetime.combine(datetime.today(), time1) - datetime.combine(datetime.today(), time2)).seconds