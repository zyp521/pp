import requests
import MyDB
import settings

db = MyDB(h=settings.HOST, u=settings.USER, p=settings.PASSWORD, db=settings.DATABASE)

sql = 'insert into douluo_comment(comment,comment_type) values(%s,%s)'
data = ('我爱你', '好')

db.update(sql, data)
