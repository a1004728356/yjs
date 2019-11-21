#多进程，父进程将自身资源拷贝一份，生成子进程。程序在子进程中运行。所以
#子进程和父进程都有各自独立的运行空间
#多线程，包含在一个进程内，多个工作线程共享一个进程资源。多线程没有僵尸问题
#GIL：全局解释器。GIL的存在，导致某一时刻，只能把一个线程交给CPU处理
#计算密集型程序：数据的提供不是问题，主要是CPU的效率，适合多进程
#IO密集型程序：CPU再快没有用，因为它获得不到想要的数据，适合py多线程
import time
import threading
def calc():
    result=0
    for i in range(50000000):
        result+=i
    print(result)
if __name__ == '__main__':
    start=time.time()
    t1 = threading.Thread(target=calc)
    t1.start()
    t2 = threading.Thread(target=calc)
    t2.start()
    t1.join()
    t2.join()
    end=time.time()
    print(end-start)