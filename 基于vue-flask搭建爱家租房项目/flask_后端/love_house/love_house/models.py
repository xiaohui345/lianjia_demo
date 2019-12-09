# -*- coding: utf-8 -*-
# @Author: 曾辉


from sqlalchemy import Column,UniqueConstraint
from sqlalchemy import String,DateTime,ForeignKey,Integer
from love_house import db
from sqlalchemy.orm import relationship



#类名就相当于表名，而一个对象就相当于一行数据

class Userinfo(db.Model):
	__tablename__ = 'userinfo'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32),index=True,nullable=True)
	pwd = Column(String(32),nullable=True)
	# 类型要一致呀
	token_id = Column(Integer,ForeignKey('token.id'))

	#在表里面不生成字段，就是方便我们查询和添加数据
	token = relationship('Token', backref='ut')


class Token(db.Model):
	__tablename__ = 'token'

	id = Column(Integer, primary_key=True, autoincrement=True)
	token = Column(String(32),nullable=True)


# 房子的类别
class House_category(db.Model):
	__table_name = 'house_category'

	id = Column(Integer, primary_key=True, autoincrement=True)
	CATEGORY_LIST={"国内二手房":1,"国内新房":2,"海外新房":3}
	category = Column(Integer,nullable=True)
	house_id = Column(Integer, ForeignKey('house_info.id'))   #一对多

	#在表里面不生成字段，就是方便我们查询和添加数据
	h_info = relationship('House_info', backref='hinfo')


#房子的基本信息
class House_info(db.Model):
	__table_name = 'house_info'

	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(32),nullable=True)
	price = Column(Integer,nullable=True)
	area = Column(String(64),nullable=True)
	type = Column(String(64),nullable=True)
	size = Column(Integer,nullable=True)
	img = Column(String(64),nullable=True)
	allinfo = Column(Integer,ForeignKey('house_allinfo.id'))

	#city=Column(String(64),nullable=True,index=True)   #房屋对应的城市

	#在表里面不生成字段，就是方便我们查询和添加数据
	h_allinfo = relationship('House_allinfo', backref='hallinfo')

#房子的详细信息
class House_allinfo(db.Model):
	__table_name = 'house_allinfo'

	id = Column(Integer, primary_key=True, autoincrement=True)
	addr = Column(String(64),nullable=True)
