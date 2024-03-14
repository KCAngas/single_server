from typing import *
from staticq import funcQue as fq
from staticq import isEmpty
# import time

interarrTime: int = 4
serviceTime: int = 10
clock: int = 0
arrTime: int = 0
serverStat: int = 0

queue = fq(5)
arrival = fq(10)
departure = fq(10)

for _ in range(10):
    arrTime += interarrTime
    arrival('E', arrTime)
    departure('E', arrTime + serviceTime)
    
print(f"Clock: {clock}")
print(f"A: {arrival('F')}")
print(f"D: {departure('F')}")
print(f"Queue: {queue()}")
print(f"Status: {serverStat}")
print()
# time.sleep(4)

while not isEmpty(departure()):
    if arrival('F') == float('inf') and departure('F') == float('inf'):
        break
    
    clock = min(arrival('F'), departure('F'))
    print(f"Clock: {clock}")

    if arrival('F') < departure('F'):
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
    

    print(f"A: {arrival('F')}")
    print(f"D: {departure('F')}")
    print(f"Queue: {queue()}")
    print(f"Status: {serverStat}")
    print()
    # time.sleep(4)

print("--- End of Simulation ---")

# def main():

        
# if __name__ == '__main__':
#     main()
    




