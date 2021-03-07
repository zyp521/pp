import pymongo
import settings

# 创建mongodb客户端
Mongo_client = pymongo.MongoClient(host=settings.HOST_Mongo, port=settings.PORT_Mongo)
# 切换数据库
db = Mongo_client['mt_test']
# 选择集合
collection = db['douluo_comment']






