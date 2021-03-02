from config import Config
from oasystem import createApp, db
from flask_script import Command
from flask_script import Manager
# 4.导入类
from flask_migrate import MigrateCommand

app = createApp(Config)


class SayHello(Command):

    def run(self):
        print('say hello...')


class RunServer(Command):

    def run(self):
        db.create_all(app=app)
        app.run(debug=False, host='0.0.0.0', port=5000)


manager = Manager(app)

manager.add_command('sayhello', SayHello)
manager.add_command('run', RunServer)
# 5.安装命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

