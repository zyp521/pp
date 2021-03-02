# 启动项目
import tornado.ioloop
from app import make_app
from models import Base

if __name__ == '__main__':
    # 1.创建数据库
    Base.metadata.create_all()
    # 2.监听端口号
    app = make_app()
    app.listen(9999)
    # 3.启动项目
    tornado.ioloop.IOLoop.current().start()
