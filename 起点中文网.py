'''https://read.qidian.com/chapter/IWRw2xSdFSmXfJNNZ-YUzw2/nR_KfXemL2H4p8iEw--PPw2
https://read.qidian.com/chapter/IWRw2xSdFSmXfJNNZ-YUzw2/w3SdIqEHtXNp4rPq4Fd4KQ2
https://read.qidian.com/chapter/IWRw2xSdFSmXfJNNZ-YUzw2/_qg-UJKijdFOBDFlr9quQA2'''

'''https://vipreader.qidian.com/chapter/1020315432/534779200
https://vipreader.qidian.com/chapter/1020315432/535787964
https://vipreader.qidian.com/chapter/1020315432/536178491'''




import requests
import re
from lxml import etree 
import threading
import time

crowl_result_1=[]
crowl_result_2=[]
url_1 ='https://read.qidian.com/chapter/IWRw2xSdFSmXfJNNZ-YUzw2/nR_KfXemL2H4p8iEw--PPw2'
url_2='https://vipreader.qidian.com/chapter/1020315432/534779200'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}


def parse_1(url,header): 
    p = re.compile(r'href="//read.qidian.com/chapter/IWRw2xSdFSmXfJNNZ-YUzw2/.+')
    response=requests.get(url,headers=header)
    html=response.text
    html_herf = p.findall(html)
    htmlElement = etree.HTML(html)#解析成html
    #html_content = etree.tostring(htmlElement,encoding='utf-8').decode("utf-8")#以字符串序列化，返回字符串
    result = htmlElement.xpath('//div[@class="read-content j_readContent"]/p/text()')
    crowl_result_1.append(result)
    i=len(crowl_result_1)
    print(f'正在爬取第{i}章')
    print(crowl_result_1)
    if len(crowl_result_1) == 57:
        return None
    else:
        url1 = 'https:'+html_herf[0][6:79]
        parse_1(url1,header)

      


def parse_2(url,header): 
    p = re.compile(r'href="//vipreader.qidian.com/chapter/1020315432/\d{9}"')
    response=requests.get(url,headers = header)
    html=response.text
    html_herf = p.findall(html)
    htmlElement = etree.HTML(html)#解析成html
    #html_content = etree.tostring(htmlElement,encoding='utf-8').decode("utf-8")#以字符串序列化，返回字符串
    result = htmlElement.xpath('//div[@class="read-content j_readContent"]/p/text()')
    crowl_result_2.append(result)
    i=len(crowl_result_2)
    print(f'正在爬取第{i+57}章')
    print(crowl_result_2)
    if len(crowl_result_2) == 295 -57:
        return None
    else:
        url1 = 'https:'+html_herf[0][6:57]
        time.sleep(1)
        parse_2(url1,header)
        
    
def main():

    t1 = threading.Thread(target=parse_1,args=(url_1,header))
    t2 = threading.Thread(target=parse_2,args=(url_2,header))
    
    t1.start()
    t2.start()
    
    '''parse_1(url_1,header)
    parse_2(url_2,header)'''
    
    while True:
        if t1.is_alive():
            print('t1还活着')
        else:
            print('t1已gg')
        if t2.is_alive():
            print('t2还活着')
        else:
            print('t2已gg')
        time.sleep(2)
     
if __name__ == '__main__':
    main()
    



    
