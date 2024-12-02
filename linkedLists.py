from stacks import Empty

"""
starting with the easy singly list

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data): #adds new noodes to the end of the list
        new_node =  Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def pre_append(self,data):#adds new nodes to the head of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self,data):
        while self.head != None:
            if self.head == data:
                self.head = self.head.next
                return
            current_node = self.head
            while current_node.next and current_node.next.data != data:
                current_node = current_node.next
            if current_node.next:
                current_node.next = current_node.next.next

    def show(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print (elements)

    def length(self):
        current_node = self.head
        sum = 0
        while current_node.next != None:
            sum += 1
            current_node = current_node.next
        return sum
    

linked1 = LinkedList()

numbers = [1,2.3,4,5,6,7,8,9,10,11]

for number in numbers:
    linked1.append(number)

linked1.show()
linked1.delete(5)
linked1.show()