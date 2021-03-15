# -*- coding:utf-8 -*-
# @Time : 2020/11/17 0017 15:04
# 文件名称 my_settings.py
# 开发人员  周云鹏
# 开发环境 PyCharm
import random

custom_settings = {
    # 请求头
    'DEFAULT_REQUEST_HEADERS': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    },
    'ROBOTSTXT_OBEY': False,
    # 设置下载中间件配置
    'DOWNLOADER_MIDDLEWARES': {
        # 设置代理的中间件
        'animal_world.my_settings.Proxy_Middle': 543,
    },
    # 储存管道
    'ITEM_PIPELINES': {
        'animal_world.pipelines.AnimalWorldPipeline': 301,  # 保存信息
        'animal_world.pipelines.DownloadimagesPipeline': 300, # 图片保存管道
    },
    # 图片下载配置
    'IMAGES_STORE': 'animal/images',
    'IMAGES_THUMBS': {'big': (300, 300), 'small': (100, 100)}


    # 日志配置
    # 'LOG_ENABLED':'True',#开启日志记录
    # 'LOG_ENCODING':'utf-8',#日志的编码
    # 'LOG_FILE':'hupu.log',#日志文件的保存文件名
    # 'LOG_LEVEL':'DEBUG',#日志级别

}


class Proxy_Middle(object):

    def __init__(self):
        self.proxy_list = [
            '117.69.144.151:4226',
            '183.166.118.199:4231',
            '117.89.95.190:4232',
        ]
        self.USER_AGENGT = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

    def process_request(self, request, spider):
            # Called for each request that goes through the downloader
            # middleware.

            # Must either:
            # - return None: continue processing this request 添加代理继续下载器下载
            # - or return a Response object   自定义下载后，返回
            # - or return a Request object
            # - or raise IgnoreRequest: process_exception() methods of
            #   installed downloader middleware will be called

            # 设置代理
            # ip = random.choice(self.proxy_list)
            # request.meta['proxy'] = 'http://' + ip

            # 设置请求头
            user_agent = random.choice(self.USER_AGENGT)
            request.headers.setdefault('user-agent', user_agent)

            # def __init__(self, url, callback=None, method='GET', headers=None, body=None,
            #              cookies=None, meta=None, encoding='utf-8', priority=0,
            #              dont_filter=False, errback=None, flags=None, cb_kwargs=None):
            return None
