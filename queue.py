class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)


ticket_queue = Queue()

ticket_queue.enqueue("Customer 1")
ticket_queue.enqueue("Customer 2")
ticket_queue.enqueue("Customer 3")

print("Current Queue:", ticket_queue.items)
next_customer = ticket_queue.peek()
print("Next Customer:", next_customer)
served_customer = ticket_queue.dequeue()
print(f"Serving Customer: {served_customer}")
print("Updated Queue:", ticket_queue.items)
