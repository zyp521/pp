# -*- coding:utf-8 -*-
# @Time : 2020/11/27 0027 21:53
# 文件名称 mian.py
# 开发人员  周云鹏
# 开发环境 PyCharm
from scrapy import cmdline

cmdline.execute('scrapy crawl luj_spider'.split())