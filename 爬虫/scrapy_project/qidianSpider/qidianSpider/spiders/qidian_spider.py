import scrapy
from qidianSpider.items import QidianspiderItem


class QidianSpiderSpider(scrapy.Spider):
    name = 'qidian_spider'
    allowed_domains = ['qidian.com']
    start_urls = ['https://read.qidian.com/chapter/_yUO8WFakkflwGcoSQesFQ2/hlV_ViyV3S_6ItTi_ILQ7A2']

    def parse(self, response):

        # 相应解析出章节，与每章文字
        article_author = response.xpath('//div[@class="text-head"]/h3[@class="j_chapterName"]/span/text()').extract_first()
        article_detail_list = response.xpath('//div[@class="read-content j_readContent "]/p/text()').re('.*')
        article_detail_str = '\n'.join(article_detail_list)
        print(f'正在爬取{article_author}')
        # 获取下一章ur
        next_page_url = response.xpath('//a[@id="j_chapterNext"]/@href').extract_first()
        item = QidianspiderItem()
        item['article_author'] = article_author
        item['article_detail_str'] = article_detail_str
        yield item
        yield scrapy.Request('https:'+next_page_url, callback=self.parse, method='GET')
