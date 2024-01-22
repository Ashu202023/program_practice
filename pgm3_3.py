import os
import signal
def signal_handler(sig,frame):
    print("\server terminated")
    exit(0)

def server():
    well_known_fifo="server.fifo"
    os.mkfifo(well_known_fifo)
    signal.signal(signal.SIGINT,signal_handler)
    
    try:
        print("Server is running.wait for clients...")
        while True:
            with open(well_known_fifo,"r") as well_known_pipe:
                data=well_known_pipe.readline().strip()
                
                if not data:
                    continue
                
                client_fifo,message=data.split(":",1)
                
                with open(client_fifo,"w") as client_pipe:
                    client_pipe.write(message)
                    client_ppe.flush()
    finally:
        os.remove(well_known_fifo)
if __name__=="__main__":
    server()
