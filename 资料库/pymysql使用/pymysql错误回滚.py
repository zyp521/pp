import pymysql

db = pymysql.connect(host="127.0.0.1",user="root",password="root",port=3306,database="demo")

cursor = db.cursor()

sql1 = "insert into user(name) value(%s)"
try:
    cursor.execute(sql1,("老王",))
    cursor.execute(sql2,("老王",))
    db.commit()
except:
    db.rollback()
finally:
    cursor.close()
    db.close()