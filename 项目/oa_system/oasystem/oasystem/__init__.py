from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 1.导入
from flask_migrate import Migrate

db = SQLAlchemy()
# 2.创建对象
migrate = Migrate()


def createApp(obj):
    app = Flask(__name__)
    app.config.from_object(obj)
    db.init_app(app)
    # 3.初始化操作
    migrate.init_app(app, db)
    from oasystem.user.views import userbp
    app.register_blueprint(userbp)
    return app
