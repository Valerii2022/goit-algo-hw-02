import queue
import random
import time

requests_queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    new_request = f"Request {request_id}"
    requests_queue.put(new_request)
    print(f"Generated: {new_request}")

def process_request():
    if not requests_queue.empty():
        current_request = requests_queue.get()
        print(f"Processing: {current_request}")
    else:
        print("No requests to process")

try:
    while True:
        generate_request()
        time.sleep(random.uniform(0.5, 2.0))  
        process_request()
        time.sleep(random.uniform(0.5, 2.0)) 
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
