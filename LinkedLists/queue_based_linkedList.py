class Empty(Exception):
    pass

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

    def enqueue(self,data): #add new node to the top
        new_entry = Node(data, None)
        if self.is_empty():
            self.head = new_entry
        else:
            self.tail.next = new_entry
        self.tail = new_entry
        self.size += 1

    def prepend(self, data): #for priority adds
        """ i didnt take care of the tail tho. it might cause some issues later"""
        new_entry = Node(data,None)
        if self.is_empty():
            self.head = new_entry
        new_entry.next = self.head
        self.head = new_entry


    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        else:
            current_node = self.head.data
            self.head = self.head.next
            self.size -= 1
            if self.is_empty():
                self.tail = None

            return current_node

    def peek_top(self):
        current_node = self.head
        if self.is_empty():
            raise Empty("Queue is Empty")
        else:
            return current_node.data
    
    def peek_last(self):
        current_node = self.tail
        if self.is_empty():
            raise Empty("Queue is Empty")
        else:
            return current_node.data
        
my_new_queue = QueueLinkedList()

numbers2 = (12,4,0,4,27)

for number in numbers2:
    my_new_queue.enqueue(number)

print(f'the first element: {my_new_queue.peek_top()} and the last : {my_new_queue.peek_last()}')
my_new_queue.dequeue()  
"""my_new_queue.prepend(10)  
my_new_queue.enqueue(10) """ 
print(f'the first element: {my_new_queue.peek_top()} and the last : {my_new_queue.peek_last()}')