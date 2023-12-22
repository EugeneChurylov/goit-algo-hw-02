from queue import Queue
import time

q = Queue()

def generate_request():
    global q
    q.put('Request')
    print("New request generated")
    time.sleep(2)

def process_request():
    global q
    if not q.empty():
        request = q.get()
        print(f"Processing: {request}")
    else:
        print("The queue is empty")
    time.sleep(2)

while True:
    generate_request()
    process_request()

