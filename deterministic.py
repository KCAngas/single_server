from typing import *
from staticq import statQueue as sq
from staticq import isEmpty
import time

def populate(value: int, size: int) -> List[float]:
    queue = sq(size)
    counter = 0

    for _ in range(size):
        counter += value
        queue('E', counter)
        
    return queue

def addEach(queue: sq, value: int) -> List[float]:
    newQueue = sq(len(queue()))
    
    for num in queue():
        newQueue('E', num + value)
        
    return newQueue

def simulation(interarrTime: int, serviceTime: int, runLength: int):
    clock: int = 0
    sysTime: int = 0
    serverStat: int = 0
    queue = sq(5)

    arrival = populate(interarrTime, runLength)
    departure = addEach(arrival, serviceTime)
    
    def display():
        print(f"A: {arrival('F')}")
        print(f"D: {departure('F')}")
        print(f"Queue: {queue()}")
        print(f"Status: {serverStat}")
        print(f"System Time: {sysTime}")
        print()
          
    print(f"Clock: {clock}")
    display()

    while not isEmpty(departure()):
        if arrival('F') == float('inf') and departure('F') == float('inf'):
            break
        
        clock = min(arrival('F'), departure('F'))
        sysTime += clock
        
        print(f"Clock: {clock}")

        if arrival('F') <= departure('F'):
            if serverStat == 1 and not isEmpty(arrival()):
                queue('E', arrival('F'))
            else:
                serverStat = 1
            arrival('D')
        else:
            if len(queue()) != 0:
                queue('D')
                serverStat = 1
            else:
                serverStat = 0
            departure('D')

        display()

    print("--- End of Simulation ---")

def main():
    simulation(4, 7, 5)
        
if __name__ == '__main__':
    main()
    




