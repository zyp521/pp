from django.db import models

# 通过查询id 返回对象的名称
# 1.导入模块
from django.db.models import Manager


# 2.定义方法
class BuyerName(Manager):

    def get_buyer_name(self, id):
        buyer_obj = Buyer.objects.get(id=id)
        return buyer_obj.name


class Buyer(models.Model):
    name = models.CharField(max_length=32, default='zs')
    password = models.CharField(max_length=128, default='111')
    email = models.CharField(max_length=128, default='110@qq.com')
    phone = models.CharField(max_length=128, default='110')
    address = models.CharField(max_length=128, default='beijing')
    # 3.赋值对象
    objects = BuyerName()


# 购物车模型类
class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)  # 主键
    goodsid = models.IntegerField(default=1)  # 商品id
    goodsname = models.CharField(max_length=32, default='苹果')  # 商品名称
    goodsimg = models.CharField(max_length=128, default='1.jpg')  # 商品图片路径
    goodsprice = models.DecimalField(max_digits=5, decimal_places=2)  # 商品价格
    goodsnum = models.IntegerField(default=10)  # 商品数量
    storeid = models.IntegerField(default=1)  # 店铺id
    storename = models.CharField(max_length=32, default='烧烤小店')
    # 设置用户和购物车关系 实际上是用户和购物车表格中记录的关系。 一对多
    buyer = models.ForeignKey(to=Buyer, on_delete=models.CASCADE)


# 用户收货地址 模型类
class UserAddress(models.Model):
    name = models.CharField(max_length=32, default='zs')
    detail = models.CharField(max_length=128, default='beijing')
    youbian = models.CharField(max_length=128, default='10000')
    phone = models.CharField(max_length=32, default='110')
    status = models.BooleanField(default=False)  # 地址选中状态，默认不选中
    # 用户和地址是一对多关系
    buyer = models.ForeignKey(to=Buyer, on_delete=models.CASCADE)


# 订单表
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    orderno = models.CharField(max_length=32, default='100010')  # 订单号 格式 根据公司规定 202010160930
    orderdate = models.DateTimeField()  # 订单日期
    orderaddress = models.CharField(max_length=128)  # 用户收货地址
    ordertotalnum = models.CharField(max_length=32)  # 总价
    status = models.BooleanField(default=False)  # 订单状态 默认是False
    # 订单和用户
    buyer = models.ForeignKey(to=Buyer, on_delete=models.CASCADE)


# 订单详情表
class OrdersDetail(models.Model):
    goodsname = models.CharField(max_length=32)  # 商品名称
    goodsprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    goodsnum = models.IntegerField()  # 数量
    goodsimg = models.CharField(max_length=128)  # 图片路径
    goodsxiaoji = models.CharField(max_length=32)  # 小计
    orders = models.ForeignKey(to=Orders, on_delete=models.CASCADE)


# 验证码校验模型类

class CheckEmail(models.Model):
    emailname = models.CharField(max_length=32)  # 邮箱名称
    authcode = models.CharField(max_length=32)  # 验证码
    etime = models.DateTimeField()  # 记录验证码保存时间。
