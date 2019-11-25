import pymysql
conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',passwd='123456',db='tedu',charset='utf8'
)
cursor=conn.cursor()

query1='select * from departments'
cursor.execute(query1)
cursor.scroll(1,mode='absolute')#绝对，以开头为起始点移动游标
cursor.fetchone()#取出一行
cursor.scroll(1,mode='relative')#以当前位置为参考点移动游标
r2=cursor.fetchall()#取出后续所有内容
print(r2)

cursor.close()
conn.close()
# ((4, '测试部'),)