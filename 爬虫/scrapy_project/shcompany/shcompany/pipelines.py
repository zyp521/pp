# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class ShcompanyPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['shcompany']

    def process_item(self, item, spider):
        self.db['company'].update({'stock_code': item['stock_code']}, {'$set': item}, True)
        print(item)
        return item
