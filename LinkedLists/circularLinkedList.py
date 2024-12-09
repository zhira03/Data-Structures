class CircularQueue:

    class Empty(Exception):
        pass

    class Node:
        def __init__(self, data , next) -> None:
            self.data =data
            self.next = next
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def peek_top(self):
        current_node = self.tail.next
        if self.is_empty():
            raise self.Empty("Queue is Empty")
        else:
            return current_node.data

    def peek_last(self):
        current_node = self.tail
        if self.is_empty():
            raise self.Empty("Queue is Empty")
        else:
            return current_node.data
        
    def dequeue(self):
        if self.is_empty():
            raise self.Empty("Queue is Empty")
        
        prev_head = self.tail.next

        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = prev_head.next
        self.size -= 1
        return prev_head.data
    
    def enqueue(self, data):
        new_entry = self.Node(data, None)
        if self.is_empty():
            new_entry.next = new_entry
        else:
            new_entry.next = self.tail.next
            self.tail.next = new_entry
        self.tail = new_entry
        self.size += 1
    
    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next

    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        result = []
        current = self.tail.next
        for _ in range(self.size):
            result.append(current.data)
            current = current.next  
        return f"CircularQueue: {result}"





        
        