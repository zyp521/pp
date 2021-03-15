import pandas as pd

# 显示所有列名称
pd.set_option('display.max_column', None)

out = pd.read_csv('./pandas_exercise/exercise_data/Euro2012_stats.csv', sep=',')
print(out)
out.info()

# 1.有多少只球队参与了2012欧洲杯？
print(out['Team'].nunique())

# 2.该数据集一共有多少列
print(out.shape[1])

# 3.将数据集中的列Team,Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = out[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# 4.将数据框discipline按照先Red Cards再Yellow Cards 进行排序
discipline.sort_values(by=['Red Cards', 'Yellow Cards'], inplace=True)  # 按多列先后排序，以列表形式填入，列表前面的先排
print(discipline)

# 5.计算每个球队拿到黄牌数的平均值
print(discipline['Yellow Cards'].mean())

# 6.找到进球数Goals超过6的球队数据
mask = out['Goals'] > 6
print(out.loc[mask, ])

# 7.选取以字母G开头的球队数据
mask = out['Team'].str.startswith('G')
print('##############################')
print(out.loc[mask, ])

# 8.选取前7列
# print(discipline.head(7))  # df.loc[行信息，列信息]
# print(discipline[:7])
# print(discipline.iloc[:7, ])
print(out.iloc[:, 0:7])

# 9.选取除了最后3列之外的全部列
print(out.iloc[:, :-3])

# 10.找到英格兰（England）、意大利(Italy)、俄罗斯(Russia)的射正率（Shooting Accuracy）
print(out.loc[out.Team.isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])
