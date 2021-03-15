import requests
from lxml import html
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"}
page=requests.get("https://list.jd.com/list.html?cat=1713,3258,3297",headers=headers)
jd_page=page.content.decode("utf8")
etree=html.etree
html_page=etree.HTML(jd_page)
lis=html_page.xpath("//ul[@class='gl-warp clearfix']/li")
for li in lis:
    book_title=li.xpath(".//div[@class='p-name']/a/em/text()")
    #book_href元素定位后是一个列表
    book_href=li.xpath(".//div[@class='p-name']/a/@href")
    #book_price=li.xpath(".//div[@class='p-price']/strong/i/text()")
    #将book_href切分用一个0元素
    book_html=book_href[0].split("/")[-1]
    book_skuid=book_html.split(".")[0]
    if book_skuid.find("=404")<0:
        print(book_skuid)
        print("")
        page_price_url="https://p.3.cn/prices/mgets?skuIds=J_"+book_skuid
        print(page_price_url)
        #通过请求p.3.cn京东价格服务器，不是单纯取其中的价格，把折扣价可以算出来的取价格。
        price_page=requests.get(page_price_url)
        book_price=price_page.json()
    print(book_title)
    if book_price:
        print(book_price)

