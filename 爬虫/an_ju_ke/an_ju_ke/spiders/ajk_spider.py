import scrapy


class AjkSpiderSpider(scrapy.Spider):
    name = 'ajk_spider'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://bj.zu.anjuke.com/fangyuan/p1/?pi=baidu-cpchz-bj-ty1&kwid=154693898957&bd_vid=10567841310074322576']

    def parse(self, response):
        print(response.text)
