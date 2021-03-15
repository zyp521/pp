# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ScrapyDemoPipeline:
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                                          password='123123', database="demo", charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # 定义sql语句
        author = item['author']
        content = item['content']
        sql = f"insert into scr(author,content)values ('{author}', '{content}')"
        print(sql)
        # 执行sql语句
        self.cursor.execute(sql)
        # 保存修改
        self.connection.commit()
        return item

    def __del__(self):
        self.cursor.close()
        self.connection.close()
