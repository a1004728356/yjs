# pip3 install paramiko
import paramiko
ssh=paramiko.SSHClient()#可以认为创建的是一个ssh的客户端，实际是一个实例
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)#意思是回答yes
ssh.connect('192.168.16.63',username='root',password='123456')
ssh.exec_command('mkdir /tmp/demo')#想使用的命令
result=ssh.exec_command('id zhangsan')
print(result[2].read().decode('utf8'))
#执行命令后，返回值是一个元组，元组中的三项都是类文件对象，分别代表了标准输入、标准输出和标准错误
ssh.close()