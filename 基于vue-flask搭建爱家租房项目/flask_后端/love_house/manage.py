# -*- coding: utf-8 -*-
# @Author: 曾辉
from love_house import create_app


app = create_app()


if __name__=='__main__':
	app.run()
	# app.__call__