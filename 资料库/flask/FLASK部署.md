# 1.安装python3 环境依赖

 

```
 yum install zlib-devel libffi-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc* make -y
```

# 2.python3.7压缩包, 解压，编译，安装

1. 压缩包放在 **/opt**（放置第三方软件，rz命令用于文件上传）

2. 解压 **tar -xvJf Python3.7...**（当前文件 /opt下解压）
3. 配置环境生成makefile 进入到Python3.7目录下运行  **./configure prefix=/usr/local/python3**（环境安装目录）

4. 安装 **make**(编译：变成可执行的2进制文件） **&& make install**（安装）(python-3.7.0 目录下安装）

# 3.建立软连接

   1. 进入安装的位置 **cd /usr/local/**(可看到新安装的python3)

2.  **ln -s /usr/local/python3/bin/python3 /usr/bin/python3** 

    **ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3**(相当于添加环境变量）

# 4.python 运行模块加载

1. **pip freeze > package.tx**t(放到/opt目录下)

2. **pip install -r package.txt** -i https://mirrors.aliyun.com/pypi/simple/  (阿里源）

# 5.安装uwsgi模块

   1.**pip3 install uwsgi**

2. **ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi**



# 6.1 uwsgi单独作服务器时

​    1.uwsgi.ini配置 uwsg.ini

```python
  [uwsgi]

  http=0.0.0.0:5000                配置uwsgi监听的socket(ip+端口)
  callable=app
  daemonize=/opt/scripts/uwsgi.log
  processes=8
  threads=4
  wsgi-file=/opt/oasystem/main.py
  module=main
  pidfile=uwsg.pid
  chdir=/opt/oasystem
  master=true
  vacuum=true
```



2. uwsgi操作命令

   ```python
   uWSGI 启动：
   uwsgi --ini xxx.ini
   
   uwsgi 重启：
   uwsgi --reload xxx.pid
   
   uwsgi 停止：
   uwsgi --stop xxx.pid
   ```

   



# 6.2 uwsgi配合nginx部署时

​    1. uwsgi配置 uwsgi.ini

  

```
[uwsgi]

  socket=127.0.0.1:5000                      /使用nginx连接时, 监控地址          
  callable=app                              //uwsgi调用的python应用实例名称,Flask里   默认是app,根据具体项目代码实例命名来设置

  daemonize=/opt/scripts/uwsgi.log           以守护进程运行，日志文件路径
  processes=8                                 配置进程数量
  threads=4                                   配置线程数量
  wsgi-file=/opt/oasystem/main.py             项目中wsgi.py文件的目录，相对于项目目录
  module=main                                 项目控制文件名（不加.py）
  pidfile=uwsg.pid                            存放uwsgi进程的pid，便于重启和关闭操作
  chdir=/opt/oasystem                         项目目录//指定运行目录
  master=true                                 独立守护进程运行/是否需要主进程
  vacuum=true                                  当服务器退出的时候自动清理环境，删除unix socket文件和pid文件
    
  home=/data/opt/Myproject/venv  # which  pytho  #指定解释器目录
```



# 7.Nginx安装

1.压缩包放在 /opt（放置第三方软件，rz命令用于文件上传）

2.解压 **tar -xvzf nginx-1.12.2.tar.gz**（当前文件 /opt下解压）

3.配置环境生成makefile 进入到**nginx-1.12.2**目录下运行  **./configure** 

4.安装 **make**(编译：变成可执行的2进制文件） **&& make install**（安装)

5.**Ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx**

# 8.nginx 启动

1. nginx 命令 直接启动

2. ngixn 操作命令

   ```
   nginx -s stop 停止nginx
   nginx -s reload 重启nginx
   nginx -t 检测是否正确
   ```

   

# 9.flask+nginx+uwsgi部署

1. 配置nginx.cof
       **cd /usr/local/nginx/conf/nginx.conf**

2.   nginx服务配置

   ```
   server {
       listen    80;
       server_name oasystem;# 服务名
       #charset utf-8;
   
    #access_log  logs/host.access.log main;
    access_log logs/host.access.log;
    error_log logs/host.error.log;
   
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:5000;
        uwsgi_param UWSGI_CHDIR /opt/oasystem;
        uwsgi_param UWSGI_SCRIPT main:app;}
   }
   ```

   

