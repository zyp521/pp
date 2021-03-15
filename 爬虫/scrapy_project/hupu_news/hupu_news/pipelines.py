# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class HupuNewsPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['hupu_news']

    def process_item(self, item, spider):
        self.db['news'].update({'news_url': item['news_url']}, {'$set': item}, True)
        print(item)
        return item
