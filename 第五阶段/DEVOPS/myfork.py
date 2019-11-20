import os

# print('...')
# os.fork()  # 生成子进程，后续代码将在父子进程中同时运行
# print('hello world')

# print('starting...')
# a = os.fork()  # 父进程返回值是子进程的pid，子进程的pid是0
# if a:
#     print('in parents')
# else:
#     print('in child')
# print('done')
# # starting...
# # in parents
# # done
# # in child
# # done

for i in range(3):
    a = os.fork()  # 父进程用来生成子进程
    if not a:  # 只有子进程才执行
        print('hello')
        exit()  # 子进程遇到exit结束，不会遇到循环条件处
