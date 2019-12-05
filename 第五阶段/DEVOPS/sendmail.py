from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

#plain表示文本文件
message=MIMEText('这是python邮件测试','plain','utf8')
message['From']=Header('zzg','utf8')
message['To']=Header('root','utf8')
message['Subject']=Header('邮件测试','utf8')
sender='zzg@tedu.cn'
receiver=['root@localhost','zhangsan@localhost']
smtp=SMTP('127.0.0.1')
smtp.sendmail(sender,receiver,message.as_string())
