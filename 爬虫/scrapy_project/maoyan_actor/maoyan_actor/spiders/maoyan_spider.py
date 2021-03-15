import scrapy


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    # allowed_domains = ['www']
    start_urls = ['https://maoyan.com/films/celebrity/789',
                  'https://maoyan.com/films/celebrity/3081',
                  'https://maoyan.com/films/celebrity/28608',
                  'https://maoyan.com/films/celebrity/28062',]


    def parse(self, response):
        pass
