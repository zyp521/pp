import scrapy


class LagouSpiderSpider(scrapy.Spider):
    name = 'lagou_spider'
    allowed_domains = ['www']
    start_urls = ['http://www/']

    def parse(self, response):
        pass
