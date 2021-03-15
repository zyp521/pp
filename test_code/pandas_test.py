import pandas as pd

df = pd.read_excel('pandas_apply_test.xlsx')
print(df)

# apply对多列进行操作
# df['归属日期'] = df.apply(lambda x: x['送达日期'] if x['送达日期']is not pd.NaT else x['调度日期'], axis=1)
# # print(df)

# apply对单列进行操作
# df['送达日期'] = df.apply(lambda x: x['送达日期'] if x['送达日期'] is not pd.NaT else 0, axis=1)
# df['送达日期'] = df['送达日期'].transform(lambda x: x if x is not pd.NaT else 0)
df['送达日期'] = df['送达日期'].agg(lambda x: x if x is not pd.NaT else 0)
print(df)
