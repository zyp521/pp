import scrapy
import json


class DdSpiderSpider(scrapy.Spider):
    name = 'dd_spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5'
                  '&macAddr=html5&channelType=html5&permanentId=20210304093258667358153572071197705&'
                  'returnType=json&channelId=70000&clientVersionNo=5.8.4&platformSource=DDDS-P&fromPlatform=106'
                  '&deviceType=pconline&token=&start=0&end=20&category=XHQH&dimension=sale']

    def parse(self, response):
        with open('/opt/data.txt', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f)
