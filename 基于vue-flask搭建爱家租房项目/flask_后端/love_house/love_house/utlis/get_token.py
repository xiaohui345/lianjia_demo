# -*- coding: utf-8 -*-
# @Author: 曾辉
import uuid


def token():
	token = str(uuid.uuid4())

	return token[-10:]




