import threading
import time
import queue

BUFFER_SIZE = 3000000
NUM_PRODUCERS = 4
NUM_CONSUMERS = 4

buffer = queue.Queue(BUFFER_SIZE)
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

def producer():
    while True:
        empty.acquire()
        mutex.acquire()

        buffer.put('X')

        mutex.release()
        full.release()

def consumer():
    while True:
        full.acquire()
        mutex.acquire()

        item = buffer.get()

        mutex.release()
        empty.release()

        # Process the consumed item (e.g., print it)
        print(item, end='', flush=True)

def main():
    # Create producer threads
    producer_threads = [threading.Thread(target=producer) for _ in range(NUM_PRODUCERS)]

    # Create consumer threads
    consumer_threads = [threading.Thread(target=consumer) for _ in range(NUM_CONSUMERS)]

    # Start producer threads
    for thread in producer_threads:
        thread.start()

    # Start consumer threads
    for thread in consumer_threads:
        thread.start()

    # Sleep for some time (e.g., 10 seconds) to allow producers and consumers to run
    time.sleep(10)

    # Stop producer threads
    for thread in producer_threads:
        thread.join(timeout=0)

    # Stop consumer threads
    for thread in consumer_threads:
        thread.join(timeout=0)

if __name__ == "__main__":
    main()

