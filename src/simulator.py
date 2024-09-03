# type: ignore
from queue import Queue

class Simulator:
    def __init__(self, queue: Queue, servers : int, random_numbers : list, time_first_event : int, arrival_interval : list, service_interval : list) -> None:
        self.queue          : Queue = queue 
        self.servers        : int   = servers
        self.random_numbers : list    = random_numbers
        self.last_random_index : int = 0
        self.losses         : int   = 0
        self.arrival_interval : list = arrival_interval
        self.service_interval : list = service_interval
        self.time_last_event : float = 0
        self.states : list = []
        self.time : float = 0
        
        self.__init_states()
        
        # TODO: Verificar como vamos tratar o primeiro evento da fila 
        self.time_first_event = time_first_event
        
        print(self)
    
    def simulate(self):
        self.running = True
        while(self.running):
            # First event
            if self.time == 0:
                self.time = self.time_first_event
                self.arrive()
            else:
                self.running = False
                
    
    def leave(self, delta_time):
        self.acumulate_time(self.time, self.queue.status)
        
        self.queue.dequeue()
        
        if self.queue.status >= self.servers:
            # TODO: Escalonar saída
            delta_time = self.time + self.random_interval(self.service_interval[0], self.service_interval[1])
            print(f'Escalonado evento de saída para: {delta_time}')
    
    def arrive(self):
        self.acumulate_time(self.time, self.queue.status)

        if self.queue.enqueue:
            # TODO: Escalonar evento de saída
            delta_time = self.time + self.random_interval(self.service_interval[0], self.service_interval[1])
            print(f'Escalonado evento de saída para: {delta_time}')
        else:
            self.losses += 1
    
        # TODO: Escalonar evento de chegada
        delta_time = self.time + self.random_interval(self.arrival_interval[0], self.arrival_interval[1])
        print(f'Escalonado evento de chegada para: {delta_time}')
    
    def acumulate_time(self, delta_time : float, state_index: int):
        self.states[state_index] = self.states[state_index] + (delta_time-self.time_last_event)
    
    def random_interval(self, a : int, b : int) -> float:
        if self.last_random_index < len(self.random_numbers):
            random_number = self.random_numbers[self.last_random_index]
            self.last_random_index += 1
            return a + ((b-a)*random_number)
        
        return -1
    
    def __init_states(self):
        for i in range(self.queue.capacity+1):
            self.states.append(0.0)
    
    def __str__(self) -> str:
        return f'Queue: {self.queue}; Servers: {self.servers}; Losses: {self.losses} \nStates:\n{self.__states_to_str()}' ##{self.__random_numbers_to_str()}'
    
    def __states_to_str(self):
        res = ''
        
        for i in range(len(self.states)):
            res += f'{i}: {self.states[i]}\n'
        
        return res
    
    def __random_numbers_to_str(self):
        str = f'\nRandom numbers: {len(self.random_numbers)}\n'
        for number in range(len(self.random_numbers)):
            str += (f'{number} | {self.random_numbers[number]}\n')
            
        return str