# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from qidianSpider.items import QidianspiderItem
import json


class QidianspiderPipeline:

    def save_file(self, item):
        # self.file = open('novel.json', 'wb')
        # line = json.dumps(dict(item))+'\n'
        # self.file.write(line.encode('utf-8'))
        with open('我家地址都有隐藏身份.txt', 'a') as f:
            f.write('\n\n------------------------------------------------\n')
            f.write(item['article_author'])
            f.write('\n')
            f.write(item['article_detail_str'])

    def process_item(self, item, spider):
        if isinstance(item,QidianspiderItem):
            self.save_file(item)
        return item
