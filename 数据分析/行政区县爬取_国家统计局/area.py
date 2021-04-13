# @Time : 2021/4/116:54
# @Author : 周云鹏
# @File : area.PY

import requests
import lxml.html
import pandas as pd

# data 获取所有的省市县
data = []
base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/89.0.4389.90 Safari/537.36'}

province_urls_responses = requests.get(base_url + 'index.html', headers=headers)
province_urls_responses.encoding = 'gb2312'
province_urls_etree = lxml.html.etree.HTML(province_urls_responses.text)
province_urls = province_urls_etree.xpath('//tr[@class="provincetr"]/td/a/@href')
provinces = province_urls_etree.xpath('//tr[@class="provincetr"]/td/a/text()')
data += provinces  # 添加省数据
# 爬取省下地级市
for i in province_urls:
    city_url = base_url + i
    city_responses = requests.get(city_url, headers=headers)
    city_responses.encoding = 'gb2312'
    county_urls_etree = lxml.html.etree.HTML(city_responses.text)
    # print(city_responses.text)
    county_urls = county_urls_etree.xpath("//tr[@class='citytr']/td[2]/a/@href")
    cities = county_urls_etree.xpath("//tr[@class='citytr']/td[2]/a/text()")
    # print(cities)
    data += cities  # 添加市数据
    # 爬出地级市下县区
    for j in county_urls:
        county_url = base_url + j
        county_responses = requests.get(county_url, headers=headers)
        county_responses.encoding = 'gb2312'
        r_urls_etree = lxml.html.etree.HTML(county_responses.text)
        # county_urls = r_urls_etree.xpath("//tr[@class='citytr']/td[2]/a/@href")
        county = r_urls_etree.xpath("//tr[@class='countytr']/td[2]/a/text()")
        print(f'正在爬取{county}')
        data += county

pd.DataFrame(columns=['area'], data=data).to_csv('area.csv')
