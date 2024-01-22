import signal
import time

# Counter to keep track of the number of alarms triggered
alarm_count = 0

# Signal handler for SIGALRM
def alarm_handler(signum, frame):
    global alarm_count
    print(f"Received SIGALRM {alarm_count + 1}")
    alarm_count += 1

    # Set the alarm again if not reached the maximum count
    if alarm_count < 5:
        signal.alarm(2)
    else:
        print("Maximum alarm count reached. Exiting.")
        exit()

# Set the SIGALRM signal handler
signal.signal(signal.SIGALRM, alarm_handler)

if __name__ == "__main__":
    try:
        # Get the user input for alarm duration
        alarm_duration = int(input("Enter the alarm duration in seconds: "))
        
        # Set the initial alarm
        signal.alarm(alarm_duration)

        # Run an infinite loop to keep the program alive
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

