import pandas as pd

pd.set_option('display.max_column', None)
out = pd.read_csv('./pandas_exercise/exercise_data/drinks.csv', sep=',')
print(out)

# 1.那个大陆(continent)平均消耗的啤酒(beer)更多
print('********************************************************')
# for i in out.groupby(by='continent'):
#     print(i)
# print(out.groupby(by='continent').get_group('AF')) # 获取分组后指定组信息
print(out.groupby(by='continent')['beer_servings'].agg('mean').sort_values(ascending=False))
# 2.打印出每个大陆（continent）的红酒消耗（wine_servings）的描述性统计值
print(out.groupby(by='continent')['wine_servings'].describe())
# 3.打印出每个大陆每种酒类列的消耗平均值
print(out.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].agg('mean'))
# 4. 打印出每个大陆每种酒列别的消耗中位数
print(out.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].agg('median'))
# 5.打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
print(out.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].agg(['mean', 'max', 'min']))
