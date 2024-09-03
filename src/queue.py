# type: ignore
class Queue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.status   = 0
    
    def enqueue(self) -> bool:
        if (self.status < self.capacity):
            self.status += 1
            return True
        
        return False
    
    def dequeue(self) -> bool:
        if (self.status > 0):
            self.status -= 1
            return True
        
        return False
    
    def __str__(self) -> str:
        return f'Capacity {self.capacity}'