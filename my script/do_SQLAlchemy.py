# -*- coding: utf-8 -*-
# 导入
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义对象
class User(Base):
	# 表的名字
	__table__ = 'tb_account_user'
	
	# 表结构
	id = Column(String)
	password = Column(String)
	nickname = Column(String)
	mobile = Column(String)
	avatar = Column(String)
	gender = Column(String)
	#birthday = Column(String(50))
	#join_time= Column(DateTime, default='0000-00-00')
	talkid = Column(String)
	talkpwd= Column(String)
	channel= Column(String)
	#is_bbs_admin = Column(String(50))
	#ban_status = Column(String(50))
	del_flag = Column(String)
	#create_time= Column(DateTime, default='0000-00-00')
	#update_time= Column(DateTime, default='0000-00-00')
	address= Column(String)
	
# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://healthcloud:healthcloud123456@10.1.64.80:9035/vaccine_server_core')	
# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)
# 查询
session = DBSession()
# 创建Query查询，filter是where条件，子厚调用one()返回唯一行,如果调用all()则返回所有行：
# accountUser = session.query(AccontUser).filter(AccontUser.id = 'b1f01dc5d88c4bd885053d71d7449c0a').one()
# 打印类型和对象
# print(accountUser)