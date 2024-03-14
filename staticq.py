#Implementation of Static Queue using functional programming
from typing import *
    
def isEmpty(queue: List[float]) -> bool:
    if len(queue) == 0:
        return True
    return False

def funcQue(maxSize: int=0, *args: float) -> List[float]:
    if maxSize == 0:
        maxSize = float('inf')
    
    if len(args) > maxSize:
        return;
    
    queue = list(args)
        
    def enqueue(temp: List[float], value: int):
        if len(temp) == maxSize:
            raise TypeError("ERROR: Exceeded queue capacity.")
        else:
            temp += [value]
    
    def dequeue(temp: List[float]):
        if len(temp) == 0:
            return
        del temp[0]
        
    def operation(buffer: str=None, value: int=None) -> List[int]:
        if buffer == 'E':
            if value == None or type(value) != int:
                raise ValueError("USAGE: queue(\'E\', value=int)")
            enqueue(queue, value)
        elif buffer == 'D':
            dequeue(queue)
        elif buffer == 'F':
            if isEmpty(queue):
                enqueue(queue, float('inf'))
            return queue[0]
        return queue
        
    return operation


    
def main():
    try:
        size = 10
        queue = funcQue(size)
        # for _ in range(4):
        #     queue('E', _)
        print(f"Queue: {queue()}")
        print(f"Empty: {isEmpty(queue())}")
        
    except(TypeError):
        print("ERROR: Exceeded queue capacity.")
        
if __name__ == '__main__':
    main()
    