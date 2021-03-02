from django.db import models


# Create your models here.

class Seller(models.Model):
    username = models.CharField(max_length=32, default='zs')  # 用户名
    password = models.CharField(max_length=128, default='123')  # 密码
    email = models.CharField(max_length=128, default='110@qq.com')  # 邮件
    phone = models.CharField(max_length=128, default='110')  # 电话
    address = models.CharField(max_length=128, default='beijing')  # 地址
    gender = models.BooleanField(default=True)  # 男
    # 头像，逻辑操作比较方便,当保存对象时候，会自动将上传的文件进行保存。
    # 2. upload_to 指定上传文件的具体目录。
    # 3. 需要下载pillow模块
    headimg = models.ImageField(upload_to='img', default='1.jpg')


class Store(models.Model):
    name = models.CharField(max_length=32, default='湛江第一烧烤小店')
    address = models.CharField(max_length=128, default='广州南沙')
    desc = models.CharField(max_length=128, default='好吃')
    logo = models.ImageField(upload_to='img', default='1.jpg')
    # 设置关系 店铺和卖家一对一
    seller = models.OneToOneField(to=Seller, on_delete=models.CASCADE)


# 商品类型
class GoodsType(models.Model):
    name = models.CharField(max_length=32, default='奇异果')
    logo = models.ImageField(upload_to='img', default='1.jpg')


# 商品
class Goods(models.Model):
    name = models.CharField(max_length=32, default='苹果')
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    bzq = models.IntegerField(default=30)  # 保质期
    scrq = models.DateField(null=True, blank=True)  # 生产日期
    desc = models.CharField(max_length=128, default='好东西.')  # 商品描述
    image = models.ImageField(upload_to='img', default='1.jpg')  # 商品图片
    content = models.TextField(default='详情介绍.')  # 商品详情
    # 商品类型和商品是一对多关系。
    goodstype = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)
    # 店铺和商品是一对多关系
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE, null=True, blank=True)
