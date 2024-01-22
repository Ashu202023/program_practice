import multiprocessing
import random
import time
import sys

# Function to perform operations in child processes
def child_process(shared_variable, semaphore):
    for _ in range(5):
        # Sleep for a random amount of time
        time.sleep(random.uniform(0, 0.5))

        # Acquire the semaphore for mutual exclusion
        semaphore.acquire()

        # Read the shared variable
        current_value = shared_variable.value

        # Modify the shared variable based on the process
        if multiprocessing.current_process().name == 'Process-A':
            shared_variable.value = current_value + 200
        elif multiprocessing.current_process().name == 'Process-B':
            shared_variable.value = current_value + 100

        # Release the semaphore
        semaphore.release()

# Main function
def main():
    # Check if enough command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <shared_memory_key>")
        return

    # Get the shared memory key from command line arguments
    shared_memory_key = int(sys.argv[1])

    # Create shared memory with multiprocessing.Value
    shared_variable = multiprocessing.Value('i', 1000)

    # Create a semaphore for mutual exclusion
    semaphore = multiprocessing.Semaphore()

    # Create processes
    process_a = multiprocessing.Process(target=child_process, args=(shared_variable, semaphore), name='Process-A')
    process_b = multiprocessing.Process(target=child_process, args=(shared_variable, semaphore), name='Process-B')

    # Start the processes
    process_a.start()
    process_b.start()

    # Wait for the processes to finish
    process_a.join()
    process_b.join()

    # Print the final result
    print("Final value of shared variable:", shared_variable.value)

if __name__ == "__main__":
    main()
    
    #python script.py 1234


