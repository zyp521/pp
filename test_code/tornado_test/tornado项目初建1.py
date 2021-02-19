# 1.导入模块
import tornado.web  # 负责应用程序开发
import tornado.ioloop  # 负责服务程序
import tornado.gen


# 2.  创建视图类
class IndexHandler(tornado.web.RequestHandler):
    # 对应get方式
    @tornado.gen
    def get(self):
        yield self.write('hello word')


# 3. 编写路由
if __name__ == '__main__':
    app = tornado.web.Application([(r'/hello/', IndexHandler), ])
    # 4. 设置端口
    app.listen(8848)
    # 5. 服务启动
    tornado.ioloop.IOLoop.current().start()
