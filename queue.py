
# # Queue using list

# stock_price_queue = []

# stock_price_queue.insert(0,11.1)
# stock_price_queue.insert(0,111.22)
# stock_price_queue.insert(0,113.12)

# print(stock_price_queue)

# stock_price_queue.pop()


# # Queue using collection stack

# from collections import deque

# q = deque()

# q.appendleft(1)
# q.appendleft(4)
# q.appendleft(3)
# q.appendleft(2)

# print(q)


# queue class
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, x):
        self.buffer.appendleft(x)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
 
    def size(self):
        return len(self.buffer)


# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

# Food Order System Using Queue
"""
import time
import threading

food_order_queue = Queue()

def place_order(orders):
    for order in orders:
        print("Placing order for", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        print("Serving", order)
        time.sleep(2)


if __name__=="__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    thread1 = threading.Thread(target=place_order, args=(orders,))
    thread2 = threading.Thread(target=serve_order)
    thread1.start()
    thread2.start()
"""

# Printing 10 binary numbers

def generate_binary_number():
    binary_queue = Queue()
    val = "1"
    binary_queue.enqueue(val)

    for x in range(10):
        num = binary_queue.dequeue()
        binary_queue.enqueue(num+"0")
        binary_queue.enqueue(num+"1")

        print(num)

if __name__=="__main__":
    generate_binary_number()