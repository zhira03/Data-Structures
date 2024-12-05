class Empty(Exception):
    pass

class LinkedStack:
    """
    FILO: first in Last out 
    """
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
        
    def is_empty(self):
        return self.size == 0
    
    def push(self,data):
        self.head = self.Node(data)
        self.size += 1

    def peek_top(self):
        current_node = self.head
        while not self.is_empty():
            return current_node.data
        else:
            raise Empty("Stack is empty")
    
    def peek_last(self):
        last = self.head = (None)
        last_node = last
        while not self.is_empty():
            return last_node.data
        else:
            raise Empty("Stack is empty")
        
    def pop(self):
        while not self.is_empty():
            current_node = self.head
            self.head = self.head.next
            self.size -= 1
            return current_node
    
    def show(self):
        elements = []
        current_node = self.head
        while self.size != 0:
            elements.append(current_node)
            current_node = current_node.next
        return elements

my_new_stack = LinkedStack()

numbs = [1,2,3,4,5,6,7,8,9,10,11]

for number in numbs:
    my_new_stack.push(number)

print(my_new_stack.peek_top())
print(my_new_stack.peek_last())