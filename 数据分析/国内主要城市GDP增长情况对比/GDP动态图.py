import pandas as pd
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts

data = pd.read_csv('GDPs.csv', sep='\s+')
data = data[['地区'] + [f'201{i}年' for i in range(1, 10)]]
print(data)
data.to_excel('GDPs.xlsx')

t1 = Timeline(init_opts=opts.InitOpts(width="1200px", height="800px", bg_color='blue'))
for i in range(1, 10):
    bar = Bar()
    data_temp = data[['地区', f'201{i}年']].copy()
    data_temp.sort_values(axis=0, ascending=True, inplace=True, by=f'201{i}年')
    print(data_temp)
    bar.add_xaxis(data_temp['地区'].values.tolist())
    bar.add_yaxis('国民生产总值/亿元', data_temp[f'201{i}年'].values.tolist())
    bar.reversal_axis()
    bar.set_global_opts(title_opts=opts.TitleOpts(f'201{i}年GDP'),)
                        #xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45, interval=0)))
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    t1.add(bar, f'201{i}年')
    t1.add_schema()

t1.render('timeline.html')
