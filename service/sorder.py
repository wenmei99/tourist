# !/usr/bin/python
# -*- coding: utf-8 -*-
from db.db_opr import db_order
import cfg


def getAllOrder(**data):
    return db_order.getAll(**data)