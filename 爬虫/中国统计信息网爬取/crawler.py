import requests
import re, lxml.html
import time, random
from excel_utils.excel_write import write_to_excel, append_to_excel
import os

res = []

# 国内所有省份url获取
start_url = 'http://www.tjcn.org/tjgb/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/89.0.4389.90 Safari/537.36'}
provinces_urls_response = requests.get(start_url, headers=header)
provinces_urls_response.encoding = 'gb2312'
# 获取所有省份网页地址
# etree = lxml.html.etree.HTML('provinces_urls_response.text')
# provinces_urls = etree.xpath('/html/body/table[6]/tbody/tr/td[1]/table[2]/tbody/tr/td/a/@href')
provinces_urls = re.findall('<a href="/tjgb/(.*?)">(\w{2,3})</a>', provinces_urls_response.text)[1:1 + 31]

# 根据上述获取的provinces_urls获取各省市年度公报链接url
base_url = start_url
print(provinces_urls)
for i in provinces_urls[18:19]:
    time.sleep(random.randint(5, 10))
    provinces_url = base_url + i[0]
    # 不同省份城市数目不同，各年度公报数不同，这里取各省公报前40条（广东省含21省地级市，为全国最高）
    buttetin_urls = []  # 各省份前40份年度公报
    for page in ('', 'index_2.html'):
        bulletin_urls_response = requests.get(provinces_url + page, headers=header)
        bulletin_urls_response.encoding = 'gb2312'
        buttetin_urls += re.findall(
            '<li><a href="/tjgb/(.*?)" title="(.*?)">(?:.*?)国民经济和社会发展统计公报</a> <span>(.*?)</span></li>',
            bulletin_urls_response.text)
    print(buttetin_urls)
    print(len(buttetin_urls))

    # 根据上诉获取的各公报URL地址，获取各公报内容
    for j in buttetin_urls:
        time.sleep(random.randint(5, 10))
        buttetin_url = start_url + j[0]
        buttetin_year = re.findall('\d{4}', j[1])[0]
        buttetin_province = i[1]
        buttetin_city = re.split('\d{4}', j[1])[0]
        buttetin_name = j[1]
        buttetin_release_date = j[2]
        buttetin_content_resposne = requests.get(buttetin_url, headers=header)
        buttetin_content_resposne.encoding = 'gb2312'
        etree = lxml.html.etree.HTML(buttetin_content_resposne.text)
        buttetin_content = ''.join(etree.xpath('//td[@id="text"]//text()'))
        buttetin_page = int(etree.xpath('//td[@id="text"]/div[last()]/p/a[@title="Page"]/b[last()]/text()')[0])

        # 如果报告多页，进行分页爬取
        if buttetin_page >= 2:
            for pg in range(2, buttetin_page + 1):
                next_page_url = buttetin_url[:-5] + f'_{pg}' + buttetin_url[-5:]
                next_page_content_response = requests.get(next_page_url, headers=header)
                next_page_content_response.encoding = 'gb2312'
                buttetin_content += ''.join(
                    lxml.html.etree.HTML(next_page_content_response.text).xpath('//td[@id="text"]//text()'))
                print(f'正在爬取{buttetin_name}第{pg}页')

        print(f'page:{buttetin_page}')
        print(f'年度:{buttetin_year}')
        print(f'省份：{buttetin_province}')
        print(f'城市：{buttetin_city}')
        print(f'报告名字：{buttetin_name}')
        print(f'报告内容：{buttetin_content}')
        print(f'报告链接：{buttetin_url}')
        print(f'发布日期：{buttetin_release_date}')
        print('-------------------------------------------------------------------')
        res.append({'年度': buttetin_year, '省份': buttetin_province, '城市': buttetin_city, '报告名字': buttetin_name,
                    '报告链接': buttetin_url, '发布日期': buttetin_release_date, '报告内容': buttetin_content})

# 写入excel表格
fileName = '公报爬取测试数据.xls'
if not os.path.exists(fileName):
    write_to_excel(res, fileName)
else:
    append_to_excel(res, fileName)
