from django.shortcuts import render, redirect
from seller import models


# Create your views here.

def index(request):
    # 1.查询所有的商品类型
    goodstype_obj_list = models.GoodsType.objects.all()
    # 2.轮播图 图片
    lb_goods_obj_list = models.Goods.objects.all().order_by('-id')[0:4]

    return render(request, 'buyer/index.html', locals())


# 查看更多
# 传统方式返回
def more_goods_list_v1(request):
    # 1.获取商品类型的id
    goodstype_id = request.GET.get('goodstype_id')
    # 2.查询当前商品类型对应的所有的商品
    goods_obj_list = models.Goods.objects.filter(goodstype_id=goodstype_id)
    # 3.返回页面
    return render(request, 'buyer/list_test.html', {'goods_obj_list': goods_obj_list})


def vuetest(request):
    return render(request, 'buyer/vue1.html')


# 查看更多，使用 vue 实现。
# 版本一：页面渲染假数据
# def more_goods_list(request):
#     # 仅仅返回页面，数据由其他视图函数返回
#     return render(request, 'buyer/list_v1.html')

# 版本二：返回数据库数据
# def more_goods_list(request):
#     # 获取商品类型id
#     goodstype_id = request.GET.get('goodstype_id')
#     return render(request, 'buyer/list_v2.html', {'goodstype_id': goodstype_id})
#

from django.http import JsonResponse


# 接受ajax 请求
def more_goods_list_ajax(request):
    # 1.查询所有的商品
    goodstype_id = request.GET.get('goodstype_id')
    # print(goodstype_id)
    # 2.查询数据库数据
    goods_obj_list = models.Goods.objects.filter(goodstype_id=goodstype_id)
    # print(goods_obj_list)
    # 3.重新组织数据结构 [{'name':'','path','','price':''},{},{}]
    goods_dic_list = []
    for goods_obj in goods_obj_list:
        dic = {}
        dic['name'] = goods_obj.name
        dic['image'] = goods_obj.image.name
        dic['price'] = goods_obj.price

        goods_dic_list.append(dic)
    # 3.返回数据
    return JsonResponse(goods_dic_list, safe=False)  # 可以放列表


#  --------------- cbv---------------------
from django.views import View
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, 'dispatch')
class CBV(View):
    # 当get方式访问的时候，自动调用 get方法
    def get(self, request):
        print('xxx')
        return render(request, 'buyer/cbv.html')

    # 当post方式访问的时候，自动调用 post方法
    def post(self, request):
        print('post...')
        return HttpResponse('post')


# ---------------------------------drf 使用-----------------------------
from rest_framework.views import APIView
from buyer.serializers import GoodsSerializers
from rest_framework.response import Response


class GoodsAPIView(APIView):

    def get(self, request):
        # 1.获取商品类型id
        # 2.查询数据库商品
        goods_obj_list = models.Goods.objects.filter(goodstype_id=4)
        # 3.组织数据结构
        goods_serializer = GoodsSerializers(goods_obj_list, many=True)
        print(goods_serializer.data)
        # 4.返回
        return Response(goods_serializer.data)


# 使用mixins 类 进行简化操作
from rest_framework import generics
from rest_framework import mixins


class GoodsMixinsView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = GoodsSerializers

    def get_queryset(self):
        id = self.request.GET.get('goodstype_id')
        goods_obj_list = models.Goods.objects.filter(goodstype_id=id)
        return goods_obj_list

    # get 方式请求
    def get(self, request):
        return self.list(request)

    # 解决图片绝对路径问题
    def get_serializer_context(self):
        return {
            'view': self
        }


class GoodsTyBView(generics.ListAPIView):
    serializer_class = GoodsSerializers

    def get_queryset(self):
        id = self.request.GET.get('goodstype_id')
        goods_obj_list = models.Goods.objects.filter(goodstype_id=id)
        return goods_obj_list

    def get_serializer_context(self):
        return {
            'view': self
        }


from rest_framework import viewsets


# 使用viewset 方法，可以实现不同的操作
class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializers

    def get_queryset(self):
        id = self.request.GET.get('goodstype_id')
        goods_obj_list = models.Goods.objects.filter(goodstype_id=id)
        return goods_obj_list

    def get_serializer_context(self):
        return {
            'view': self
        }


def more_goods_list(request):
    # 获取商品类型id
    goodstype_id = request.GET.get('goodstype_id')
    return render(request, 'buyer/list_v3.html', {'goodstype_id': goodstype_id})


#  使用通用视图类返回数据
class GoodsAjaxView(generics.ListAPIView):
    serializer_class = GoodsSerializers

    def get_queryset(self):
        id = self.request.GET.get('goodstype_id')
        goods_obj_list = models.Goods.objects.filter(goodstype_id=id)
        return goods_obj_list

    def get_serializer_context(self):
        return {
            'view': self
        }


# 商品详情页面
def goods_details(request):
    # 1.获取商品的id
    id = request.GET.get('id')
    # 2.根据商品id 查询数据库
    goods_obj = models.Goods.objects.get(id=id)
    # 3.返回页面和数据
    return render(request, 'buyer/detail.html', {'goods_obj': goods_obj})


from buyer import models as bmodels


# 注册
def register(request):
    if request.method == 'POST':
        # 1.获取表单提交的内容
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')
        user_email = request.POST.get('user_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # 2.保存到数据库
        buyer_obj = bmodels.Buyer()
        buyer_obj.name = user_name
        buyer_obj.password = user_pwd
        buyer_obj.email = user_email
        buyer_obj.phone = phone
        buyer_obj.address = address
        buyer_obj.save()
        # 3.重定向到登录页面
        return redirect('/buyer/login/')

    return render(request, 'buyer/register.html')


# 第一版
# def login(request):
#     msg = ''
#     if request.method == 'POST':
#         # 1.获取表单提交的内容
#         user_name = request.POST.get('user_name')
#         user_pwd = request.POST.get('user_pwd')
#         # 2.查询数据库
#         buyer_obj = bmodels.Buyer.objects.filter(name=user_name, password=user_pwd).first()
#         if buyer_obj:
#             # 3. 重定向到首页
#             return redirect('/buyer/index/')
#         else:
#             msg = '用户名或者密码错误'
#     return render(request, 'buyer/login.html', {'msg': msg})

def login(request):
    msg = ''
    if request.method == 'POST':
        # 1.获取表单提交的内容
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')
        # 2.查询数据库
        buyer_obj = bmodels.Buyer.objects.filter(name=user_name, password=user_pwd).first()
        if buyer_obj:
            response = redirect('/buyer/index/')
            # 4.将用户名和用户id 保存到 cookie 用于页面显示。
            response.set_cookie('buyer_id', buyer_obj.id)
            response.set_cookie('buyer_name', buyer_obj.name)
            # 3. 重定向到首页
            return response
        else:
            msg = '用户名或者密码错误'
    return render(request, 'buyer/login.html', {'msg': msg})


# 登出操作

def logout(request):
    response = redirect('/buyer/login/')
    # 1.删除cookie中的内容
    response.delete_cookie('buyer_name')
    response.delete_cookie('buyer_id')
    # 2.重定向到登录
    return response


# 添加购物车
def add_cart(request):
    buyer_id = request.COOKIES.get('buyer_id')
    if buyer_id:  # 表示用户登录了
        # 1.获取表单提交的内容
        goods_id = request.GET.get('goods_id')
        number = request.GET.get('number')
        print(goods_id, number)
        print(type(number))
        # 2.判断当前商品是否存在购物车
        # 如果存在则修改数量，如果不存在则保存数据。
        # 根据当前用户的id 和商品的id 进行查询
        shopping_cart_obj = bmodels.ShoppingCart.objects.filter(goodsid=goods_id, buyer_id=buyer_id).first()
        if shopping_cart_obj:
            shopping_cart_obj.goodsnum += int(number)
            shopping_cart_obj.save()
        else:
            print('else....')
            # 保存数据到数据库
            goods_obj = models.Goods.objects.get(id=goods_id)
            cart_obj = bmodels.ShoppingCart()
            cart_obj.goodsid = goods_id
            cart_obj.goodsnum = int(number)
            cart_obj.goodsname = goods_obj.name
            cart_obj.goodsimg = goods_obj.image.name
            cart_obj.goodsprice = goods_obj.price
            cart_obj.storeid = goods_obj.store.id
            cart_obj.storename = goods_obj.store.name
            cart_obj.buyer_id = buyer_id
            cart_obj.save()
        dic = {'status': 'ok'}
    else:  # 用户没有登录
        dic = {'status': 'no'}

    return JsonResponse(dic)


# 我的购物车
def my_cart(request):
    # 1.获取当前用户下的购物车
    buyer_id = request.COOKIES.get('buyer_id')
    cart_obj_list = bmodels.ShoppingCart.objects.filter(buyer_id=buyer_id)
    print(cart_obj_list)
    # 2.计算每一个购物车中商品的小计价格 [{'xiaoji':84.77,'car_obj':car_obj},{}]
    car_dic_list = []
    for car_obj in cart_obj_list:
        dic = {}
        price = car_obj.goodsprice
        number = car_obj.goodsnum
        xiaoji = price * number
        print('--------->>>>')
        print(xiaoji)
        dic['xiaoji'] = xiaoji
        dic['car_obj'] = car_obj
        car_dic_list.append(dic)

    return render(request, 'buyer/cart.html', locals())


# 修改购物车中商品的数量
def change_car_num(request):
    # 1.获取购物车id
    car_id = request.GET.get('car_id')
    print(car_id)
    # 2.修改商品数量
    car_obj = bmodels.ShoppingCart.objects.get(id=car_id)
    car_obj.goodsnum += 1
    car_obj.save()
    dic = {'status': 'ok'}
    return JsonResponse(dic)


# 删除购物车
def delete_car(request):
    # 1.获取购物车id
    car_id = request.GET.get('id')
    # print(car_id)
    # 2.查询数据库并且删除
    bmodels.ShoppingCart.objects.get(id=car_id).delete()
    # 3.重定向到购物车列表页面
    return redirect('/buyer/my_cart/')


# 用户中心
def user_center_info(request):
    # 1.查询当前用户下的所有的收货地址
    buyer_id = request.COOKIES.get('buyer_id')
    address_obj_list = bmodels.UserAddress.objects.filter(buyer_id=buyer_id).order_by('-id')
    return render(request, 'buyer/user-center-info.html', {'address_obj_list': address_obj_list})


# 保存用户收货地址
def add_address(request):
    # 1.获取表单提交的内容
    shoujianren = request.POST.get('shoujianren')
    xiangxiaddress = request.POST.get('xiangxiaddress')
    youbian = request.POST.get('youbian')
    phone = request.POST.get('phone')
    # 2.获取当前用户id
    buyer_id = request.COOKIES.get('buyer_id')
    # 4.查询当前用户下的所有的地址，将状态改成False
    address_obj_list = bmodels.UserAddress.objects.filter(buyer_id=buyer_id)
    if address_obj_list:
        address_obj_list.update(status=False)

    # 3.保存数据库
    address_obj = bmodels.UserAddress()
    address_obj.name = shoujianren
    address_obj.detail = xiangxiaddress
    address_obj.youbian = youbian
    address_obj.phone = phone
    address_obj.buyer_id = buyer_id
    address_obj.status = True
    address_obj.save()
    # 4.重定向到用户中心
    return redirect('/buyer/user_center_info/')


# 改变地址选中状态
def change_address_status(request):
    buyer_id = request.COOKIES.get('buyer_id')
    # 1.获取地址id
    id = request.GET.get('id')
    print(id)
    # 2.查询数据库中的记录，并且修改状态
    # 先将当前用户下的所有地址全部改成False,然后再将选中的地址改成True
    bmodels.UserAddress.objects.filter(buyer_id=buyer_id).update(status=False)
    address_obj = bmodels.UserAddress.objects.get(id=id)
    address_obj.status = True
    address_obj.save()

    return JsonResponse({'status': 'ok'})


# 修改地址
def update_address(request):
    if request.method == 'POST':
        # 1.获取表单提交的内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        detail = request.POST.get('detail')
        youbian = request.POST.get('youbian')
        phone = request.POST.get('phone')
        # 2.查询数据库并且修改
        address_obj = bmodels.UserAddress.objects.get(id=id)
        address_obj.name = name
        address_obj.detail = detail
        address_obj.youbian = youbian
        address_obj.phone = phone
        address_obj.save()
        # 3.重定向到用户中心页面
        return redirect('/buyer/user_center_info/')
    else:
        # 1.获取地址id
        id = request.GET.get('id')
        # 2.查询数据库并且返回页面
        address_obj = bmodels.UserAddress.objects.get(id=id)
        return render(request, 'buyer/edit-address.html', {'address_obj': address_obj})


import datetime


# 订单列表和创建订单
def orders_list(request):
    # 1.获取购物车id
    shoppingcarids = request.POST.getlist('shoppingcarids')
    # print(shoppingcarids)  # ['3', '4']
    # 2.创建订单
    times = datetime.datetime.now()
    # print(times)  # 2020-10-16 10:19:28.026537
    times1 = times.strftime('%Y%m%d%H%M%S')
    # print(times)  # 20201016102058
    buyer_id = request.COOKIES.get('buyer_id')
    address_obj = bmodels.UserAddress.objects.filter(buyer_id=buyer_id, status=True).first()
    orders_obj = bmodels.Orders()
    orders_obj.orderno = times1  # 订单号
    orders_obj.orderdate = times  # 日期
    if address_obj:  # 判断地址是否存在
        orders_obj.orderaddress = address_obj.detail + ' (' + address_obj.name + ' 收) ' + address_obj.phone
    else:
        orders_obj.orderaddress = ''  # 如果用户没有收货地址则先设置成 ''

    orders_obj.ordertotalnum = ''  # 订单总价，设置为''
    orders_obj.buyer_id = buyer_id
    orders_obj.save()
    # 3.创建订单详情表
    totalnum = 0
    for car_id in shoppingcarids:
        # 根据car_id 查询 购物车对象
        car_obj = bmodels.ShoppingCart.objects.get(id=car_id)
        # 将购物车对象内容赋值给订单详情对象
        ordersdetail_obj = bmodels.OrdersDetail()
        ordersdetail_obj.goodsname = car_obj.goodsname
        ordersdetail_obj.goodsnum = car_obj.goodsnum
        ordersdetail_obj.goodsprice = car_obj.goodsprice
        ordersdetail_obj.goodsimg = car_obj.goodsimg
        xiaoji = car_obj.goodsnum * car_obj.goodsprice
        ordersdetail_obj.goodsxiaoji = xiaoji
        ordersdetail_obj.orders = orders_obj
        ordersdetail_obj.save()
        totalnum += xiaoji
        # 删除购物车信息
        car_obj.delete()

    # 4.计算商品总价格，重新修改订单
    orders_obj.ordertotalnum = totalnum
    orders_obj.save()
    # 4.返回页面
    return render(request, 'buyer/place_order.html', {'orders_obj': orders_obj, 'address_obj': address_obj})


# 立即购买
def now_buy(request):
    # 1. 获取商品的id 和数量
    goodsid = request.GET.get('goodsid')
    number = request.GET.get('number')
    print(goodsid, number)
    # 2.创建订单

    times = datetime.datetime.now()
    times1 = times.strftime('%Y%m%d%H%M%S')
    buyer_id = request.COOKIES.get('buyer_id')
    address_obj = bmodels.UserAddress.objects.filter(buyer_id=buyer_id, status=True).first()
    orders_obj = bmodels.Orders()
    orders_obj.orderno = times1  # 订单号
    orders_obj.orderdate = times  # 日期
    if address_obj:  # 判断地址是否存在
        orders_obj.orderaddress = address_obj.detail + ' (' + address_obj.name + ' 收) ' + address_obj.phone
    else:
        orders_obj.orderaddress = ''  # 如果用户没有收货地址则先设置成 ''

    orders_obj.ordertotalnum = ''  # 订单总价，设置为''
    orders_obj.buyer_id = buyer_id
    orders_obj.save()

    # 3.创建订单详情
    goods_obj = models.Goods.objects.get(id=goodsid)
    ordersdetail_obj = bmodels.OrdersDetail()
    ordersdetail_obj.goodsname = goods_obj.name
    ordersdetail_obj.goodsnum = number
    ordersdetail_obj.goodsprice = goods_obj.price
    ordersdetail_obj.goodsimg = goods_obj.image.name
    xiaoji = goods_obj.price * int(number)
    ordersdetail_obj.goodsxiaoji = xiaoji
    ordersdetail_obj.orders = orders_obj
    ordersdetail_obj.save()

    # 4.计算商品总价格，重新修改订单
    orders_obj.ordertotalnum = xiaoji
    orders_obj.save()

    # 5.返回页面
    return render(request, 'buyer/place_order.html', {'orders_obj': orders_obj, 'address_obj': address_obj})


# 我的订单
# 访问我的订单--》》 两种情况
# 第一种，用户开始生成订单的时候已经选了地址。
# 第二种，用户开始生成订单的时候没有选地址。

def my_orders(request):
    # 1.将当前用户下的订单查询出来渲染到页面上
    buyer_id = request.COOKIES.get('buyer_id')
    orders_obj_list = bmodels.Orders.objects.filter(buyer_id=buyer_id)
    for orders_obj in orders_obj_list:
        if orders_obj.orderaddress == '':  # 没有地址
            # 2.将地址设置到订单上
            address_obj = bmodels.UserAddress.objects.filter(buyer_id=buyer_id, status=True).first()
            orders_obj.orderaddress = address_obj.detail + ' (' + address_obj.name + " 收) " + address_obj.phone
            orders_obj.save()
    return render(request, 'buyer/myorders.html', {'orders_obj_list': orders_obj_list})


# 支付宝测试
from alipay import AliPay


def zfbtest(request):
    # 私钥
    app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
    MIIEogIBAAKCAQEAgJJQqYjAqAMP5yNS7TUi9aat0ajw6ZOMvCoT73EqibQWU79X+7nSYncG1wlYha89q3xMJtG09ajQyllEJHIYuh4AQ6cAoc3f0jbEQh1kHjC3SphI6Hx89bSwiKhrQXArl6vbb/lfKkszrzwU84fB/ixmimDVAQh91/mgWTbg2q1l4788y40bgAm3cgVVFL4B5LV/mFSN2NZ3gRyFLyI+aa2LFcEBdysZrOmv86nbkwFV3KdFsN6ZwQB4JIaX9kirLTbfBJ1199a1Bsy488sCms0d/HXKT3PqkvS94+S5bImeaU7o3D51T/CL+Ty1zPPBUf+6seu6BIWMKasscG/vZwIDAQABAoIBABT6Soju1ChVn5Gh9NTZN6QHFxM/Uld6CJtm7ivCNiOTq5TsgmmDDy2bqBUL5FKjnhdNx4sJ6lGuwqpRWEnuB9TOMlLXe8XqtlsxLmJvMzet0SotoK+2KBla6vbRK/bYW3R6yOoDMSDQdlVgIzb87o0PJ4fqdradcRL9GsmTp6pmJyBG0y5mhFkiOZq0ESRHYVKp8YD8WhB9wjMdBxyliC+FsFbeh1zTsoExCcXwuaMbTG+3Tco28fflgkugOn7IVkTZ0Ym8oz1/5vz8N/trfd5cRwo1EOQ8Dnr+pLJzTmodIsn7RxF/5NlwEuk+QmTK7/lb8Lro9x8YYhXOkLEfHFkCgYEAutU9ADCDT9cb1wPm2yP13djcvUGVVOmkKEowqTFsXO/CQ3YRwLc47QzdyK+b6EDpqGTfuY/OH712jV2ayAnDPwvw6rxQcPH/rvuhcbKNafsN53GwrqSTWkCYvj+yy8RMFDeXoRx4euOYkFO6zW+LzKVgd6uzT5SfdwbIae9J1JMCgYEAsCt0Vw4Ou79fPjt3zbOTjVx5KLxbB08DIRuA6PNspksFmBmF4KR7/n5lg9b95XBhF2HO1lVhrgRpwod3GPGBQWQXF7OfqgUqiq3La3ZOZVJ8dMz86XTLxBSpJL9eLKK4hsqyWOVoyrmaUJrr5xhBwG2cmiw4zE5YcaOsFz0jMl0CgYAd5jI07Y6WIF6cMkunlkGqlyH8R5qWVC2pJPZUnUwyM0xrb2G37Zp2lTCJBVF2Aa1i/YGwOItMGQ334Zr7mFReqpKLfkeBS7kXT72ubFylMUAwYclcqYnLT7sh9x+t7GQgeCUT63J8eB/aOQwUBF3jCjQ98oRnn+lFKxi3m0u9cQKBgDlTiqIhcu3pUkbf9xY6z1L6unplAIIaVfxaBNLJE5vxYbqi44u8OpUP8Fy8gxY8QXvoWfQpCIYl7XxdtIWrYNI0jccqrlQXJkbGUyF+9/fEpbckVVBqrzv5NSk+FJkVwlIqd2qyDC2bw/li0Ez8+bhycrlAlqL1A5bHGeLeBCwJAoGAPiXEpoO/oqLH1fjETRl9r+rExUf+9MdRGhmM5ku6WbWEgEj0Fflv8vqKCXkgnFBeo9j0JRxFg8OubMKgP1/rg8JNFS1EArjuu2LTnKYR2E+P5egu7bUvdXxzyXeaf4j7ehgeuNNtdlvqOmuhF3Yg3Hybkz1fv3ZUVIeKy5eWS1c=
    -----END RSA PRIVATE KEY-----"""
    # 公钥
    alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAubtn6v/fRxicLhOdTijJ0xqXLZflHjvq31Y13NId7Xjs5w7vHiddCrml0k69iD0COo/1Ke8AJLVajwh9Zj/ZtAjjRjiK9cRW4SgTRlTm3Bnbqm5aZucmunOwgJfeCohgLTkFIwOOPbSb93u+nwvMTWAayiblm3aHGmZuBxb0EsUP5IBg1XCs26Am5gV8nWZ87cxDrF1C36i94kbDpmhFubicEIw+NMRuyKmWObrTZmxugv2AcM4lgM1LVz+Qa4H1mj0KQl4CjRHMlImSrznsvWq+5HUbIxMA7VUStA+mpJHFG4azb1jWOlatK984vXXgfLqRSH/gu2lkRA9gEGc36wIDAQAB
    -----END PUBLIC KEY-----"""

    alipay = AliPay(
        appid="2016092800613099",  # 自己的appid
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,  # 自己app的私钥
        alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认False
    )
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="2016111211",
        total_amount=str(1),
        subject='测试的天天生鲜',
        return_url=None,
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(url)


def zfb(request):
    orderno = request.GET.get('orderno')
    total = request.GET.get('total')

    # 私钥
    app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
        MIIEogIBAAKCAQEAgJJQqYjAqAMP5yNS7TUi9aat0ajw6ZOMvCoT73EqibQWU79X+7nSYncG1wlYha89q3xMJtG09ajQyllEJHIYuh4AQ6cAoc3f0jbEQh1kHjC3SphI6Hx89bSwiKhrQXArl6vbb/lfKkszrzwU84fB/ixmimDVAQh91/mgWTbg2q1l4788y40bgAm3cgVVFL4B5LV/mFSN2NZ3gRyFLyI+aa2LFcEBdysZrOmv86nbkwFV3KdFsN6ZwQB4JIaX9kirLTbfBJ1199a1Bsy488sCms0d/HXKT3PqkvS94+S5bImeaU7o3D51T/CL+Ty1zPPBUf+6seu6BIWMKasscG/vZwIDAQABAoIBABT6Soju1ChVn5Gh9NTZN6QHFxM/Uld6CJtm7ivCNiOTq5TsgmmDDy2bqBUL5FKjnhdNx4sJ6lGuwqpRWEnuB9TOMlLXe8XqtlsxLmJvMzet0SotoK+2KBla6vbRK/bYW3R6yOoDMSDQdlVgIzb87o0PJ4fqdradcRL9GsmTp6pmJyBG0y5mhFkiOZq0ESRHYVKp8YD8WhB9wjMdBxyliC+FsFbeh1zTsoExCcXwuaMbTG+3Tco28fflgkugOn7IVkTZ0Ym8oz1/5vz8N/trfd5cRwo1EOQ8Dnr+pLJzTmodIsn7RxF/5NlwEuk+QmTK7/lb8Lro9x8YYhXOkLEfHFkCgYEAutU9ADCDT9cb1wPm2yP13djcvUGVVOmkKEowqTFsXO/CQ3YRwLc47QzdyK+b6EDpqGTfuY/OH712jV2ayAnDPwvw6rxQcPH/rvuhcbKNafsN53GwrqSTWkCYvj+yy8RMFDeXoRx4euOYkFO6zW+LzKVgd6uzT5SfdwbIae9J1JMCgYEAsCt0Vw4Ou79fPjt3zbOTjVx5KLxbB08DIRuA6PNspksFmBmF4KR7/n5lg9b95XBhF2HO1lVhrgRpwod3GPGBQWQXF7OfqgUqiq3La3ZOZVJ8dMz86XTLxBSpJL9eLKK4hsqyWOVoyrmaUJrr5xhBwG2cmiw4zE5YcaOsFz0jMl0CgYAd5jI07Y6WIF6cMkunlkGqlyH8R5qWVC2pJPZUnUwyM0xrb2G37Zp2lTCJBVF2Aa1i/YGwOItMGQ334Zr7mFReqpKLfkeBS7kXT72ubFylMUAwYclcqYnLT7sh9x+t7GQgeCUT63J8eB/aOQwUBF3jCjQ98oRnn+lFKxi3m0u9cQKBgDlTiqIhcu3pUkbf9xY6z1L6unplAIIaVfxaBNLJE5vxYbqi44u8OpUP8Fy8gxY8QXvoWfQpCIYl7XxdtIWrYNI0jccqrlQXJkbGUyF+9/fEpbckVVBqrzv5NSk+FJkVwlIqd2qyDC2bw/li0Ez8+bhycrlAlqL1A5bHGeLeBCwJAoGAPiXEpoO/oqLH1fjETRl9r+rExUf+9MdRGhmM5ku6WbWEgEj0Fflv8vqKCXkgnFBeo9j0JRxFg8OubMKgP1/rg8JNFS1EArjuu2LTnKYR2E+P5egu7bUvdXxzyXeaf4j7ehgeuNNtdlvqOmuhF3Yg3Hybkz1fv3ZUVIeKy5eWS1c=
        -----END RSA PRIVATE KEY-----"""
    # 公钥
    alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAubtn6v/fRxicLhOdTijJ0xqXLZflHjvq31Y13NId7Xjs5w7vHiddCrml0k69iD0COo/1Ke8AJLVajwh9Zj/ZtAjjRjiK9cRW4SgTRlTm3Bnbqm5aZucmunOwgJfeCohgLTkFIwOOPbSb93u+nwvMTWAayiblm3aHGmZuBxb0EsUP5IBg1XCs26Am5gV8nWZ87cxDrF1C36i94kbDpmhFubicEIw+NMRuyKmWObrTZmxugv2AcM4lgM1LVz+Qa4H1mj0KQl4CjRHMlImSrznsvWq+5HUbIxMA7VUStA+mpJHFG4azb1jWOlatK984vXXgfLqRSH/gu2lkRA9gEGc36wIDAQAB
        -----END PUBLIC KEY-----"""

    alipay = AliPay(
        appid="2016092800613099",  # 自己的appid
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,  # 自己app的私钥
        alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认False
    )
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=orderno,
        total_amount=total,
        subject='测试的天天生鲜',
        return_url='http://127.0.0.1:8000/buyer/update_orders_status/?orderno=' + orderno,
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(url)


def update_orders_status(request):
    orderno = request.GET.get('orderno')
    print(orderno)
    bmodels.Orders.objects.filter(orderno=orderno).update(status=True)
    return HttpResponse('订单状态修改成功了...')


# -------------------- session使用---------------

def set_session(request):
    request.session['name'] = 'zs'
    request.session['age'] = '18'

    return HttpResponse('set session')


def get_session(request):
    name = request.session['name']
    age = request.session['age']
    print(name, age)
    return HttpResponse('get session')


def delete_session(request):
    # del request.session['name']
    request.session.clear()  # 删除所有的键值对
    return HttpResponse('delete session')


def testfunc(request):
    name = bmodels.Buyer.objects.get_buyer_name(2)
    print(name)
    buyer_obj = bmodels.Buyer.objects.get(id=2)
    print(buyer_obj)
    return HttpResponse('XXX')


def testmiddlevare(request):
    print('view...')
    # print(id(testmiddlevare))
    response = HttpResponse('测试中间件')
    num = 1 / 0
    #
    # def test():
    #     return HttpResponse('xx')
    #
    # response.render = test

    return response


from django.core.mail import EmailMultiAlternatives


def email_test(request):
    email = EmailMultiAlternatives(
        subject='冬天来了',
        body='冬天来了，春天也就不远了.',
        from_email='python_liurui@163.com',
        to=['1337765076@qq.com']
    )
    email.send()

    return HttpResponse('发送成功了...')


import random


# 生成验证码
def get_yzm():
    return random.randint(1000, 9999)


def register_email_ajax(request):
    dic_msg = {'status': 'success', 'data': ''}
    # 1.获取邮箱
    email_name = request.GET.get('email')
    # print(email)
    # 2.生成验证码
    yzm = get_yzm()
    # 3.发送邮件
    try:
        email = EmailMultiAlternatives(
            subject='ddsx验证码',
            body=str(yzm),
            from_email='python_liurui@163.com',
            to=[email_name]
        )
        email.send()
    except:
        # 说明邮件发送失败了.返回错误信息，前端根据错误信息进行判断
        dic_msg['data'] = '邮箱不正确!'
        dic_msg['status'] = 'error'
        print('错误L ....')
    else:
        # 邮箱发送成功了，则执行else。
        # 将验证码、邮箱、时间保存到数据库，用于邮箱注册时的校验。
        checkemail_obj = bmodels.CheckEmail()
        checkemail_obj.emailname = email_name
        checkemail_obj.authcode = yzm
        checkemail_obj.etime = datetime.datetime.now()  # 当前时间
        checkemail_obj.save()
    finally:
        return JsonResponse(dic_msg)


# 邮箱注册
def register_email(request):
    dic = {'email_name_error': '', 'code_error': '', 'code_time_out': ''}
    if request.method == 'POST':
        # 1.获取表单提交的内容
        emailname = request.POST.get('emailname')
        code = request.POST.get('code')
        userpass = request.POST.get('userpass')
        # 2.校验
        # (1).校验邮箱名称
        checkemail_obj = bmodels.CheckEmail.objects.filter(emailname=emailname).first()
        if checkemail_obj:
            # (2).验证码是否正确
            pass
            authcode = checkemail_obj.authcode
            if authcode == code:
                # 验证码正确
                # print('验证码正确')
                # (3).时间是否有效
                # 获取当前时间和数据库保存的时间进行比较。
                starttime = checkemail_obj.etime  # 数据库保存的时间
                endtime = datetime.datetime.now()
                zztime = endtime - starttime
                if zztime.seconds < 120:  # 没有失效
                    # 3.保存
                    buyer_obj = bmodels.Buyer()
                    buyer_obj.name = emailname
                    buyer_obj.password = userpass
                    buyer_obj.save()
                    # 删除数据库中的校验信息
                    checkemail_obj.delete()
                    # 4.重定向到登录页面
                    return redirect('/buyer/login/')
                else:
                    # 失效...
                    dic['code_time_out'] = '验证码失效了'
                    checkemail_obj.delete()
            else:
                # 验证码输入错误
                dic['code_error'] = '验证码输入有误'
        else:
            dic['email_name_error'] = '获取验证码邮箱和当前邮箱不一致'

    return render(request, 'buyer/register_email.html', {'dic': dic})


from django.views.decorators.cache import cache_page

import time


# @cache_page(10)  # 单位s
# def cache_test(request):
#     ctime = time.time()
#     return render(request, 'buyer/cache_teest.html', {'ctime': ctime})


def cache_test(request):
    ctime = time.time()
    dtime = time.time()
    return render(request, 'buyer/cache_teest.html', {'ctime': ctime, 'dtime': dtime})


# 设置缓存
from django.core.cache import cache


def set_cache(request):
    name = cache.get('name')
    print(name)
    if name:
        print('1111')
        return render(request, 'buyer/cache_teest.html', locals())
    else:
        print('2222')
        name = 'zs'
        cache.set('name', name, 15)
        return render(request, 'buyer/cache_teest.html', locals())


def update_cache(request):
    name = cache.get('name')
    if name:
        cache.delete('name')
    name = 'lis'
    cache.set('name', name, 15)
    return render(request, 'buyer/cache_teest.html', locals())
