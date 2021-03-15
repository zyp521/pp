import scrapy
from hupu_news.items import HupuNewsItem


class HupuSpiderSpider(scrapy.Spider):
    name = 'hupu_spider'
    allowed_domains = ['hupu.com']
    start_urls = []
    for i in range(1, 2):
        base_url = 'https://voice.hupu.com/news?category=all&page=%s'
        ful_url = base_url.format(i)
        start_urls.append(ful_url)

    def parse(self, response):
        detail_url_list = response.xpath('/html/body/div[3]/div[1]/div[2]/ul/li/div[1]/h4/a/@href').extract()
        for url in detail_url_list:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        # 显示请求的url
        # print(response.url)
        news_title = response.xpath('/html/body/div[4]/div[1]/div[1]/h1/text()').extract_first()
        news_source = response.xpath('//*[@id="source_baidu"]/a/text()').extract_first()
        news_date = response.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
        news_content = response.xpath('/html/body/div[4]/div[1]/div[2]/div/div[2]/p//text()').extract()
        news_item = HupuNewsItem()
        news_item['news_title'] = news_title.strip()
        news_item['news_source'] = news_source.strip()
        news_item['news_date'] = news_date.strip()
        news_item['news_content'] = ''.join(news_content)
        news_item['news_url'] = response.url
        # print(news_item)
        yield news_item
