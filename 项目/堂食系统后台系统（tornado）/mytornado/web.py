import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.gen
import json
import tornado.concurrent
from concurrent.futures import ThreadPoolExecutor
#定义类，继承于tornado.web.RequestHandler
class InfoHandler(tornado.web.RequestHandler):
    #定义线程池
    executor=ThreadPoolExecutor(10000)
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()
    #在进行tornado并发处理时，要用一个线程池来维护是最好的
    @tornado.concurrent.run_on_executor
    def get_response(self):
        foods_json=[
              {
                "name": "地三鲜",
                "images": "/static/images/disanxian.jpeg",
                "price": 13.00
              },
              {
                "name": "西红柿牛楠",
                "images": "/static/images/niunan.jpg",
                "price": 53.00
              },
              {
                "name": "红烧鸡块",
                "images": "/static/images/hongsaojikuai.jpg",
                "price": 28.00
              },
              {
                "name": "水煮肉",
                "images": "/static/images/suizhurou.jpg",
                "price": 35.00
              },
              {
                "name": "凉拌土豆丝",
                "images": "/static/images/todousi.jpg",
                "price": 10.00
              }
            ]
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","Content-Type")
        self.set_header("Content-Type","application/json;charset=UTF-8")
        foods=json.dumps(foods_json)
        self.write(foods)
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("MY Hello!")
        self.write("Hello World")


if __name__=="__main__":
    application=tornado.web.Application(
        handlers=[
            (r"/",InfoHandler),
            (r"/hello", HelloHandler)
        ]
    )
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(8001)
    tornado.ioloop.IOLoop.instance().start()