import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from animal_world.my_settings import custom_settings
from animal_world.items import AnimalWorldItem



class AnimalWorldSpiderSpider(scrapy.Spider):
    name = 'animal_world_spider'
    allowed_domains = ['iltaw.com']
    custom_settings = custom_settings
    start_urls = []
    for i in range(1, 2):
        base_url = 'http://www.iltaw.com/animal/all?page={}'.format(i)
        start_urls.append(base_url)


    def parse(self, response):
        # 自动查询div下a标签
        lk = LinkExtractor(restrict_xpaths=('//ul[@class="info-list"]/li/div'))
        link_list = lk.extract_links(response)
        for link in link_list:
            yield scrapy.Request(link.url, callback=self.parse_detail)

    def parse_detail(self, response):
        # print(response.url)
        image_url = response.xpath('//div[@class="cover-wrap"]//div[@class="img"]/img/@data-url').extract_first()
        name_ch = response.xpath('/html/body/div[1]/div/div[2]/div/div[2]/h3/text()').extract_first()
        name_en = response.xpath('/html/body/div[1]/div/div[2]/div/div[2]/h3/span/text()').extract_first()
        animal_type = response.xpath('string(/html/body/div[1]/div/div[2]/div/div[2]/div[2])').extract_first()
        Summary = response.xpath('string(/html/body/div[1]/div/div[4]/div/div[2])').extract_first()
        item = AnimalWorldItem()
        item['name_ch'] = name_ch
        item['name_en'] = name_en
        item['image_urls'] = [image_url]
        item['images'] = f'animal/images/{image_url.split("/")[-1]}'
        item['animal_type'] = animal_type
        item['Summary'] = Summary
        yield item


