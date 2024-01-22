import os
import sys
def main():
    parent_to_child_pipe_read,parent_to_child_pipe_write=os.pipe()
    child_to_parent_pipe_read,child_to_parent_pipe_write=os.pipe()
    try:
        child_pid=os.fork()
        if child_pid>0:
            os.close(parent_to_child_pipe_read)
            os.close(child_to_parent_pipe_write)
            message_to_child="hello son,i am your parent"
            os.write(parent_to_child_pipe_write,message_to_child.encode())
            data_from_child=os.read(child_to_parent_pipe_read,100)
            print("parent received data from child",data_from_child.decode())
            os.close(parent_to_child_pipe_write)
            os.close(child_to_parent_pipe_read)
        elif child_pid==0:
            os.close(parent_to_child_pipe_write)
            os.close(child_to_parent_pipe_read)
            data_from_parent=os.read(parent_to_child_pipe_read,100)
            print("data recieved from parent:",data_from_parent.decode())
            
            message_to_parent="Hello , i am your son,you are my papa"
            os.write(child_to_parent_pipe_write,message_to_parent.encode())
            os.close(child_to_parent_pipe_write)
            os.close(parent_to_child_pipe_read)
        else:
            print("fork failed")
    except OSError as e:
        print("fork failed",e)
        sys.exit(1)
if __name__=="__main__":
    main()
         
