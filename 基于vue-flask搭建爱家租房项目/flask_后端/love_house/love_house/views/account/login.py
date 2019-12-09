# -*- coding: utf-8 -*-
# @Author: 曾辉
from flask import request, make_response,session
from flask.blueprints import Blueprint
from love_house.utlis.ret_response import Baseresponse
from love_house.utlis.pwd_hashlib import pwd_md5
from love_house import db, models


al = Blueprint('al', __name__)


@al.route('/login', methods=['POST'])
def login():
	ret = Baseresponse()
	try:
		login_data = request.get_json()  # get_json()获取json数据，并且已经帮我们序列化了.
		username = login_data.get('username')
		password = login_data.get('password')

		md5_pwd = pwd_md5(username, password)

		# filter_by 关键字传参
		user_obj = db.session.query(models.Userinfo).filter_by(name=username, pwd=md5_pwd).first()

		if user_obj:
			token_obj = db.session.query(models.Token).filter_by(id=user_obj.token_id).first()
			ret.data={'username' :user_obj.name,
			          'token' : token_obj.token}

			return make_response(ret.dict)

		ret.code = 1001
		ret.error = '用户名或者是密码错误!'
		return make_response(ret.dict)

	except Exception:
		ret.code = 1003
		return make_response(ret.dict)
