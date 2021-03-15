#统计城市地铁线路最多,先不要站点
#分组条件：city,line
import pandas
subways=pandas.read_csv("subway.csv",names=["city","line","station"])
subways=subways[["city","line"]]
subways=subways.drop_duplicates().reset_index()
subways=subways[["city","line"]]
count_subway=subways.groupby("city").count()
count_subway=count_subway.sort_values("line",ascending=False)
print(count_subway)