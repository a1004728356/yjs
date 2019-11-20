import os
import time

pid = os.fork()
if pid:
    print('in parent,sleeping...')
    time.sleep(20)
    os.waitpid(-1.1)  # 收拾子进程，如果子进程是僵尸进程，就释放它
                        # 如果不是，父进程不做任何动作，继续向下执行
    time.sleep(60)
else:
    print('in child,sleeping')
    time.sleep(15)
