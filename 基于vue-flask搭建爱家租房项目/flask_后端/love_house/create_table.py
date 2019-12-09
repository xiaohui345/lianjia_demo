# -*- coding: utf-8 -*-
# @Author: 曾辉

#生成表，需要用到 appy 应用上文管理
import pandas as pd

from love_house import create_app,db,models

app = create_app()

app_ctx = app.app_context()


with app_ctx:
	# with 对象 的时候就会自动的触发类的__enter__ 方法,然后执行下面的代码，最后执行__exit__

	#创建表
	db.create_all()
	# db.drop_all()

	# 自动手动的操作choice
	data = pd.read_csv('love_house/utlis/data/houseinfo.csv',encoding='gbk',usecols=['xiaoqu','jiedaohao','size','price(万)','img','type'])
	# print(data.head(),type(data.head()))
	data_list = data.to_dict(orient='records')   #将dataframe转变为字典

	# print(da,type(da))[{},{}]

	obj_list = []
	for k in data_list:
		#k 就是代表一行数据
		addr = k['jiedaohao']
		housea_allinfo_obj = models.House_allinfo(addr=addr)

		title = k['xiaoqu']
		price = k['price(万)']
		area = k['jiedaohao']
		size = k['size']
		type = k['type']
		img = '/static/img/'+ k['img']
		house_info_obj = models.House_info(title=title,price=price,area=area,size=size,type=type,img=img,h_allinfo=housea_allinfo_obj)
		obj = models.House_category(category=models.House_category.CATEGORY_LIST.get('国内新房'), h_info=house_info_obj)
		obj_list.append(obj)


	db.session.add_all(obj_list)

	db.session.commit()
	db.session.close()