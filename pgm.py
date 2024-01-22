import os
pid=os.fork()
if pid>0:
    print("i am parent process")
    print("process ID:",os.getpid())
    print("Child process ID:",pid)
else:
    print("i am child process")
    print("process ID:",os.getpid())
    print("process ID:",os.getppid())
