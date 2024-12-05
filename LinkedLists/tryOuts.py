from circularLinkedList import CircularQueue

my_new_queue = CircularQueue()
my_new_queue2 = CircularQueue()

numbers2 = [1,2,3,4,5,6,7,8,9,10,11]


for number in numbers2:
    my_new_queue.enqueue(number)

print(f'the first element: {my_new_queue.peek_top()} and the last : {my_new_queue.peek_last()}')
my_new_queue.rotate()
print(f'the first element: {my_new_queue.peek_top()} and the last : {my_new_queue.peek_last()}')

names = ['Taku', 'Mama', 'Linda', 'Joey', 'Rudo', 'Tendai']
updated = []

for name in names:
    my_new_queue2.enqueue(name)
updated = my_new_queue2.rotate()
#print(f'the first element: {my_new_queue2.peek_top()} and the last : {my_new_queue2.peek_last()}')
print(str(my_new_queue2.rotate()))

