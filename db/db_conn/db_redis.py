#!/usr/bin/env python
#coding=utf-8

from db.db_conn.db_conf import REDIS_CONFIG
import redis

pool = redis.ConnectionPool(host=REDIS_CONFIG["ip"], port=REDIS_CONFIG["port"], db=0)
session_redis = redis.Redis(connection_pool=pool)