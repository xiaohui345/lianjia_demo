# -*- coding: utf-8 -*-
# @Author: 曾辉
import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379,password="zh4350697", max_connections=1000)
