import os
def client():
    request_fifo="client_request_fifo"
    response_fifo="client_response_fifo"
    
    os.mkfifo(request_fifo)
    os.mkfifo(response_fifo)
    
    try:
        file_name=input("enter the file name:")
        with open(request_fifo,"w") as request_pipe:
            request_pipe.write(file_name)
        
        with open(response_fifo,"r") as response_pipe:
            response_pipe.write(file_name)
        
    finally:
        os.remove(request_fifo)
        os.remove(response_fifo)
if __name__=="__main__":
    client()
