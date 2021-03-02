# Django celery 异步通讯



## 一  安装相应模块

#### 1.安装模块

```python
pip install django-celery==3.2.2
Pip install django-redis
Pip install redis ==2.10.6 
```

#### 2.安装redis数据库

```
1.Redis-x64-3.2.100.zip  解压到相应目录如下图
```

![解压图](C:\Users\Administrator\Desktop\新建文件夹\statics\20201021084922.png)

```
2. 直接运行 redis-server.exe 启动redis 端口：6379， 如下图
```

![](C:\Users\Administrator\Desktop\新建文件夹\statics\redis启动.png)

```
3. 关闭redis数据库，直接执行 redis-cli.exe ,执行后+shutdown
```

