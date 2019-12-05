from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

def send_msg(sender,receiver,subject,msg):
    message=MIMEText(msg,'plain','utf8')
    message['From']=Header(sender,'utf8')#头部中的发件人
    message['To']=Header(receiver[0],'utf8')#头部中的收件人
    message['Subject']=Header(subject,'utf8')#头部中的主题
    smtp=SMTP('127.0.0.1')#创建SMTP对象
    smtp.sendmail(sender,receiver,message.as_string())#发送邮件
if __name__ == '__main__':
    sender = 'zzg@tedu.cn'  # 发件人
    receiver = ['root@localhost', 'zhangsan@localhost']  # 收件人
    subject='邮件测试'
    msg='这是python邮件测试\r\n'
    send_msg(sender,receiver,subject,msg)
