import os
def client(client_id):
    well_known_fifo="server_fifo"
    client_fifo=f"client_{client_id}_fifo"
    os.mkfifo(client_fifo)
    
    try:
        with open(well_known_fifo,"w") as well_known_pipe:
            while True:
                message=input("enter a message(type 'exit' to quit):")
                if message.lower()=="exit":
                    break
                
                well_known_pipe.write(f"{client_fifo}:{message}\n")
                well_known_pipe.flush()
                
                with open(client_fifo,"r") as client_pipe:
                    echoed_message=client_pipe.read()
                    print(f"Server echoed: {echoed_message.strip()}")
    
    finally:
        os.remove(client_fifo)

if __name__=="__main__":
    client_id=input("enter client id :") 
    client(client_id)           
