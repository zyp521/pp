import pymysql

class MyDB:
    def __init__(self,h,u,p,db,P=3306):
        self.db = pymysql.connect(host=h,user=u,password=p,database=db,port=P)
        self.cursor = self.db.cursor()

    def select(self,sql,data):
        self.cursor.execute(sql,data)
        res = self.cursor.fetchall()
        return res

    def update(self,sql,data):
        res = self.cursor.execute(sql, data)
        self.db.commit()
        return res


    def __del__(self):
        self.cursor.close()
        self.db.close()