# -*- coding:utf-8 -*-
# @Time : 2020/11/18 0018 20:48
# 文件名称 猫眼.py
# 开发人员  周云鹏
# 开发环境 PyCharm
import requests
import queue
import redis
from threading import Thread
from lxml import etree
import hashlib

start_urls = ['https://maoyan.com/films/celebrity/789',
              'https://maoyan.com/films/celebrity/3081',
              'https://maoyan.com/films/celebrity/28608',
              'https://maoyan.com/films/celebrity/28062', ]

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Host': 'maoyan.com',
  'Cookie': '__mta=147559688.1604560278196.1605702943638.1605702978269.9; \
  __mta=147559688.1604560278196.1605702902377.1605702934972.7; uuid_n_v=v1; \
  uuid=16C7CCE01F3611EBAE5C81238522EC8EAD98AC9EE24C4707B5BC119EDD202473; \
  _lxsdk_cuid=175973ed23ec8-0da0b714dd49a-383e570a-100200-175973ed23ec8;\
   _lxsdk=16C7CCE01F3611EBAE5C81238522EC8EAD98AC9EE24C4707B5BC119EDD202473; \
   _csrf=9f5a77418247a69e176c08e708fd08ab1a2b31224e317ef4bf50ae59b99a1877; \
   _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic;\
    Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1604560278,1604560450,1605702891; \
    __mta=147559688.1604560278196.1605702891280.1605702897223.5; \
    Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1605702978; _lxsdk_s=175db59b602-ef4-b62-fd4%7C%7C17',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

class MaoYan(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue
        self.client = redis.Redis()

    def parse(self, url):
        response = requests.get(url, headers=headers)
        tree = etree.HTML(response.text)
        # print(tree)
        actor_urls = tree.xpath('//div[@class="rel-item"]/a/@href')
        actor_name = tree.xpath('/html/body/div[3]/div/div[2]/div[1]/p[1]/text()')[0]
        return actor_name, actor_urls

    def run(self):
        while True:
            if self.queue.empty():
                break
            actor_name, actor_urls = self.parse(self.queue.get())
            print(f'{self.name}获取了{actor_name}')
            self.request_seen(actor_urls)

    def request_seen(self,urls):
        base_url = 'https://maoyan.com'
        for url in urls:
            fp = hashlib.md5(url.encode('utf-8')).hexdigest()
            res = self.client.sadd('actors',fp)
            if res == 1:
                self.queue.put(base_url+url)


if __name__ == '__main__':
    # 初始请求队列
    qu = queue.Queue()
    for i in start_urls:
        qu.put(i)

    # 创建多线程爬虫
    for i in ['aa','bb','cc']:
        t = MaoYan(i,qu)
        t.start()
