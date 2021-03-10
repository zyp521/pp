import pandas as pd
import MongoDB

# 从mongo数据库读取数据
data = MongoDB.MongoDB().find()
# 对数据进行初步处理
for index, item in enumerate(data):
    item.update({'_id': index, 'title': item['title'][1], 'size': ''.join([item['size'][i] for i in range(1, 10)]),
                 'address': item['address'][1].split('\n')[1].strip(), 'detail': '|'.join(item['detail']), 'price': int(item['price'][0])})
print(data)
columns = list(data[0].keys())
data = [list(i.values()) for i in data]
out = pd.DataFrame(columns=columns, data=data)
out['size'] = out['size'].str.strip()
# out['address'] = out['address'].str.split('\\n')
out = out[[i for i in out.columns[1:]]]
out.to_excel('zufang.xlsx')
