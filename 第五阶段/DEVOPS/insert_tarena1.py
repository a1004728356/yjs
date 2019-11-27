from dbconn import Session,Departments,Employees,Salary
# hr=Departments(dep_id=2,dep_name='运部')
# print(hr.dep_id)
# print(hr.dep_name)#此时还没有在数据库中创建记录，所以是none
# session=Session()#建立到数据库的会话连接
# session.add(hr)#真正向数据库中写入记录
# session.commit()
# session.close()
# dev=Departments(dep_id=4,dep_name='开发部')
# qa=Departments(dep_id=5,dep_name='测试部')
# alice=Employees(emp_id=1,emp_name='alice',gender='male',birth_date='1980-01-12',email='a576860507@qq.com',dep_id='4')
# bob=Employees(emp_id=2,emp_name='bob',gender='male',birth_date='1911-01-12',email='a576860507@qq.com',dep_id='4')
# tom=Employees(emp_id=3,emp_name='tom',gender='male',birth_date='1990-01-12',email='a576860507@qq.com',dep_id='5')
# aaa=Employees(emp_id=4,emp_name='aaa',gender='male',birth_date='1991-01-12',email='a576860507@qq.com',dep_id='5')
aaa=Salary(auto_id=1,data='2019/11/27',emp_id='4',basic='10000',awards='2000')
#
#
#
#
session=Session()
# session.add_all([aaa,tom,bob,alice])
session.add(aaa)
session.commit()
session.close()