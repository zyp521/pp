import scrapy
from scrapy.linkextractors import LinkExtractor
from matplotlib_download.items import MatplotlibDownloadItem


class MatplotlibSpiderSpider(scrapy.Spider):
    name = 'matplotlib_spider'
    # allowed_domains = ['www']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        url_list = response.xpath('//*[@id="matplotlib-examples"]/div/ul/li[26]/ul/li/a/@href').extract()
        # print(url_list)
        for i in url_list:
            ful_url = response.urljoin(i)
            yield scrapy.Request(ful_url, callback=self.parse_files)

    def parse_files(self, response):
        # 自动提取a标签中的链接
        lk = LinkExtractor(restrict_xpaths=('//div[@class="body"]/div/p[1]',))
        file_url = lk.extract_links(response)[0]
        # print(file_url)
        item = MatplotlibDownloadItem()
        item['file_urls'] = [file_url.url]
        yield item
