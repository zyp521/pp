import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'
    # allowed_domains = ['www']
    start_urls = ['http://81.70.100.13:8000/buyer/index']

    def parse(self, response):
        print(response.text)

    def start_requests(self):
        log_in = 'http://81.70.100.13:8000/buyer/login/'
        from_data = {
            'user_name': '888888',
            'user_pwd': '123456'
        }
        yield scrapy.FormRequest(formdata=from_data,url=log_in,callback=self.parse_login)

    def parse_login(self,response):
        if '888888' in response.text:
            print('登录成功')

        yield from super().start_requests()
