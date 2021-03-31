import pandas as pd
from pyecharts.charts import Line
import pyecharts.options as opts
import arrow

data = pd.read_csv('./pandas_exercise/exercise_data/Apple_stock.csv', sep=',')
print(data)
data.info()


# 1.将Date这个列转换为datetime类型
data['Date'] = pd.to_datetime(data['Date'])
# 2. 将Date设置为索引
data.set_index(keys='Date',inplace=True)
print(data)

# 3. 有重复的日期吗
print(data.index.is_unique)  # is_unique属性判断是否有重复的项
# 4.将index设置为升序
data.sort_index(ascending=True, inplace=True) # sort_index()按索引进行排序
print(data)
# 5. 找到每个月的最后一个交易日(business day)
apple_month = data.resample('BM').mean()  # 重采样目前得需要使用聚合
print(apple_month.head())

# 6. 数据集中最早的日期与最晚的日期相差多少天？
print('-------------------------------------------------------------------------------')
print(data.index.max() - data.index.min())

# 7. 在数据中一共有多少个月
print(data.resample('BM').mean().shape[0])
print(data)

# 8. 按照时间顺序可视化Adj Close值
data = data.resample('Q').mean()
line = Line(init_opts=opts.InitOpts(width='800px', bg_color='#f8f8f8'))


def get_year(timestamp):
    return arrow.get(timestamp).format('YYYY-MM-DD')


years = list(map(get_year, data.index.tolist()))
print(years)
line.add_xaxis(years)
line.add_yaxis('Adj_close', y_axis=[float('{:0.2f}'.format(i)) for i in data['Adj Close'].values.tolist()])
# line.set_series_opts(label_opts=opts.LabelOpts(interval=3)) # interval调整坐标轴刻度标签之间得间隔，不能直接修改系列标签显示
# line.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=12)))  # 坐标轴类目标签配置项，可间隔设置标签而不影响原数据
line.set_global_opts(xaxis_opts=opts.AxisOpts(name='日期'), yaxis_opts=opts.AxisOpts(name='销量/万'))
line.render('./pandas_exercise/template/line.html')

