# 1.导入模块
import pymysql

# 2.链接数据库
db = pymysql.connect(host="localhost", user="root", password="root",
                 database="demo", port=3306,cursorclass=pymysql.cursors.DictCursor)

# 3. 游标对象 :  所有的数据库操作都是基于游标对象
cursor = db.cursor()

# 4. 编写sql语句
sql = "select * from user,user_info where user.id=user_info.u_id"

# 5.执行sql
res = cursor.execute(sql)
print(res)
# 6.查看结果
# print(cursor.fetchone())
# print(cursor.fetchone())

print(cursor.fetchall())


# 7.关闭数据库链接
cursor.close()
db.close()

