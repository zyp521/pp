# -*- coding:utf-8 -*-
# @Time : 2020/11/16 0016 15:17
# 文件名称 mian.py
# 开发人员  周云鹏
# 开发环境 PyCharm
from scrapy import cmdline

cmdline.execute('scrapy crawl shcompany_spider'.split())