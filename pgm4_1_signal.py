import signal
import time
def signal_handler(signum,frame):
    signal_names={
    signal.SIGINT:"SIGINT",
    signal.SIGHUP:"SIGHUP",
    signal.SIGTERM:"SIGTERM",
    signal.SIGQUIT:"SIGQUIT"}
    
    if signum in signal_names:
        print(f"Received signal: {signal_names[signum]}")
        if signum==signal.SIGQUIT:
            exit(0)

def main():
    signal.signal(signal.SIGINT,signal_handler)
    signal.signal(signal.SIGHUP,signal_handler)
    signal.signal(signal.SIGTERM,signal_handler)
    signal.signal(signal.SIGQUIT,signal_handler)
    
    print("program is running.Press Ctrl+c to interrupt or send signals")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Exiting programs")
    
if __name__=="__main__":
   main()
        
