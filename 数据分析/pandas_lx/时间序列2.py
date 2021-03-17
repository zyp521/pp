import pandas as pd

data = pd.read_csv('./pandas_exercise/exercise_data/Apple_stock.csv', sep=',')
print(data)
data.info()


# 1.将Date这个列转换为datetime类型

# 2. 将Date设置为索引

# 3. 有重复的日期吗

# 4.将index设置为升序

# 5. 找到每个月的最后一个交易日(business day)

# 6. 数据集中最早的日期与最晚的日期相差多少天？

# 7. 在数据中一共有多少个月

# 8. 按照时间顺序可视化Adj Close值

