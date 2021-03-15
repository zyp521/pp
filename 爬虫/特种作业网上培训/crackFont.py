#encoding=utf-8
from fontTools.ttLib import TTFont
import requests
import time
import os
import json

def download_font(index):
    url="http://jmaspx.tskspx.com/font/font%d/sfont.ttf"% index
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "jmaspx.tskspx.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    }
    try:
        req = requests.get(url,headers=headers,timeout=5)
        with open("fonts/download/%d.ttf" % index,"wb") as  f:
            f.write(req.content)
        return True
    except Exception as e:
        print(e)
    return False

# for i in range(12):
#     download_font(i)
#     time.sleep(2)

# font2 = TTFont('fonts/download/9.ttf')  # 打开访问网页新获得的字体文件02.ttf
# obj_list2 = font2.getGlyphNames()[5:]
# uni_list2 = font2.getGlyphOrder()[5:]
#

font1=TTFont('fonts/01.ttf')    #打开本地字体文件01.ttf
obj_list1=font1.getGlyphNames()[5:]   #获取所有字符的对象，去除第一个和最后一个
uni_list1=font1.getGlyphOrder()[5:]    #获取所有编码，去除前2个
word_dict = {
        "uniE0A0": "o",
        "uniE123": "Q",
        "uniE1F2": "E",
        "uniE231": "1",
        "uniE2DC": "M",
        "uniE35D": "P",
        "uniE4EA": "6",
        "uniE4FE": "m",
        "uniE5DE": "D",
        "uniE630": "8",
        "uniE6ED": "Y",
        "uniE6F5": "S",
        "uniE7A0": "N",
        "uniE7A2": "k",
        "uniE7A4": "7",
        "uniE7A6": "b",
        "uniE7E1": "5",
        "uniE8AE": "i",
        "uniE8C0": "2",
        "uniE9A2": "3",
        "uniE9B2": "R",
        "uniEAAA": "w",
        "uniEABC": "p",
        "uniEAE1": "t",
        "uniEBA3": "I",  # I am
        "uniEBCF": "e",
        "uniECAE": "f",
        "uniECB2": "z",
        "uniECFA": "1",# 123
        "uniEDFD": "X",
        "uniEEEE": "9",
        "uniEF21": "g",
        "uniEF32": "s",
        "uniEF3A": "r",
        "uniEFAB": "0",
        "uniEFEF": "G",
        "uniEFFA": "U",
        "uniF012": "B",
        "uniF013": "x",
        "uniF014": "T",
        "uniF015": "a",
        "uniF016": "j",
        "uniF017": "V",
        "uniF028": "d",
        "uniF065": "h",
        "uniF090": "A",
        "uniF093": "c",
        "uniF0AC": "F",
        "uniF0EB": "K",
        "uniF134": "4",
        "uniF13B": "n",
        "uniF191": "H",
        "uniF1CB": "L",
        "uniF31B": "C",
        "uniF32B": "Z",
        "uniF342": "y",
        "uniF3DB": "W",
        "uniF3DE": "O",
        "uniF42B": "u",
        "uniF43C": "J",
        "uniF563": "v",
        "uniF5A2": "q",
    }

def comp(L1,L2):
    if abs(len(L1) -len(L2))!= 0:
        return -1000
    mark= 0
    for l1 in sorted(L1,key=lambda x:x[0]):
        for l2 in sorted(L2,key=lambda x:x[0]):
            mark -= ((l1[0]-l2[0])*(l1[0]-l2[0]) + (l1[1]-l2[1])*(l1[1]-l2[1]))
    return mark

def comp(l1,l2):  #定义一个比较函数，比较两个列表的坐标信息是否相同
    if len(l1)!=len(l2):
        return False
    else:
        mark=1
        for i in range(len(l1)):
            if abs(l1[i][0]-l2[i][0])<40 and abs(l1[i][1]-l2[i][1])<40:
                pass
            else:
                mark=0
                break
        return mark


def getDict():
    final_dict={

    }
    font = TTFont('fonts/01.ttf')
    uni_list = font.getGlyphOrder()[5:]
    on_p = []
    for i in uni_list:
        pp1 = []
        p = font['glyf'][i].coordinates
        for f in p:
            pp1.append(f)
        on_p.append(pp1)

    for num in range(0,11):
        font2 = TTFont('fonts/download/%d.ttf' % (num+1))
        uni_list2 = font2.getGlyphOrder()[5:]
        on_p1 = []
        for i in uni_list2:
            pp1 = []
            p = font2['glyf'][i].coordinates
            for f in p:
                pp1.append(f)
            on_p1.append(pp1)
        for i in range(len(on_p)):
            L1 = on_p[i]
            curMax = None
            max_mark = -100000000
            for j in range(len(on_p1)):
                L2 = on_p1[j]
                # m = comp(L1,L2)
                # print(m)
                # if m >= max_mark:
                #     max_mark = m
                #     curMax = uni_list2[j]
                if comp(L1,L2):
                    curMax = uni_list2[j]

            if "jerry%d" % (num) not in final_dict:
                final_dict["jerry%d" % (num)]={}
            final_dict["jerry%d" % (num)][curMax]=word_dict[uni_list[i]]
        print("jerry%d" % (num))
        print([final_dict["jerry%d" % (num)][key] for key in uni_list2])

    return final_dict




for i in range(1,11+1):
    if not os.path.exists("fonts/download/%d.ttf" % i):
        print("字体不存在，正准备下载.","fonts/download/%d.ttf" % i)
        download_font(i)
        time.sleep(2)
print("准备生成字体转换表.如果网站字体更新请主动删除 fonts/tr.json")
if not os.path.exists("fonts/tr.json"):
    final_dict = getDict()
    with open("fonts/tr.json","w") as f:
        f.write(json.dumps(final_dict))

final_dict=json.load(open("fonts/tr.json","r"))
print("生成字体转换表完成")


def crack(cls,words):
    ans=""
    for word in words:
        try:
            uni=word.encode('unicode_escape').decode()[2:]
            key = "uni"+ uni.upper()
            #print(repr(cls),repr(key))
            if cls in final_dict and key in final_dict[cls]:
                ans+=final_dict[cls][key]
            else:
                #print(word,"not in")
                ans+=word
        except Exception as e:
            print(e)
    return ans



def do_req():
    from lxml import etree
    url="http://jmaspx.tskspx.com/user/0704/getNextQuestion.do?&stlx=0&answer=&stbh=3052181"
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=62D8CDC1D2C37C6A9E0B73A804B5A237",
        "Host": "jmaspx.tskspx.com",
        "Referer": "http://jmaspx.tskspx.com/user/0704/getNextQuestion.do?currentPage=6&stlx=&answer=&stbh=3052178",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    }
    data={
        "currentPage": "7",
        "stlx": "",
        "answer": "",
        "stbh": "3052181",
    }
    req = requests.get(url,headers=headers)
    html = etree.HTML(req.content.decode("utf-8"))
    with open("a.html",'wb') as f:
        f.write(req.content)
    answer= html.xpath('//table[@class="plxanswer2"]//span/text()')[0]
    font_num=html.xpath('//table[@class="plxanswer2"]//span/@class')[0]
    try:
        td = html.xpath('//td[@class="headtop"]')[0]
    except Exception as e:
        print(e)
        time.sleep(2)
    title = td.xpath('span[2]/text()')[0].strip()
    print(title)
    for x in title:
        print(x,type(x),x.encode('unicode_escape').decode())
    print(answer.encode("unicode_escape"))
    print(font_num)
    num =int(font_num[5:])
    ans = crack(font_num,title)
    print(ans)











#do_req()