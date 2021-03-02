# 创建application对象
import tornado.web
from urls import urlpatterns
from settings import torando_config


def make_app():
    app = tornado.web.Application(
        urlpatterns,
        **torando_config,
        # debug=True,
        # autoreload=True
    )
    return app
