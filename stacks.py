"""
FILO: first in Last out 
"""
class Stack():
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
    


myStack = Stack()

numbers = 12 , 4 , 4,27

for i in numbers:
    myStack.push(i)
    print(f'Pushed number: {i}')

print(myStack)

print(f'Popped Number: {myStack.pop()}')

print(myStack)
print(myStack.peek())
print(myStack)
