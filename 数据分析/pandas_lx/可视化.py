import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Scatter, Bar

pd.set_option('display.max_column',None)

data = pd.read_csv('./pandas_exercise/exercise_data/train.csv', sep=',')
print(data.head())


# 1.将PassengerId设置为索引
data.set_index(keys='PassengerId', inplace=True)
print(data)
# 2.绘制一个展示男女乘客比例的扇形图
out = data.groupby(by='Sex')['Sex'].count()
k = out.index
v = out.values.tolist()

data_pair = [list(i) for i in zip(k, v)]
pie = Pie()
pie.add('', data_pair=data_pair, radius=['30%', '70%'], center=['50%', '50%'], rosetype='area')
pie.set_global_opts(title_opts=opts.TitleOpts(title='玫瑰图'))
pie.render('./pandas_exercise/template/pie_rosetype.html')


# 3. 绘制一个展示船票Fare，与乘客年龄和性别的散点图
data.info()
out1 = data.query("Sex == 'male'")[['Age', 'Fare']]  # query查询条件等于字符串，字符串得加引号
out2 = data.query("Sex == 'female'")[['Age', 'Fare']]
print(out1.isnull().sum())
print(out2.isnull().sum())
out1 = out1.loc[out1.Age.notnull(), :]
out2 = out2.loc[out2.Age.notnull(), :]
print(out1.max(), out2.max())
scatter = Scatter(init_opts=opts.InitOpts(width='1200px', height='600px', bg_color='#f8f8f8'))
scatter.add_xaxis([i for i in range(0, 81, 1)])
scatter.add_yaxis(series_name='male', y_axis=out1.Fare.values.tolist(), label_opts=opts.LabelOpts(is_show=False))
scatter.add_yaxis(series_name='female', y_axis=out2.Fare.values.tolist(), label_opts=opts.LabelOpts(is_show=False))
scatter.set_global_opts(title_opts=opts.TitleOpts(title='男女票价散点分布图',
                                                  title_textstyle_opts=opts.TextStyleOpts(font_weight='bolder',
                                                                                          font_size=30)),
                        xaxis_opts=opts.AxisOpts(name='年龄', name_location='center', name_gap=30,
                                                 name_textstyle_opts=opts.TextStyleOpts(font_weight='bolder',
                                                                                        font_size=24),
                                                 axislabel_opts=opts.LabelOpts(interval=9)),
                        yaxis_opts=opts.AxisOpts(name='票价', name_location='center', name_gap=30,
                                                 name_textstyle_opts=opts.TextStyleOpts(font_weight='bolder',
                                                                                        font_size=24)
                                                 ))
scatter.render('./pandas_exercise/template/scatter.html')

# 4. 有多少人生还
print('生还人数', data.Survived.sum())

# 5. 绘制一个展示船票价格的直方图
bar = Bar()
print(data.Fare.describe())
data['Fare_'] = pd.cut(data.Fare, bins=[i for i in range(0, 600, 10)])
out = data[['Fare', 'Fare_']]
out = out.groupby(by='Fare_')[['Fare']].count()
bar.add_xaxis(list(range(0, 600, 10)))
bar.add_yaxis('票价', out.Fare.values.tolist(), category_gap=0, markpoint_opts=opts.MarkPointOpts(
    data=[opts.MarkPointItem(type_='min'), opts.MarkPointItem(type_='max')], symbol='circle',symbol_size=30))
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar.render('./pandas_exercise/template/bar_base.html')



