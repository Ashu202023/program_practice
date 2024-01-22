import os
import subprocess

def main():
    fifo_path="my_fifo"
    try:
        os.mkfifo(fifo_path)
        pid=os.fork()
        if pid>0:
            print("parent process(ls -l):")
            with open(fifo_path,"w") as fifo_write:
                subprocess.run(["ls","-l"],stdout=fifo_write)
        elif pid==0:
            print("child process (sort):")
            with open(fifo_path,"r") as fifo_read:
                subprocess.run(["sort"],stdin=fifo_read)
        else:
            print("fork failed")
    except OSError as e:
        print("Error:",e)
        sys.exit(1)
    finally:
        os.remove(fifo_path)

if __name__=="__main__":
    main()
    
