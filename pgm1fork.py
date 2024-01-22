import os
pid=os.fork()
if pid>0:
    print("i am parent process:")
    print("parent process id:", os.getpid())
    print("child process id:" ,pid)
    print("get owner id:",os.getuid())
    os.wait()
else:
    print("i am child process")
    print("i am child process",os.getpid())
    print("i am parent process",os.getppid())
