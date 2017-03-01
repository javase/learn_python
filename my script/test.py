# -*- coding: utf-8 -*-
import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'tb_account_user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    nickname = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://healthcloud:healthcloud123456@10.1.64.80:9035/vaccine_server_core')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
# 添加到session:
# session.add(new_user)
# 提交即保存到数据库:
# session.commit()
# 关闭session:
# session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='b1f01dc5d88c4bd885053d71d7449c0a').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('nickname:', user.nickname)
# 关闭Session:
session.close()