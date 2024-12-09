from circularLinkedList import CircularQueue

cq = CircularQueue()
tasks = ["Task1", "Task2", "Task3", "Task4"]

# Enqueue tasks into the circular queue
for task in tasks:
    cq.enqueue(task)

# Perform round-robin task assignment
rounds = 3  # Number of rounds to simulate
for i in range(rounds):
    print(f"Round {i+1}:")
    # Get the current state of the queue
    current_tasks = cq.__str__()
    print("Current queue state:", current_tasks)

    # Simulate task processing
    for _ in range(cq.__len__()):
        task = cq.peek_top()
        print(f"Processing {task}")
        cq.rotate()
        

    # Optionally modify the queue after each round (e.g., remove completed tasks)
    # For this example, let's dequeue one task at the end of each round
    if not cq.is_empty():
        completed_task = cq.dequeue()
        print(f"Completed {completed_task}")

    print()  # Blank line for better readability