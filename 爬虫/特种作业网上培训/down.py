#encoding=utf-8
import requests
import time
from lxml import etree
from urllib.parse import urljoin
import re
import os
import random
import json
from urllib.parse import splithost

host = "jmaspx.tskspx.com"
#host="www.aqscpx.com"
index_url = 'http://%s/indexNew.do' %host


class tskspxSpider:
    def __init__(self,user,password,sleepTime=1,debug=False,debugPage=1):
        self.sess = requests.Session()
        self.user =user
        self.password=password
        self.debug = debug
        self.debugPage=debugPage
        self.sleepTime=sleepTime
        print("+============INFO=================+\n"
              +"+  user:%s\n"%self.user
              +"+  pass:%s\n"%self.password
              +"+  sleep:%d s\n"%int(self.sleepTime)
              +"+  debug:%s\n"% str(self.debug)
             +"+=================================+")

    def close(self):
        self.sess.close()

    def login(self):
        try:
            os.mkdir(self.user)
        except:
            pass
        try:
            os.mkdir(self.user+'/img')
        except:
            pass
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            #http://www.tskspx.com/indexNew.do
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        self.sess.get(index_url,headers=headers)
        time.sleep(2)
        url = 'http://%s/userLogin.do?userid=%s&password=%s' % (host,self.user, self.password)
        headers = {
            #http://www.tskspx.com/indexNew.do
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": host,
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            "Referer": index_url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        req = self.sess.post(url, headers=headers)
        print(req.text)
        time.sleep(2)
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            #"Host":host,
            "Referer":"http://%s/indexNew.do" % host,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        req= self.sess.get('http://%s/toSelectProject.do' % host,headers=headers)
        #req = self.sess.get('http://www.tskspx.com/user/userCenter.do')
        print(req.status_code)



        print(req.url)
        if req.url != 'http://%s/user/userCenter.do' % host:
            print("cur_url:",req.url)
            print("Login Failed,exit")
            exit(0)
        html = etree.HTML(req.text)
        project = html.xpath('//div[@class="ptop"]/ul[@class="e"]/li[1]/text()')[0]
        self.project = project[project.find('培训项目：')+len('培训项目：'):]

    def getMenuPage(self):
        print("getMenuPage")
        url = 'http://%s/user/knowledge.do?menuid=3' % host
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            #http://www.tskspx.com/indexNew.do
            "Referer": "http://%s/user/userCenter.do" % host,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        req = self.sess.get(url,headers=headers)
        html = etree.HTML(req.text)
        # if not html.xpath('//a[@class="zsdlx"]/@href'):
        #     print("未检测到任何项目，可能是学习卡过期了，请手动关闭窗口")
        #     while True:
        #         time.sleep(1)
        #         print("未检测到任何项目，可能是学习卡过期了，请手动关闭窗口")
        urls = {}

        for tr in html.xpath('//table[@class="ptbside"]/tr[2]/td[1]/table/tr'):
            #print(tr)
            try:
                a = tr.xpath('td[3]/a[@class="nod1"]')[0]
                href = a.xpath("@href")[0]
                #print(href)
                m = re.match("javascript:getKnowledgeQuestion\\((\\d+), ?'([0-9a-zA-Z]+)'\\)", href)
                if m:
                    apid = m.group(1)
                    zsdDg = m.group(2)
                    text = a.xpath("text()")[0]
                    url = "http://%s" % host + '/user/' + apid + '/getCurrentQuestion.do?currNum=' + '&zsdDg=' + zsdDg
                    if text not in urls:
                        urls[text] = {
                            "url": url,
                            "zsdDg": zsdDg
                        }
            except Exception as e:
                #print(e)
                pass

        # for a in html.xpath('//a[@class="nod1"]'):
        #     try:
        #         href = a.xpath("@href")[0]
        #         print(href)
        #         m =  re.match("javascript:getKnowledgeQuestion\\((\\d+), ?'([0-9a-zA-Z]+)'\\)",href)
        #         if m:
        #             apid = m.group(1)
        #             zsdDg =  m.group(2)
        #             text = a.xpath("text()")[0]
        #             url = "http://%s" %host + '/user/' + apid + '/getCurrentQuestion.do?currNum=' + '&zsdDg=' + zsdDg
        #             if text not in urls:
        #                 urls[text]={
        #                     "url":url,
        #                     "zsdDg":zsdDg
        #                 }
        #             #return url,zsdDg
        #     except Exception as e:
        #         print(e)
        #print(urls)
        if len(urls.keys()) == 0:
            while True:
                time.sleep(1)
                print("未检测到任何项目，可能是学习卡过期了，请手动关闭窗口")
        elif len(urls.keys()) == 1:
            keys = list(urls.keys())
            print("项目：", self.project+"-" +keys[0] )
            with open('%s/info.json' % self.user, 'w') as f:
                info = {
                    "user": self.user,
                    "password": self.password,
                    "project": self.project+"-" +keys[0]
                }
                f.write(json.dumps(info))

            return urls[keys[0]]['url'],urls[keys[0]]['zsdDg']

        while True:
            print("检测到可能存在多个结果，请黏贴文本选择")
            keys = list(urls.keys())
            for i in range(len(keys)):
                print("%d:\t%s" % (i,keys[i]))
            text = input("黏贴文本>")
            text = text.strip()
            if text not in urls:
                print("结果不存在")
            else:
                print("项目：", self.project + "-" + keys[0])
                with open('%s/info.json' % self.user, 'w') as f:
                    info = {
                        "user": self.user,
                        "password": self.password,
                        "project": self.project + "-" + text
                    }
                    f.write(json.dumps(info))


                return urls[text]['url'],urls[text]['zsdDg']

        # for a in html.xpath('//table[@class="ptbside"]//a[@class="nod1"]'):
        #     try:
        #         href = a.xpath("@href")[0]
        #         #print(href)
        #         m =  re.match("javascript:getKnowledgeQuestion\\((\\d+), ?'(\\d+)'\\)",href)
        #         if m:
        #             apid = m.group(1)
        #             zsdDg =  m.group(2)
        #             url = "http://%s" %host + '/user/' + apid + '/getCurrentQuestion.do?currNum=' + '&zsdDg=' + zsdDg
        #             #return url,zsdDg
        #     except Exception as e:
        #         print(e)




        # print(html.xpath('//a[@class="zsdlx"]/text()')[0], html.xpath('//a[@class="zsdlx"]/@href')[0])
        # url = urljoin(url,html.xpath('//a[@class="zsdlx"]/@href')[0])
        # return url
    def getIntoQuestionPage(self,url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            #http://www.tskspx.com/indexNew.do
            "Referer": "http://%s/user/knowledge.do?menuid=3" % host,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        req = self.sess.get(url, headers=headers)
        #html = etree.HTML(req.text)
        print(req.url)
        html = etree.HTML(req.text)
        table = html.xpath('//table[@class="plxanswer1"]')[0]
        first_one=None
        for a in table.xpath('tr[1]//a'):
            first_one = a
            if a.xpath('text()')[0] == u'第一题':
                print("Find First One!")
                break
            else:
                print(a.xpath('text()')[0])
        href = first_one.xpath('@href')[0]
        print(href)
        m=re.match('''javascript:jumpPageNumNew\\((.*?),(.*?),'(.*?)'\\);''',href)
        if not m:
            print("Error dont match,exit")
            exit(0)
        print(m.group(2),m.group(3))
        all = int(m.group(2))
        stlx=m.group(3)
        stbh =html.xpath('//input[@name="stbh"]/@value')[0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            #http://www.tskspx.com/indexNew.do
            "Referer": "%s" % url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        url = urljoin(req.url,'getNextQuestion.do?currentPage=1&stlx=&answer=&stbh='+stbh)
        #print(url)
        req = self.sess.get(url,headers=headers)
        #print(req.url)
        return req.url,all,stlx,stbh
    def downloadImg(self,base_url,img_src):
        headers={
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            #http://www.tskspx.com/indexNew.do
            "Pragma": "no-cache",
            "Referer": base_url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        try:
            req = self.sess.get(img_src, headers=headers)
            filename = "%s/img/%d_" % (self.user, random.randint(1,100000)) + os.path.basename(img_src)
            with open(filename, 'wb') as f:
                f.write(req.content)
            return filename
        except Exception as e:
            print(e)
        return ""

    def getAllQuestionPage(self,base_url,all,stbh,zsdDg):
        startPage = 1
        if self.debug == True:
            startPage = self.debugPage
        for i in range(startPage,all+1):
            if os.path.exists("%s/%d.json" % (self.user,i)):
                continue
            url = urljoin(base_url,('getNextQuestion.do?currentPage=%d&stlx=&answer=&stbh=%s&zsdDg=%s' % (i,stbh,zsdDg)))
            #print(url)
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                #http://www.tskspx.com/indexNew.do
                "Referer": "%s" % url,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
            }
            #print("req:",url)
            req = self.sess.get(url, headers=headers)
            #html = etree.HTML(req.text)
            html = etree.HTML(req.content.decode("utf-8"))


            try:
                 td = html.xpath('//td[@class="headtop"]')[0]
            except Exception as e:
                print(e)
                #raise e
                time.sleep(2)
                continue
            question={}

            question['type'] = td.xpath('span[1]/text()')[0]
            #print(td.xpath('span[2]/@class')[0].strip())
            title =td.xpath('span[2]/text()')
            if title:
                 question['title'] =CF.crack(td.xpath('span[2]/@class')[0].strip(),title[0].strip())
            else:
                question['title']=""
            question['pics'] = None
            if td.xpath('span[2]/img')!= []:
                #print("page:",i)
                #print()
                #print(question['title'])
                if td.xpath('span[2]/img')[0].xpath('@src') != []:
                    question['pics']=self.downloadImg(req.url,urljoin(req.url,td.xpath('span[2]/img')[0].xpath('@src')[0]))
            question['options'] ={}
            for label in html.xpath('//table[@class="ks_st"]//label'):
                op = label.xpath('@for')[0]
                question['options'][op] = label.xpath('text()')[1].strip()
#yang1 
            if html.xpath('//table[@class="plxanswer2"]//span/text()')!= []:
                answer = html.xpath('//table[@class="plxanswer2"]//span/text()')[0]
            else:
                    answer = ""


            font_num = html.xpath('//table[@class="plxanswer2"]//span/@class')[0]

            question['answer'] = CF.crack(font_num,answer)


            with open("%s/%d.json" % (self.user,i),'w') as f:
                f.write(json.dumps(question))
            print(question)
            time.sleep(self.sleepTime + random.random())


def main():
    user=str(input("输入身份证号："))
    password = "123456"
    password=str(input("输入密码："))
    #user = "420802199710290854"
    #user = "429006198301285144"
    #user = "42243119640727215X"
    #user = "420802199307300039"
    #password = user[-8:]

    #print(repr(password))
    if not  password :
        password = user[-8:]
    timesleep=2
    try:
        timesleep=int(input("输入等待时间(默认为2)："))
    except:
        timesleep=2
    spider = tskspxSpider(user, password, timesleep)
    spider.login()
    url,zsdDg = spider.getMenuPage()
    url, all, stlx, stbh = spider.getIntoQuestionPage(url)
    #print(url, all, stlx, stbh)
    spider.getAllQuestionPage(url, all, stbh,zsdDg)
    spider.close()

if __name__ == '__main__':
    main()
