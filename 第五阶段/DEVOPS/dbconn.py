#pip3 install sqlalchemy
#create database tarena default charset='utf8';
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine=create_engine(
    'mysql+pymysql://root:123456@localhost/tarena?charset=utf8',encoding='utf8'#echo=True
)
#mysql+pymysql://用户名:密码@主机/库名
Base=declarative_base()#创建ORM所需的基类
Session=sessionmaker(bind=engine)

class Departments(Base):
    __tablename__='departments'#库中表名
    dep_id=Column(Integer,primary_key=True)#dep_id是表中字段
    dep_name=Column(String(20),unique=True)#dep_name是字段

    def __str__(self):
        return '[%s:%s]' % (self.dep_id,self.dep_name)
if __name__ == '__main__':
    Base.metadata.create_all(engine)#没有时创建，已有不创建