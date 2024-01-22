import threading
import math

def calculate_square_roots(start, end, results):
    for i in range(start, end):
        results[i] = math.sqrt(i)

def main():
    # Define the range of integers
    start = 0
    end = 100

    # Create an array to store the results
    results = [0.0] * (end - start)

    # Create a thread to calculate square roots
    square_root_thread = threading.Thread(target=calculate_square_roots, args=(start, end, results))

    # Display a short message in the main thread
    print("Calculating square roots in a separate thread. Please wait...")

    # Start the thread
    square_root_thread.start()

    # Wait for the thread to complete
    square_root_thread.join()

    # Display the results in the main thread
    for i, result in enumerate(results):
        print(f"Square root of {start + i}: {result}")

if __name__ == "__main__":
    main()

