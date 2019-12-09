# -*- coding: utf-8 -*-
# @Author: 曾辉

import redis

class Config(object):
	#md5加盐方式
	SALT = 'qazwsx456789'

	DEBUG = False



class RedisDevelopmentConfig(Config):
	# SECRET_KEY = "dasdsadwdwd123"

	# redis的连接池
	# SESSION_TYPE = "redis"
	# RE_POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, password="zh4350697", max_connections=1000)
	# SESSION_REDIS = redis.Redis(connection_pool=RE_POOL)


	import datetime
	PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)  # 设置session过期时间


	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456789@127.0.0.1:3306/lianjiadb2?charset=UTF8MB4'
	SQLALCHEMY_POOL_SIZE = 10
	SQLALCHEMY_MAX_OVERFLOW = 2
	SQLALCHEMY_POOL_RECYCLE = -1
	SQLALCHEMY_POOL_TIMEOUT = 2

	SQLALCHEMY_TRACK_MODIFICATIONS = False   #将其设为True时，每次请求结束后都会自动提交数据库中的变动。
	#False 需要我们手动的进行commit()
