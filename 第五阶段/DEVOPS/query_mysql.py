import pymysql
conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',passwd='123456',db='tedu',charset='utf8'
)
cursor=conn.cursor()

query1='select * from departments'
cursor.execute(query1)
r1=cursor.fetchone()
print(r1)
r2=cursor.fetchmany(2)
print(r2)
r3=cursor.fetchall()
print(r3)

cursor.close()
conn.close()
# (1, '人事部')
# ((2, '运维部'), (3, '开发部'))
# ((4, '测试部'),)