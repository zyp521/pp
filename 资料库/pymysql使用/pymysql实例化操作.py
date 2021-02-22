from py3 import MyDB
import  setting
# 实例化
db = MyDB(h=setting.HOST,u=setting.USER,p=setting.PASSWORD,db=setting.DATABASE,P=setting.PORT)

# 查询数据
sql = "select * from user where id=%s"

res = db.select(sql,(4,))

print(res)