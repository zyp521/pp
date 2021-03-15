# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    cook_name = scrapy.Field()
    cook_type = scrapy.Field()
    cook_url = scrapy.Field()
    cook_publish_up = scrapy.Field()
    cook_material = scrapy.Field()
    ip = scrapy.Field()
