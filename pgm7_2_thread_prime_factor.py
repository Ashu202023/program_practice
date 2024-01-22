import threading
import sys

def calculate_prime_factors(number, result):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            result.append(i)
    if number > 1:
        result.append(number)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py number1 number2 ...")
        return

    numbers = [int(arg) for arg in sys.argv[1:]]
    threads = []

    for number in numbers:
        result = []
        thread = threading.Thread(target=calculate_prime_factors, args=(number, result))
        threads.append((number, thread, result))
        thread.start()

    for number, thread, result in threads:
        thread.join()
        print(f"Original Number: {number}, Prime Factors: {result}")

if __name__ == "__main__":
    main()
    
    #python script.py 24 36 42


