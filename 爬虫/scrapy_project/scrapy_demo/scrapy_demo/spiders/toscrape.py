import scrapy
import re
from scrapy_demo.items import ScrapyDemoItem
import scrapy.core.scraper

class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        reg_content = re.compile('<span class="text" itemprop="text">(.*?)</span>')
        reg_author = re.compile('<small class="author" itemprop="author">(.*?)</small>')
        text_list = reg_content.findall(response.text)
        author_list = reg_author.findall(response.text)

        for each_index, each_author in enumerate(author_list):
            items = ScrapyDemoItem()
            items["author"] = each_author
            items["content"] = text_list[each_index]
            yield items



