# -*- coding: utf-8 -*-
# @Author: 曾辉

import hashlib
import settings




def pwd_md5(username,pwd):
	md5 = hashlib.md5(settings.Config.SALT.encode('utf-8') + bytes(username[:2],encoding='utf-8'))
	md5.update(bytes(pwd,encoding='utf-8'))


	return md5.hexdigest()