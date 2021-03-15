import scrapy
from scrapy.linkextractors import LinkExtractor
from ludingji.my_setting import custom_settings


class LujSpiderSpider(scrapy.Spider):
    name = 'luj_spider'
    # allowed_domains = ['www']
    custom_settings = custom_settings
    start_urls = ['https://www.kanunu8.com/wuxia/201102/1624.html']

    def parse(self, response):
        # lk = LinkExtractor(restrict_xpaths='//div[@class=""]/')
        # urls = lk.extract_links(response)
        base_url = 'https://www.kanunu8.com/wuxia/201102/'
        urls = response.selector.re('<a href="(1624/(?:\d{5}).html)">(.*?)</a></td>')
        urls = urls[:-4]
        for url in urls[::2]:
            title = urls[urls.index(url)+1]
            url = base_url + url
            # print(title, url)
            yield scrapy.Request(url=url, callback=self.parse_url, meta={'title': title})

    def parse_url(self, response):
        content_text = response.xpath('string(//div[@align="center"]/table[5]//p)').extract()
        title = response.meta.get('title', '未知章节').replace(' ', '_')
        with open(f'./鹿鼎记全文/{title}.txt', 'wt', encoding='utf-8') as f:
            print(f'写入{title}')
            f.writelines(content_text)
