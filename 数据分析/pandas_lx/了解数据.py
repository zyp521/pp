import pandas as pd

# 1.pandas下查看全部字段列
pd.set_option('display.max_column', None)
# pandas下查看全部行
# pd.set_option('display.max_rows', None)
# pandas下设置value的显示长度，默认为50
pd.set_option('max_colwidth', 50)

out = pd.read_csv('./pandas_exercise/exercise_data/chipotle.tsv', sep='\t')# seq csv文件字段分割符
print(out)

# 2.读取前10行内容
print(out.head(10))
# 3.查看数据多少列,列名称,行索引
print(out.shape[1], out.columns, out.index)
# 4.被下单数最多的商品(item)是什么
c = out[['item_name', 'quantity']].groupby(by='item_name')['quantity'].sum()  # 直接聚合，不使用agg生成series
c.sort_values(inplace=True, ascending=False)
print(c.head(5))

# 5.一共有多少商品被下单
print(len(out['item_name'].unique()))  # 去除重复值，返回去重后的series

# 6.将价格转换为浮点数
out['item_price'] = out['item_price'].str[1:].agg(float)  # 价格字符串切分，转化为浮点数，agg可直接跟python内置函数
print(out['item_price'])

# 7.在该数据集对应的日期内收入是多少
out['revenue'] = out['item_price']*out['quantity']
print(out['revenue'].sum())

# 8.在该数据集对应日期内，一共有多少订单
print(out['order_id'].nunique())

# 9.每一单（order）对应的平均总价是多少？
avg_price = out[['order_id', 'revenue']].groupby(by='order_id')[['revenue']].mean()
print(avg_price)

# 10.一共有多少种商品被被售出
print(out['item_name'].nunique())
