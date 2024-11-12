"""
FIFO= first in first out
"""

from collections import deque

a = [12,-5,17,6,0,3,9,100]

myQue = deque()

for number in a:
    myQue.append(number)

print(f'New List: {myQue}')
myQue.popleft()


print(myQue)