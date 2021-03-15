from mitmproxy import http,ctx
import json
import time


class Taobao_spider:
    def __init__(self):
        pass
    
    def request(self,flow: http.HTTPFlow):
        # 拦截请求进行操作
        pass
 
    def response(self,flow: http.HTTPFlow):
       # 抓的得响应进行处理
       if 'h5api.m.taobao.com/h5/mtop'in flow.request.url:
           base_filename = './taobao_data/taobao'+str(time.time()).replace('.','')
           with open(base_filename+'.txt','w',encoding='utf-8')as f:
               f.write(flow.response.text)
         
    
addons = [
    Taobao_spider()
    ]
