import threading

def print_hello_world(thread_num):
    for _ in range(5):
        print(f"Hello, World (thread {thread_num})")

def main():
    threads = []

    for i in range(10):
        thread = threading.Thread(target=print_hello_world, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

