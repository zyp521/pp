import scrapy

from ..items import CaipuSpiderItem
from ..my_settings import custom_settings
from scrapy.linkextractors import LinkExtractor
import socket
from scrapy_redis.spiders import RedisSpider
class MenuSpiderSpider(RedisSpider):
    name = 'menu_spider'
    # allowed_domains = ['www']
    custom_settings = custom_settings
    #当前电脑从redis中的redis-key所对应的初始任务列表中取任务。
    redis_key = 'caipu:start_urls'
    myaddr = socket.gethostbyname(socket.gethostname())
    # start_urls = ['https://home.meishichina.com/recipe-type.html']
    #
    # def parse(self, response):
    #     le = LinkExtractor(restrict_xpaths=['//div[@class="category_sub clear"]/ul'])
    #     links = le.extract_links(response)
    #     # print(links)
    #     for link in links:
    #         cook_type = link.text
    #         type_url = link.url
    #         #meta的功能三：parse方法之间传递参数
    #         yield scrapy.Request(type_url,
    #                              callback=self.parse_type,
    #                              encoding='utf-8',meta={'cook_type':cook_type})

    def parse(self,response):
        print(response.url)
        cook_type = response.xpath('//h1[@class="on"]/a/text()').extract_first()
        li_list = response.xpath('//div[@id="J_list"]/ul/li')
        for li in li_list:
            cook_name = li.xpath('.//div[@class="detail"]/h2/a/text()').extract_first()
            # print(cook_name)
            cook_url = li.xpath('.//div[@class="detail"]/h2/a/@href').extract_first()
            #发布人
            cook_publish_up = li.xpath('.//div[@class="detail"]/p[1]/a/text()').extract_first()
            cook_material = li.xpath('.//div[@class="detail"]/p[2]/text()').extract_first()

            item = CaipuSpiderItem()
            item['cook_name']= cook_name
            item['cook_type']= cook_type
            item['cook_url']= cook_url
            item['cook_publish_up']= cook_publish_up
            item['cook_material']= cook_material
            item['ip'] = self.myaddr
            # print(item)
            yield item
        #获取下一页的连接
        next_page = response.xpath('//div[@class="ui-page-inner"]/a[last()]/text()').extract_first()
        if next_page=='下一页':
            next_url = response.xpath('//div[@class="ui-page-inner"]/a[last()]/@href').extract_first()
            yield scrapy.Request(next_url,callback=self.parse,encoding='utf-8')