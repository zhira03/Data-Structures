from Stacks.stacks import Empty

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

    def append(self,data): #adds new nodes to the end of the list
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
        # Special case: if the head contains the target data
        if self.head and self.head.data == data:
            self.head = self.head.next  # Remove the head node
            return
        
        # Traverse the list to find the node to delete
        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data == data:  # Found the target node
                current_node.next = current_node.next.next  # Remove it
                return
            current_node = current_node.next

    def show(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements

    def get(self,index):
        if index >= self.length():
            print("Index out of Bounds")
            return None
        current_index = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            if current_index == index : return current_node.data
            current_index += 1

    def length(self):
        current_node = self.head
        sum = 0
        while current_node.next != None:
            sum += 1
            current_node = current_node.next
        return sum
    

linked1 = LinkedList()

numbers = [1,2,3,4,5,6,7,8,9,10,11]

for number in numbers:
    linked1.append(number)

print(f'Initial LinkedList: {linked1.show()}')
linked1.delete(5)
print(f'Final LinkedList: {linked1.get(8)}')
