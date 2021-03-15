# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimalWorldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_ch = scrapy.Field()
    name_en = scrapy.Field()
    animal_type = scrapy.Field()
    Summary = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
