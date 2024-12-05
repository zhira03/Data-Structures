"""
FILO: first in Last out 
"""
import os


class Stack():
    """using a List as the stack base """
    def __init__(self):
        self.stack = list()

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        else:
            return "List is Empty"
        
    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        else:
            return "List is Empty"
        
    def __str__(self):
        return str(self.stack)
    
class Empty(Exception):
    pass

class ArrayStack:
    """using an array as the stack base instead of a List"""

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.data.pop()
    


myStack = Stack()



numbers = 12 , 4 , 4,27
numbers2 = [12,4,0,4,27]


def reversefile(filename):
  
  S=ArrayStack()
  original=open(filename)
  for line in original:
    S.push(line.rstrip(' \n ')) #wewill re-insertnewlineswhenwriting
  original.close()
 
  #nowweoverwritewithcontents inLIFOorder
  output=open(filename, w ) # reopeningfileoverwritesoriginal
  while not S.isempty():
    output.write(S.pop()+ '\n' ) #re-insertnewlinecharacters
  output.close()

def tell_me():

    for i in numbers:
        myStack.push(i)
        print(f'Pushed number: {i}')

    print(myStack)

    print(f'Popped Number: {myStack.pop()}')

    print(myStack)
    print(myStack.peek())
    print(myStack)

"""rev1 = reversefile(try2)

print(rev1)"""