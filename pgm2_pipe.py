import os
def main():
    parent_read,child_write=os.pipe()
    try:
       child_pid=os.fork()
       
       if child_pid>0:
           os.close(child_write)
           data=os.read(parent_read,100)
           print(f"parent received data from child:{data.decode()}")
           os.close(parent_read)
       elif child_pid==0:
           os.close(parent_read)
           message="hello from the world"
           os.write(child_write,message.encode())
           os.close(child_write)
       else:
           print("fork failed")
    except OSError as e:
        
        print("fork failed:",e)
        sys.exit(1)
if __name__=="__main__":
    main()
