import threading
import time
import random
import queue

NUM_MEASURES = 100
NUM_MUSICIANS = random.randint(3, 10)

mutex = threading.Semaphore(1)
sem_measure = threading.Semaphore(0)
sem_sleep = threading.Semaphore(0)
sleeping_musicians = set()

def play_musician(musician_id):
    global sleeping_musicians
    for measure in range(1, NUM_MEASURES + 1):
        # Simulate 25% chance of falling asleep
        if random.random() < 0.25:
            sleep_duration = random.randint(1, 5)
            mutex.acquire()
            sleeping_musicians.add(musician_id)
            mutex.release()
            print(f"MEASURE {measure}: Musician {musician_id} is sleeping for {sleep_duration} measures")
            time.sleep(sleep_duration)
            mutex.acquire()
            sleeping_musicians.remove(musician_id)
            mutex.release()
            print(f"Musician {musician_id} woke up")

        # Simulate playing a measure
        mutex.acquire()
        print(f"MEASURE {measure}: Musician {musician_id} playing", end=' ')
        for other_musician in range(1, NUM_MUSICIANS + 1):
            if other_musician != musician_id and other_musician not in sleeping_musicians:
                print(f"Musician {other_musician} playing", end=' ')
        print()
        mutex.release()

        time.sleep(1)  # Simulate playing a measure

def conductor():
    for measure in range(1, NUM_MEASURES + 1):
        sem_measure.release()
        time.sleep(1)  # Conductor signaling measure change

def main():
    musician_threads = []
    
    for musician_id in range(1, NUM_MUSICIANS + 1):
        thread = threading.Thread(target=play_musician, args=(musician_id,))
        musician_threads.append(thread)
        thread.start()

    conductor_thread = threading.Thread(target=conductor)
    conductor_thread.start()

    for measure in range(1, NUM_MEASURES + 1):
        sem_measure.acquire()
        time.sleep(1)  # Wait for musicians to finish playing the measure

    # Wait for musician threads to finish
    for thread in musician_threads:
        thread.join()

    # Wait for conductor thread to finish
    conductor_thread.join()

if __name__ == "__main__":
    main()

