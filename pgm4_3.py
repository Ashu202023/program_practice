import os
import signal
import time
import sys

def sigchld_handler(signum, frame):
    # The handler for SIGCHLD
    # Wait for the child process to get its exit status
    pid, exit_status = os.wait()
    print(f"Received SIGCHLD. Child process {pid} terminated with exit status: {exit_status}")

def main():
    # Set the signal handler for SIGCHLD
    signal.signal(signal.SIGCHLD, sigchld_handler)

    # Fork a child process
    pid = os.fork()

    if pid == 0:
        # This is the child process
        print(f"Child process {os.getpid()} is running.")
        time.sleep(2)
        sys.exit(42)  # Child process exits with exit status 42

    else:
        # This is the parent process
        print(f"Parent process {os.getpid()} is running. Waiting for SIGCHLD...")

        # The parent process will wait for the child to terminate
        while True:
            try:
                # Sleep to allow time for the child process to terminate
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nParent process interrupted. Exiting.")
                break

if __name__ == "__main__":
    main()

