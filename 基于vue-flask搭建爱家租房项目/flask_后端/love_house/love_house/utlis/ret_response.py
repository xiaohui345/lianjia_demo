# -*- coding: utf-8 -*-
# @Author: 曾辉


class Baseresponse():

	def __init__(self):
		self.code = 1000
		self.data = {}
		self.error = None


	@property
	def dict(self):
		# 把类里面的所有数据按照字典的形式进行封装
		return self.__dict__



class dataresponse(Baseresponse):

	def __init__(self):
		super().__init__()
		self.data = []