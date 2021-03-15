import pandas as pd

raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# 字典形式创建表格数据
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

print(data1)
print(data2)
print(data3)

# 1.将data1和data2两个数据框按照行的维度进行合并，命名为all_data
all_data = pd.concat((data1, data2))
# all_data = data1.append(data2)
print(all_data)

# 2.将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
all_data_col = pd.concat((data1, data2), axis=1)
print(all_data_col)
# 3.按照subject_id的值对all_data和data3作合作
out = pd.merge(left=all_data, right=data3, on='subject_id') # merge只能实现左右合并,关联列只留下一列
print(out)
# 4.对data1和data2按照subject_id做链接
out = pd.merge(left=data1, right=data2, on='subject_id')
print(out)
# 5.找到data1和data2合并后的所有匹配结果
out = pd.merge(left=data1, right=data2, on='subject_id',how='outer')
print(out)
