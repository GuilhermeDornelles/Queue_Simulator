# type: ignore
from queue import Queue
from simulator import Simulator
from generator import Generator

def main():
    queue_capacity = 5
    servers = 1
    time_first_event = 2.0
    arrival_interval = [2, 5]
    service_interval = [3, 5]
    
    random_numbers = Generator().generate_numbers(total_number=100000, seed=1234, multiplier=33, increment=44, module=99999, precision=2)

    # print(random_numbers)
    
    queue = Queue(queue_capacity)
    simulator = Simulator(queue, servers, random_numbers = random_numbers, time_first_event=time_first_event, arrival_interval=arrival_interval, service_interval=service_interval)
    
    print(simulator)
    simulator.simulate()
    print(simulator)

if __name__ == '__main__':
    main()