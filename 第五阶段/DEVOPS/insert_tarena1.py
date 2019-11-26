from dbconn import Session,Departments
# hr=Departments(dep_id=2,dep_name='运部')
# print(hr.dep_id)
# print(hr.dep_name)#此时还没有在数据库中创建记录，所以是none
# session=Session()#建立到数据库的会话连接
# session.add(hr)#真正向数据库中写入记录
# session.commit()
# session.close()
dev=Departments(dep_id=4,dep_name='开发部')
qa=Departments(dep_id=5,dep_name='测试部')
session=Session()
session.add_all([dev,qa])
session.commit()
session.close()