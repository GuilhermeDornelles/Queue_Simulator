from queue_1 import SimpleQueue
from scheduler import Scheduler
from utils import Event, EventType

class Simulator:
    def __init__(self, queue: SimpleQueue, servers : int, random_numbers : list, time_first_event : int, arrival_interval : list, service_interval : list) -> None:
        self.queue          : SimpleQueue = queue 
        self.servers        : int   = servers
        self.random_numbers : list    = random_numbers
        self.last_random_index : int = 0
        self.losses         : int   = 0
        self.arrival_interval : list = arrival_interval
        self.service_interval : list = service_interval
        self.time_last_event : float = 0
        self.states : list = []
        self.time : float = 0
        self.scheduler : Scheduler = Scheduler()
        self.scheduler.add_event(Event(EventType.ARRIVE, time_first_event))
        
        self.__init_states()
    
    def simulate(self):
        self.running = True
        while(self.running):
            if not self.__all_random_used():
                event : Event = self.scheduler.get_next_event()

            if event:
                self.time_last_event = self.time
                self.time = event.time
                if event.type == EventType.ARRIVE:
                    self.arrive()
                else:
                    self.leave()
            else:
                self.running = False
    
    def leave(self):
        self.acumulate_time(self.time, self.queue.status)

        self.queue.dequeue()
        
        if self.queue.status >= self.servers:
            # TODO: Escalonar saída
            delta_time = self.time + self.random_interval(self.service_interval[0], self.service_interval[1])
            self.scheduler.add_event(Event(EventType.LEAVE, delta_time))
    
    def arrive(self):
        self.acumulate_time(self.time, self.queue.status)

        if self.queue.status < self.queue.capacity:
            self.queue.enqueue()
            if self.queue.status <= self.servers:
                # TODO: Escalonar evento de saída
                delta_time = self.time + self.random_interval(self.service_interval[0], self.service_interval[1])
                self.scheduler.add_event(Event(EventType.LEAVE, delta_time))
        else:
            self.losses += 1
    
        # TODO: Escalonar evento de chegada
        delta_time = self.time + self.random_interval(self.arrival_interval[0], self.arrival_interval[1])
        self.scheduler.add_event(Event(EventType.ARRIVE, delta_time))
    
    def acumulate_time(self, delta_time : float, state_index: int):
        self.states[state_index] = self.states[state_index] + (delta_time-self.time_last_event)
    
    def __all_random_used(self) -> bool:
        return self.last_random_index >= len(self.random_numbers)
    
    def random_interval(self, a : int, b : int) -> float:
        if self.last_random_index < len(self.random_numbers):
            random_number = self.random_numbers[self.last_random_index]
            self.last_random_index += 1
            return a + ((b-a)*random_number)
        else:
            self.running = False
            return -1
    
    def __init_states(self):
        for i in range(self.queue.capacity+1):
            self.states.append(0.0)
    
    def __str__(self) -> str:
        return f'SimpleQueue: {self.queue}; Servers: {self.servers}; Losses: {self.losses} \nStates:\n{self.__states_to_str()}'
    
    def __states_to_str(self):
        res = ''
        
        for i in range(len(self.states)):
            res += f'{i}: {round(self.states[i],4)}\n'
        
        return res
    
    def __random_numbers_to_str(self):
        str = f'\nRandom numbers: {len(self.random_numbers)}\n'
        for number in range(len(self.random_numbers)):
            str += (f'{number} | {self.random_numbers[number]}\n')
            
        return str