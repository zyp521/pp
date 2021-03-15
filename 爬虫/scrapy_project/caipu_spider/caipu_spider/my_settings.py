#自定义配置字典
import random

custom_settings = {
    #请求头
    'DEFAULT_REQUEST_HEADERS' : {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    },
    'ROBOTSTXT_OBEY' : False,
    #下载中间件配置
    # 'DOWNLOADER_MIDDLEWARES' : {
    #     #设置代理的中间件
    #    'z_animal_world.my_settings.Proxy_Middle': 543,
    # },
    #存储管道
    'ITEM_PIPELINES' : {
       'caipu_spider.my_settings.MongoPipeline': 300,
    },



    #日志配置
    # 'LOG_ENABLED':'True',#开启日志记录
    # 'LOG_ENCODING':'utf-8',#日志的编码
    # 'LOG_FILE':'hupu.log',#日志文件的保存文件名
    # 'LOG_LEVEL':'DEBUG',#日志级别

    # #mongo配置
    # 'MONGO_URI':'localhost',
    # #数据名字
    'MONGO_DATABASE':'caipu',

    #=======================
    #scrapy-redis配置
    #配置scrapy-redis调度器
    'SCHEDULER' : "scrapy_redis.scheduler.Scheduler",
    #配置url去重
    'DUPEFILTER_CLASS' : "scrapy_redis.dupefilter.RFPDupeFilter",
    #配置优先级队列
    'SCHEDULER_QUEUE_CLASS' : 'scrapy_redis.queue.PriorityQueue',
    'REDIS_PORT' : 6379,

    # #主机
    # 'REDIS_HOST' : 'localhost',
    # 'MONGO_URI' : 'localhost',

    #从机
    'REDIS_HOST': '10.10.123.17',
    'MONGO_URI': '10.10.123.17',


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
        '''

        :param request:
        :param spider:
        :return:
        '''
        # 设置代理
        ip  = random.choice(self.proxy_list)
        print(ip)
        request.meta['proxy'] = 'http://'+ip

        #设置请求头
        user_agent = random.choice(self.USER_AGENGT)
        print(user_agent)
        request.headers.setdefault('user-agent',user_agent)

import pymongo
from itemadapter import ItemAdapter

class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        #集合的名字
        self.collection_name = 'caipu'

    #scrapy项目启动之后的入口方法
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        '''
        spider代码执行的之后调用这个方法
        :param spider:
        :return:
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # self.collection_name=item['cook_type']
        self.db[self.collection_name].update({'cook_url':item['cook_url']},{'$set':dict(item)},True)
        print(item)
        return item
