import pandas as pd
import MyDB_, settings


# 从数库中读取数据并保存成excel表格

db = MyDB_.MyDB(h=settings.HOST, u=settings.USER, p=settings.PASSWORD, db=settings.DATABASE)
data = db.select('select * from douluo_comment')
data_ids = []
data_comment = []
data_type = []
for i in data:
    data_ids.append(i[0])
    data_comment.append(i[1])
    data_type.append(i[2])

datas = pd.DataFrame({'ids': data_ids, 'comment': data_comment, 'type': data_type})
datas.to_excel('./statics/douluo_comment.xlsx',sheet_name='斗罗大陆真人版评论')