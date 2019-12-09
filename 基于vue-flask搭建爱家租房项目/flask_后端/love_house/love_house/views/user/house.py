# -*- coding: utf-8 -*-
# @Author: 曾辉
from flask.blueprints import Blueprint
from flask import make_response, session
from love_house.utlis.ret_response import Baseresponse
from love_house import models, db
import numpy as np
import redis
import random
from love_house.utlis.get_redis import POOL


uh = Blueprint('uh', __name__)


def house_list(n):
	'''
	获取房屋的数据
	:param n:  n为1 则为:国内二手房;n为2 则为:国内新房;n为3 则为:海外新房
	:return:
	'''
	data_list = db.session.query(models.House_info, models.House_category.category).join(models.House_category,
	                                                                                     models.House_info.id == models.House_category.house_id).filter(
		models.House_category.category == n).all()
	return data_list


def get_rand_n(data_list, redis_name):
	'''
	随机获取展示的房屋数据的index值
	:param data_list:
	:param redis_name:
	:return:
	'''
	t = list(np.random.randint(1, len(data_list),size=3))

	conn = redis.Redis(connection_pool=POOL)
	h_n = conn.get(redis_name)
	if not h_n:
		# 第一次进入
		conn.set(redis_name, '{}'.format(t), ex=60 * 60 * 5)  # ex s
	else:
		# 把字节变为字符串
		t = eval(h_n.decode('utf-8'))

	return t


@uh.route('/house', methods=['GET'])
def house():
	ret = Baseresponse()

	# 只拿国内新房的数据
	# 做连表
	old_data_list = house_list(1)
	new_data_list = house_list(2)
	abroad_data_list = house_list(3)
	n_t_list = get_rand_n(new_data_list, 'new_num')
	o_t_list = get_rand_n(old_data_list, 'old_num')
	a_t_list = get_rand_n(abroad_data_list, 'abroad_num')
	# 把index放入session中，为了保证一段时间的Index不变，传给前端展示的数据一定时间内不变
	ret.data = {'newhouse': [], 'abroad_newhouse': [], 'oldhouse': []}

	def data(h_obj):
		da = {
			'title': h_obj.title,
			'price': h_obj.price,
			'img': h_obj.img,
			'area': h_obj.area,
			'size': h_obj.size,
			'type': h_obj.type,
		}
		return da

	def ret_data(n_list,new_data_list,category):
		for t in n_list:
			r_da = data(new_data_list[t][0])
			if category ==1:
				ret.data['oldhouse'].append(r_da)
			if category ==2:
				ret.data['newhouse'].append(r_da)
			if category ==3:
				ret.data['abroad_newhouse'].append(r_da)

	ret_data(n_t_list,new_data_list,2)
	ret_data(o_t_list, old_data_list,1)
	ret_data(a_t_list, abroad_data_list,3)


	return make_response(ret.dict)
