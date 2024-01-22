import os
def server():
    request_fifo="client_request_fifo"
    response_fifo="client_response_fifo"
    
    os.mkfifo(request_fifo)
    os.mkfifo(response_fifo)
    
    try:
        with open(request_fifo,"r") as request_pipe:
            file_name=request_pipe.read().strip()
            
            try:
                with open(file_name,"r") as file:
                    content=file.read()
            except FileNotFoundError:
                content="file not found"
        with open(response_fifo,"w") as response_pipe:
            response_pipe.write(content)
    finally:
        os.remove(request_fifo)
        os.remove(response_fifo)
if __name__=="__main__":
    server()
        
