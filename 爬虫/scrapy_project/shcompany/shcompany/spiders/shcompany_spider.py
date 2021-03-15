import scrapy
from shcompany.items import ShcompanyItem

class ShcompanySpiderSpider(scrapy.Spider):
    name = 'shcompany_spider'
    allowed_domains = ['askci.com']
    start_urls = ['https://s.askci.com/stock/0-0-0/1/']

    def parse(self, response):
        print(response.__class__)
        # company_list = response.xpath('//*[@id="ResultUl"]/tr')
        # # print(company_list)
        # for i in company_list:
        #     item = ShcompanyItem()
        #     item['stock_code'] = i.xpath('string(./td[2]/a)').extract_first()
        #     item['stock_name'] = i.xpath('string(./td[3]/a)').extract_first()
        #     item['company_name'] = i.xpath('string(./td[4])').extract_first()
        #     item['sh_date'] = i.xpath('string(./td[5])').extract_first()
        #     item['corporate_finance'] = i.xpath('string(./td[7]/a/@href)').extract_first()
        #     item['industry_type'] = i.xpath('string(./td[8])').extract_first()
        #     item['major_businesses'] = i.xpath('string(./td[9])').extract_first()
        #     # print(item)
        #     yield item