# '''
# 将任务单独的保存到redis中。
# '''
# import requests,redis
# from lxml import etree
# base_url = 'https://home.meishichina.com/recipe-type.html'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
#     }
# response = requests.get(base_url,headers=headers)
# tree = etree.HTML(response.text)
# type_urls = tree.xpath('//div[@class="category_sub clear"]/ul/li/a/@href')
# #将url存储redis的list中
# #创建一个redis连接
# redis_ = redis.Redis()
# for type_url in type_urls:
#     # print(type_url)
#     redis_.lpush('caipu:start_urls',type_url)