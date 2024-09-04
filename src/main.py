# type: ignore
from queue_1 import SimpleQueue
from simulator import Simulator
from generator import Generator

def main():
    # queue_capacity = 5
    servers = 1
    # time_first_event = 2.0
    # arrival_interval = [2, 5]
    # service_interval = [3, 5]
    
    # random_numbers = Generator().generate_numbers(total_number=100000, seed=1234, multiplier=33, increment=44, module=99999, precision=2)

    time_first_event = 2.0
    service_interval = [3, 6]
    arrival_interval = [1, 2]
    queue_capacity = 3

    random_numbers = [
        0.3276,
        0.8851,
        0.1643,
        0.5542,
        0.6813,
        0.7221,
        0.9881,
    ]

    # print(random_numbers)
    
    queue = SimpleQueue(queue_capacity)
    simulator = Simulator(queue, servers, random_numbers = random_numbers, time_first_event=time_first_event, arrival_interval=arrival_interval, service_interval=service_interval)
    
    # print(simulator)
    simulator.simulate()
    print(simulator)
    print('Executed events: ')
    for ev in simulator.scheduler.executed_events:
        print(ev)

if __name__ == '__main__':
    main()