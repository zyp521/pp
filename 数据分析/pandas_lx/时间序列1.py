import pandas as pd

pd.set_option('display.max_column',None)

out = pd.read_csv('./pandas_exercise/exercise_data/US_Crime_Rates_1960_2014.csv', sep=',')


# 1.将Year的数据类型转换为datetime64
# out['Year'].astype('datetime64[ns]')
out.Year = pd.to_datetime(out.Year, format='%Y') # 转换日期pd.to_datetime()
out.info()

# 2.将列Year设置为数据框的索引
out.set_index(keys='Year', inplace=True)
print(out)

# 3.删除名为Total的列
out.drop(columns='Total', inplace=True)
# del out['Total']
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&-------------------------------------&')
print(out)

# 4.按照Year对数据框进行分组并求和
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
out = out.resample('10AS').max()
# out['Population'] = out['Population'].resample('10AS').max()
print(out.iloc[:,:-4])

# 5.何时是美国历史上生存最危险的年代

print(out.idxmax(0))  # 找出每列最大值索引
