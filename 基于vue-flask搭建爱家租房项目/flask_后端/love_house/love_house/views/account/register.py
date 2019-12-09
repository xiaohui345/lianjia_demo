# -*- coding: utf-8 -*-
# @Author: 曾辉
from flask import request, make_response
from flask.blueprints import Blueprint
from love_house.utlis.ret_response import Baseresponse
from love_house.utlis.pwd_hashlib import pwd_md5
from love_house.utlis.get_token import token
from love_house import db, models

ar = Blueprint('ar', __name__)


@ar.route('/register', methods=['POST'])
def register():
	ret = Baseresponse()

	try:
		login_data = request.get_json()  # get_json()获取json数据，并且已经帮我们序列化了.
		username = login_data.get('username')
		password = login_data.get('password')

		u1 = db.session.query(models.Userinfo).filter_by(name=username).first()
		if u1:
			ret.code = 1001
			ret.error = '用户名已存在'
			return make_response(ret.dict)

		# 加密后的pwd返回的是一串字符串,要跟表里面的格式一致;
		md5_pwd = pwd_md5(username, password)
		tk = token()
		token_obj = models.Token(token=tk)
		user_obj = models.Userinfo(name=username, pwd=md5_pwd, token=token_obj)

		db.session.add(user_obj)

		db.session.commit()

		ret.data = {
			'username': username,
			'token': tk
		}

		return make_response(ret.dict)

	except Exception:
		ret.code = 1003
		return make_response(ret.dict)
