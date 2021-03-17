import pandas as pd
import datetime
import numpy as np


pd.set_option('display.max_column',None)
# 1. 将数据做存储并且设置前三列为合适的索引
out = pd.read_table('./pandas_exercise/exercise_data/wind.data', sep='\s+', parse_dates=[['Yr', 'Mo', 'Dy']])
print(out)

# 2. 2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)


out['Yr_Mo_Dy'] = out['Yr_Mo_Dy'].apply(fix_century)
print(out)
# 3. 将日期作为索引,注意数据类型,datetime[ns]
out['Yr_Mo_Dy'] = pd.to_datetime(out['Yr_Mo_Dy'])  # 日期转换pd.to_datetime()
out.set_index(keys='Yr_Mo_Dy', inplace=True)  # 修改行索引


# 4.对应每一个location,一共有多少数据值缺失
out.info()
print(out.isnull().sum())

# 5.对于每一个location，一共有多少完整的数值
print(out.notnull().sum())  # 判断非空notnull()
print(out.shape[0] - out.isnull().sum()) # 行数-每列缺失值，就是每列非缺失值

# 6. 对于全体数据，计算风速平均值
print(out.mean().mean())

# 7.创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
loc_stats = out.apply(['max', 'min', 'mean', 'std'])  # apply可以接受含多个统计函数的列表
matrix = np.mat(loc_stats.values)  # 配合矩阵转置，实现行列完全转换
matrix_T = matrix.T
# print(matrix)
loc_stats = pd.DataFrame(data=matrix_T, index=loc_stats.columns, columns=loc_stats.index)
print(loc_stats)

# 8.创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差
print(out)
day_stats = pd.DataFrame()
day_stats['min'] = out.min(axis=1) # 按列方向所有位置求聚合
day_stats['max'] = out.max(axis=1)
day_stats['mean'] = out.mean(axis=1)
day_stats['std'] = out.std(axis=1)

# print(day_stats.head())

# 9.对于每一个location，计算一月份的平均风速

out['date'] = out.index
out['month'] = out['date'].apply(lambda date: date.month)  # 拆分日期分别为年月日，方便使用query取月、日、年、
out['year'] = out['date'].apply(lambda date: date.year)
out['day'] = out['date'].apply(lambda date: date.day)
print(out)
january_winds = out.query('month == 1')  # query参数是字符串规则
print(january_winds.loc[:, 'RPT':'MAL'].mean())


# 10. 对于数据记录按照年为频率取样
# print(out.resample('A').mean())
print(out.query('month==1 and day==1'))
# 11. 对于数据记录按照月为频率取样
# print(out.resample('M').mean())
