from dbconn import Departments,Session,Salary
session=Session()
qset=session.query(Departments).order_by(Departments.dep_id)
print(qset)#qset仅仅是一条sql语句
for dep in qset:
    print(dep)
for dep in qset:
    print('%s:%s' % (dep.dep_id,dep.dep_name))
###########################################################
qset2=session.query(Departments.dep_id,Departments.dep_name)
print(qset2)
for id,name in qset2:
    print(id,name)
###########################################################
qset3=session.query(Departments)[1:4]#返回的不是sql语句
print(qset3)
for i in qset3:
    print(i.dep_name)
###########################################################
qset4=session.query(Departments.dep_name).filter(Departments.dep_id==5)
print(qset4)
for i in qset4:
    print(i.dep_name)
###########################################################
qset5=session.query(
    Salary.data,Salary.emp_id,Salary.basic+Salary.awards
)
print(qset5)
for data,emp_id,sal in qset5:
    print('%s:%s:%s' % (data,emp_id,sal))
#############################################################
qset6=session.query(Departments.dep_id).filter(Departments.dep_name.in_(['测试部','开发部']))
print(qset6)#查询两个部门的ID号
for did in qset6:
    print(did)
#############################################################
qset7=session.query(Departments.dep_id).filter(~Departments.dep_name.in_(['运维部','开发部']))
print(qset7)#查询名字不是这两个部门的ID
for did in qset7:
    print(did)
#############################################################
from sqlalchemy import and_,or_,delete
from dbconn import Employees
qset8=session.query(Employees).filter(and_(Employees.gender=='male',Employees.dep_id==4))
print(qset8)
for emp in qset8:
    print(emp.emp_name)
qset9=session.query(Employees).filter(or_(Employees.gender=='male',Employees.dep_id==4))
print(qset9)
for emp in qset9:
    print(emp.emp_name)
##############################################################
qset10=session.query(Departments).order_by(Departments.dep_id)
print(qset10.all())#返回所有查询结果，组成列表
print(qset10.first())#只返回查询到的第一个结果
#print(qset10.one())#报错，one要求返回的结果只有一个
qset11=session.query(Departments).filter(Departments.dep_id==1)
print(qset11.one())
print(qset11.scalar())#调用one(),返回第一列
#############################################################
qset12=session.query(Departments).filter(Departments.dep_id.isnot(None)).order_by(Departments.dep_id)
print(qset12)
for i in qset12:
    print(i)
qset13=session.query(Departments).filter(Departments.dep_id.is_(None)).order_by(Departments.dep_id)
print(qset13)
for i in qset13:
    print(i)
##############################################################
#统计一共有几个部门
qset13=session.query(Departments).count()
print(qset13)
############################################################
#得到每个员工在哪个部门，部门使用名字，不用ID
qset14=session.query(Employees.emp_name,Departments.dep_name).join(Departments,Employees.dep_id==Departments.dep_id)
print(qset14.all())
#注意query()中先写Employees.emp_name,join()中就要先用Departments
#########################################################
#第一种修改记录的方法，通过查询语句的update方法
hr=session.query(Departments).filter(Departments.dep_name=='hr')
print(hr)
hr.update({'dep_name':'人力资源部'})
session.commit()
session.close()
###########################################################
hr=session.query(Departments).get(1)#获取主键是1的实例
print(hr)
hr.dep_name='人事部'
session.commit()
session.close
###########################################################
#删除ID为5的员工记录
# tom=session.query(Employees).get(5)
# session.delete(tom)
# session.commit()
# session.close()
session=Session()
#session.query(Employees).filter(Employees.emp_id==1).delete()
a=session.query(Employees).get(3)
#for i in a:
#       print(i)
#print(a)
session.delete(a)
session.commit()
session.close()
