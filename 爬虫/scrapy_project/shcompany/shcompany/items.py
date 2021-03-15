# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShcompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_code = scrapy.Field()
    stock_name = scrapy.Field()
    company_name = scrapy.Field()
    sh_date = scrapy.Field()
    corporate_finance = scrapy.Field()
    industry_type = scrapy.Field()
    major_businesses = scrapy.Field()
