from enum import Enum
class EventType(Enum):
    ARRIVE = 'ARRIVE'
    LEAVE  = 'LEAVE'

class Event:
    def __init__(self, type : EventType, time: float) -> None:
        self.type : EventType = type
        self.time : float     = time
        self.id   : int       = -1
        
    def __str__(self) -> str:
        return f'ID: {self.id}; Tipo: {self.type.value}; Time: {self.time}'