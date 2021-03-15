# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from excel_utils.excel_utils import write_to_excel,append_to_excel
import os
from animal_world.items import AnimalWorldItem
from scrapy.pipelines.images import ImagesPipeline

class AnimalWorldPipeline:
    def __init__(self):
        self.filename = './animal/animal.xls'

    def process_item(self, item, spider):
        print(item)
        if isinstance(item, AnimalWorldItem):
            if not os.path.exists(self.filename):
                with open(self.filename, 'w', encoding='utf-8') as f:
                    write_to_excel([dict(item)], self.filename)
            else:
                append_to_excel([dict(item)], self.filename)
            return item


# 更改图片的名称
class DownloadimagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        # # 获取request中的item
        # item = request.meta['item']
        # # 文件格式
        # images_type = 'jpg'  #这里小编图省事，应该是通过地址取出具体的图片格式，这里全都都是jpg的
        # # 修改使用item中的书名为图片名
        # image_name = u'animal/images/{0}.{1}'.format(item['images'],images_type)
        images_name = request.url.split('/')[-1]
        return images_name

    def get_media_requests(self, item, info):
        # # 删除sha1散列值的图片
        # file = item['images'][0]['path']
        # os.remove('.\\images\\{}'.format(file))
        for image_url in item['image_urls']:
            # 为request带上meta参数，把item传递过去
            yield scrapy.Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        item.pop('image_urls')
        return item
