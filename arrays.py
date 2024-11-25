"""
FIFO= first in first out
"""

from collections import deque
from stacks import Empty

class ArrayQueue:
    """using an Array as the Queue base """
    default_capacity = 32

    def __init__(self):
        self. size = 0
        self.data = [None] * ArrayQueue.default_capacity
        self.front = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def top(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self.data[self.front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        ans  = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1 ) % len(self.data)
        self.size -= 1
        return ans
    
    def enqueue(self, e):
        if self.size == len(self.data):
            self.resize( 2 * len(self.data))
        available = (self.front + self.size) % len(self.data)
        self.data[available] = e
        self.size += 1

    def resize(self, capacity):
        prev = self.data
        self.data = [None] * capacity
        moving = self.front
        for item in range(self.size):
            self.data[item] = prev[moving]
            moving = (1 + moving) % len(prev)
        self.front = 0
        
tk = ArrayQueue()

numbers2 = [12,4,0,4,27]
    

a = [12,-5,17,6,0,3,9,100]
for i in numbers2:
    tk.enqueue(i)
    print(f'Enqueued number: {i}')
print(tk)

def simple_array():
    myQue = deque()

    for number in a:
        myQue.append(number)

    print(f'New List: {myQue}')
    myQue.popleft()


    print(myQue)