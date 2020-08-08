#所有英雄ID'''https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'''
'''https://lol.qq.com/data/info-defail.shtml?id=61
https://lol.qq.com/data/info-defail.shtml?id=236
https://lol.qq.com/data/info-defail.shtml?id=104'''

import requests
import multiprocessing 
#//ul[@id="skinBG"]/li/img/@* 

header={'Referer': 'https://lol.qq.com/data/info-heros.shtml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
url_a ='https://game.gtimg.cn/images/lol/act/img/skin/big'

hero_address_meta = {}
hero_all = []

response = requests.get(url,headers=header)
html = response.json()
hero_list = html['hero']

#获取所有英雄的名字与其对应的网页链接
for each in hero_list:
    hero_Id = each["heroId"]
    hero_name = each["name"]
    hero_all.append(hero_name)
    hero_address_meta.setdefault(hero_name,url_a+hero_Id)
    
#print(hero_all)    
#print(hero_address_meta)

#上面获得针对每个英雄ID 拼接所有皮肤图片链接
for i in hero_all:
    list1=[]
    for j in range(31):
        str1 = str(j).rjust(3,"0")
        str2 = hero_address_meta[i]+str1+".jpg"
        list1.append(str2)
    hero_address_meta.update({i:list1})

#print(hero_address_meta)
def get_image(file_name,p,url):
    try:
        response = requests.get(url)
        result = response.text
        if result!='404 page not found\n':
            with open(r'./image/LOL/'+file_name+'_'+str(p)+'.jpg','wb') as f:
                f.write(response.content)
    except requests.exceptions.ConnectionError:
        pass

def process(hero_list):
    for i in hero_list:
        for j in hero_address_meta[i]:
            p = hero_address_meta[i].index(j)
            print(f'正在爬取{i}第{p}')
            get_image(i,p,j)

#双进程处理下载
def main():
    hero_all_mid = int(len(hero_all)/2)
    t1 = multiprocessing.Process(target=process,args=(hero_all[:hero_all_mid],))
    t2 = multiprocessing.Process(target=process,args=(hero_all[hero_all_mid:],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("所有图片爬取完毕")
    
if __name__ =="__main__":
    main()

        
 
        
        
    



        



