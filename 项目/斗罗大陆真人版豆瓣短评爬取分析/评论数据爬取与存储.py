import requests
import time,random
import re
import MyDB_
import settings
import pickle

db = MyDB_.MyDB(h=settings.HOST, u=settings.USER, p=settings.PASSWORD, db=settings.DATABASE)

# 起始页url
start_url = 'https://movie.douban.com/subject/30313969/comments?start={}&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

# 分页获取数据
for i in range(25):
    response = requests.get(start_url.format(i * 20), headers=headers)
    ## 由于js渲染问题，使用xpath找不到节点，改用正则表达式
    # print(response.text)
    # tree = html.etree.HTML('response.text')
    # print(tree)
    # comment_trees = tree.xpath('//div')
    # print(comment_trees)
    # for each_tree in comment_trees:
    #     comment_type = each_tree.xpath('./div[2]/h3/span[2]/span[2]/@title')
    #     comment_content = each_tree.xpath('./div[2]/p/span/text()')
    #     print(comment_type, comment_content)

    # 使用正则匹配内容
    comment_type = re.findall('<span class="allstar[1-5]0 rating" title="(.*?)"></span>', response.text)
    comment_content = re.findall('<span class="short">(.*?)</span>', response.text)
    # 进行持久化存储
    for each_comment_content, each_commnet_type in zip(comment_content, comment_type):
        try:
            sql = 'insert into douluo_comment(comment,comment_type) values(%s,%s)'
            data = (each_comment_content, each_commnet_type)
            db.update(sql, data)
        except:
              print(data)
    print(f'完成第{i}页')
    time.sleep(random.randint(5,10))
