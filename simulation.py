from staticq import statQueue as sq
from typing import *
import time

try:
    clock: List[float] = sq(17, 0, 0.4, 1.6, 2.1, 2.4, 3.1, 3.3, 3.8, 4.0, 4.9, 5.6, 5.8, 7.2, 8.6)
    customer: Dict = {0.4: 'A', 1.6: 'A', 2.1: 'A', 2.4: 'D', 3.1: 'D', 
                3.3: 'D', 3.8: 'A', 4.0: 'A', 4.9: 'D', 5.6: 'A', 
                5.8: 'A', 7.2: 'A', 8.6: 'D'}
    wait: List[float] = []
    server: List[float] = []
    
    while len(clock()) != 0:        
        if clock('F') not in customer:
            print(f"Clock: {clock('F')}")
            print(f"Wait queue: {wait}")
            print(f"Server queue: {server}")
            print("-------------------------")
            clock('D')
            time.sleep(1)
            continue
            
        if customer[clock('F')] == 'A':
            if len(server) == 0:
                server.append(clock('F'))
            else:
                wait.append(clock('F'))
        elif customer[clock('F')] == 'D':
            server.pop(0)
            
            if len(server) == 0 and len(wait) != 0:
                server.append(wait[0])
                wait.pop(0)

        print(f"Clock: {clock('F')}")
        print(f"Wait queue: {wait}")
        print(f"Server queue: {server}")
        print("-------------------------")
        clock('D')
        time.sleep(1)
        
    print("    End of Simulation    ")
    print("-------------------------")
    
    # for i in range(15):
    #     print(f"Clock: {clock('F')}")
    #     clock('D')
    #     time.sleep(0.2)
    
except(TypeError):
    print("You exceeded the queue limit.")
except(IndexError):
    print("End Simulation")
    

