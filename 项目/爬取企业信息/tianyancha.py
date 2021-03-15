#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosin
:date: 03/28/2019
"""
from tianyancha import crawler
from util import log
import urllib3
urllib3.disable_warnings()


log.set_file("tianyancha.log")


if __name__ == '__main__':
    keys = ['Google']  # todo 查询字段设置
    crawler.load_keys(keys)
    crawler.start()




