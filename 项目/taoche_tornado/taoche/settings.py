# 配置文件
import os

# 1.数据库配置
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(BASE_DIR, 'db1.sqlite')

# 2. tornado 参数的配置

torando_config = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}
