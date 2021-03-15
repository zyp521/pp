#地铁线路哪一个城市地铁站点最多
import pandas
subways=pandas.read_csv("subway.csv",names=["city","line","station"])
# 按照city进行分组，求count()
subway_city=subways.groupby("city").count()
#分组排序，按降序来进行排序
subway_city=subway_city.sort_values("station",ascending=False)
print(subway_city)