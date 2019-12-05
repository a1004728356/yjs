from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

#plain表示文本文件
message=MIMEText('这是python邮件测试','plain','utf8')
message['From']=Header('zzg','utf8')#头部中的发件人
message['To']=Header('root','utf8')#头部中的收件人
message['Subject']=Header('邮件测试','utf8')#头部中的主题
sender='zzg@tedu.cn'#发件人
receiver=['root@localhost','zhangsan@localhost']#收件人
smtp=SMTP('127.0.0.1')#创建SMTP对象
smtp.sendmail(sender,receiver,message.as_string())#发送邮件
