import time
import os
def calc():
    result=0
    for i in range(50000000):
        result+=i
    print(result)
if __name__ == '__main__':
    # start=time.time()
    # calc()
    # calc()
    # end=time.time()
    # print(end-start)
    #########################
    start=time.time()
    pid=os.fork()
    if not pid:
        calc()
        exit()
    pid = os.fork()
    if not pid:
        calc()
        exit()
    os.waitpid(-1,0)#处理子进程，挂起父进程
    os.waitpid(-1,0)
    end=time.time()
    print(end-start)