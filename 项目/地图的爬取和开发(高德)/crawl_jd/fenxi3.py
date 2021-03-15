#统计城市地铁线路中站台最多的线
import pandas
subways=pandas.read_csv("subway.csv",names=["city","line","station"])
sta_subways=subways.groupby(["city","line"]).count()
sta_subways=sta_subways.sort_values("station",ascending=False)
print(sta_subways)