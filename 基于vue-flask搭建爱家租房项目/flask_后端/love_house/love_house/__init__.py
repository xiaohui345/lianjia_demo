# -*- coding: utf-8 -*-
# @Author: 曾辉
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy




#实例化SQLAlchemy对象
db = SQLAlchemy()


#导入所有的类，从而在数据库中生成表
from love_house.models import *

#导入蓝图
from love_house.views.account.login import al
from love_house.views.account.register import ar
from love_house.views.user.house import uh
from love_house.views.user.all_house import all_h


def create_app():

	app = Flask(__name__)

	app.config.from_object('settings.RedisDevelopmentConfig')


	#注册蓝图
	app.register_blueprint(al)
	app.register_blueprint(ar)
	app.register_blueprint(uh)
	app.register_blueprint(all_h)
	#初始化之前需要先加载配置文件
	#初始化 (对取app里面的配置文件，读取数据库的连接)
	db.init_app(app)


	# 回去的时候给响应加上响应头，避免发生跨域;
	@app.after_request
	def hander_cors(response):
		response.headers['Access-Control-Allow-Origin'] = '*'

		if request.method == 'OPTIONS':

			response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

			response.headers['Access-Control-Allow-Methods'] = 'DELETE,PUT'

		return response

	return app