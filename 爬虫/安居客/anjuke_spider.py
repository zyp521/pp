from mitmproxy import http,ctx
import pymongo
from lxml import html

class Ajk_spider:
    def __init__(self):
        # 创建mongodb数据库链接
        self.mongoClient = pymongo.MongoClient(host='127.0.0.1',port=27017)
        # 切换数据库
        self.db = self.mongoClient['anjuke']
        
    
    def request(self,flow: http.HTTPFlow):
        # 拦截请求进行操作
        pass
 
    def response(self,flow: http.HTTPFlow):
        # 抓的得响应进行处理
        if 'pi=baidu-cpchz-bj-ty1&kwid=154693898957&bd_vid=11006793483426581265'in flow.request.url:
            tree = html.etree.HTML(flow.response.text)
            content_list_tree = tree.xpath('//div[@id="list-content"]/div[@class="zu-itemmod"]')
            dict_list =[]
            for each_div_tree in content_list_tree:
                dict_content = {}
                dict_content['title'] = each_div_tree.xpath('./div[@class="zu-info"]/h3//text()')
                dict_content['size'] = each_div_tree.xpath('./div[@class="zu-info"]/p[1]//text()')
                dict_content['address'] = each_div_tree.xpath('./div[@class="zu-info"]/address/text()')
                dict_content['detail'] = each_div_tree.xpath('./div[@class="zu-info"]/p[2]/span/text()')
                dict_content['price'] = each_div_tree.xpath('./div[@class="zu-side"]//b/text()')  
                dict_list.append(dict_content)
            self.save(dict_list)
                      

    def save(self,data):
        '''params:data-->[{},{}....]'''
        x = self.db['ajk_collection'].insert_many(data)
        print('已插入'+str(len(x.inserted_ids))+'条记录')
         
    
addons = [
    Ajk_spider()
    ]


