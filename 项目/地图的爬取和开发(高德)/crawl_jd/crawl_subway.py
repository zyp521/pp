import requests
from bs4 import BeautifulSoup
def getinfo(id,cityname,name):
    res=requests.get("http://map.amap.com/service/subway?_1612234854108=&srhdata="+id+"_drw_"+cityname+".json")
    subway=res.json()
    for line in subway["l"]:
        for station in line["st"]:
            if len(line["la"])>0:
                with open("subway.csv","a+",encoding="utf8") as f:
                    f.write(name+","+line["ln"]+"("+line["la"]+")"+","+station["n"]+"\n")
            else:
                with open("subway.csv","a+",encoding="utf8") as f:
                    f.write(name+","+line["ln"]+","+station["n"]+"\n")
def get_city():
    url="http://map.amap.com/subway/index.html"
    response=requests.get(url)
    html=response.content.decode("utf8")
    print(html)
    soup=BeautifulSoup(html)
    citys=soup.find_all(class_="city-list")[0]
    print(citys)
    for city in citys.find_all("a"):
        id=city["id"]
        cityname=city["cityname"]
        name=city.get_text()
        getinfo(id,cityname,name)
    more_citys=soup.find_all(class_="more-city-list")[0]
    for more_city in more_citys.find_all("a"):
        id=more_city["id"]
        cityname=more_city["cityname"]
        name=more_city.get_text()
        getinfo(id,cityname,name)
if __name__=="__main__":
    #getinfo("1100","beijing","北京")
    get_city()