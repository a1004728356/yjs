import pymysql
conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',passwd='123456',db='tedu',charset='utf8'
)
cursor=conn.cursor()
insert_dep1='update departments set dep_name=%s where dep_name=%s'
cursor.execute(insert_dep1,('人力资源部','人事部'))
delete1='delete from departments where dep_name=%s'
cursor.execute(delete1,('测试部',))
conn.commit()

cursor.close()
conn.close()