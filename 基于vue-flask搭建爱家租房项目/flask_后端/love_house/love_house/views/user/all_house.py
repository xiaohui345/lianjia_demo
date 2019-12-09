# -*- coding: utf-8 -*-
# @Author: 曾辉
'''
这是获取所有二手房和新房数据的api
'''
from flask import make_response
from love_house.utlis.ret_response import Baseresponse
from love_house import models, db
from flask.blueprints import Blueprint


all_h = Blueprint('all_h',__name__)

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


@all_h.route('/ershoufang/<string:cityname>',methods=['GET'])
def ershoufang(cityname):
	if cityname:
		city_name =cityname
	else:
		city_name = '北京'    #表示用户没有选择城市，就是默认的北京

	print(city_name)
	#然后把城市作为数据库查找的一个条件
	ret = Baseresponse()

	all_data_list = house_list(1)

	ret.data = {
		'ershoufang':[]
	}

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

	for obj in all_data_list:
		ret.data['ershoufang'].append(data(obj[0]))

	return make_response(ret.dict)



@all_h.route('/xinfang',methods=['GET'])
def xinfang():

	ret = Baseresponse()

	all_data_list = house_list(2)

	ret.data = {
		'xinfang':[]
	}

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

	for obj in all_data_list:
		ret.data['xinfang'].append(data(obj[0]))

	return make_response(ret.dict)