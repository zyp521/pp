from django.shortcuts import render, HttpResponse, redirect
from seller import models


# def index(request):
#     seller_name = request.COOKIES.get('seller_name')
#     if seller_name:
#         return render(request, 'seller/index.html')
#     else:
#         return redirect('/seller/login/')

# def check_login(func):
#     def inner(request):
#         seller_name = request.COOKIES.get('seller_name')
#         if seller_name:
#             return func(request)
#         else:
#             return redirect('/seller/login/')
#
#     return inner


# @check_login
def index(request):
    return render(request, 'seller/index.html')


# def login(request):
#     msg = ''
#     if request.method == 'POST':
#         # 1.获取表单提交的内容
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 2.查询数据库进行比较
#         seller_obj = models.Seller.objects.filter(username=username, password=password).first()
#         if seller_obj:  # 正确
#             # 重定向到首页
#             return redirect('/seller/index/')
#         else:
#             msg = '用户名或者密码错误'
#
#     return render(request, 'seller/login.html', {'msg': msg})

# 设置cookie
def login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        seller_obj = models.Seller.objects.filter(username=username, password=password).first()
        if seller_obj:
            response = redirect('/seller/index/')
            # 设置cookie
            response.set_cookie('seller_name', seller_obj.username)
            response.set_cookie('seller_id', seller_obj.id)
            # 注意seller_obj.headimg 获取的是一个对象而不是字符串路径。
            # print(seller_obj.headimg, type(seller_obj.headimg))
            # print(seller_obj.headimg.name, type(seller_obj.headimg.name))
            response.set_cookie('seller_headimg', seller_obj.headimg.name)

            return response
        else:
            msg = '用户名或者密码错误'

    return render(request, 'seller/login.html', {'msg': msg})


# def register(request):
#     if request.method == 'POST':
#         # 1.获取表单提交的内容
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         gender = request.POST.get('gender')
#         headimg = request.FILES.get('headimg')  # 注意使用的是 FILES
#         # print(headimg, type(headimg))
#         # 2.保存到数据库
#         seller_obj = models.Seller()
#         seller_obj.username = username
#         seller_obj.password = password
#         seller_obj.email = email
#         seller_obj.phone = phone
#         seller_obj.address = address
#         seller_obj.gender = gender
#         seller_obj.headimg = headimg
#         seller_obj.save()
#
#         # 3.重定向到登录页面
#         return redirect('/seller/login/')
#
#     return render(request, 'seller/register.html')
from seller.form import SellerForm


# 使用form表单
def register(request):
    sellerform = SellerForm()
    if request.method == 'POST':
        # 使用form 进行校验
        sellerform = SellerForm(request.POST, request.FILES)
        if sellerform.is_valid():  # 如果返回True 说明符合校验规则
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            headimg = request.FILES.get('headimg')
            seller_obj = models.Seller()
            seller_obj.username = username
            seller_obj.password = password
            seller_obj.email = email
            seller_obj.phone = phone
            seller_obj.address = address
            seller_obj.gender = gender
            seller_obj.headimg = headimg
            seller_obj.save()
            return redirect('/seller/login/')

    return render(request, 'seller/register.html', {'sellerform': sellerform})


# 登出
# @check_login
def logout(request):
    response = redirect('/seller/login/')
    # 1. 删除cookie
    response.delete_cookie('seller_name')
    response.delete_cookie('seller_headimg')
    response.delete_cookie('seller_id')
    # 2.重定向到登录页面
    return response


# -----------------------------------店铺设置-----------------------
import os


# 当用户注册完查看店铺时，会进行第一次保存。
# 之后的每一次查看，都是修改，
# @check_login
def store(request):
    if request.method == 'POST':
        store_id = request.POST.get('id')
        print('--->>>', store_id)
        if store_id:  # 进行修改
            # 1.获取表单提交的内容
            shopname = request.POST.get('shopname')
            shopaddress = request.POST.get('shopaddress')
            shopdesc = request.POST.get('shopdesc')
            shopimg = request.FILES.get('shopimg')

            # 2.查询数据库并且修改
            store_obj = models.Store.objects.get(id=store_id)
            if shopimg:  # 如果修改图片则进行赋值
                # 先删除以前的图片，然后再重新赋值新的图片
                path = 'static/' + store_obj.logo.name  # img/1.jpg
                os.remove(path)
                # 重新赋值
                store_obj.logo = shopimg

            store_obj.name = shopname
            store_obj.address = shopaddress
            store_obj.desc = shopdesc
            store_obj.save()
            # 3.重定向首页
            return redirect('/seller/index/')
        else:
            # 1.获取表单提交的内容
            shopname = request.POST.get('shopname')
            shopaddress = request.POST.get('shopaddress')
            shopdesc = request.POST.get('shopdesc')
            shopimg = request.FILES.get('shopimg')

            # 2.保存到数据库
            store_obj = models.Store()
            store_obj.name = shopname
            store_obj.address = shopaddress
            store_obj.desc = shopdesc
            store_obj.logo = shopimg
            seller_id = request.COOKIES.get('seller_id')
            seller_obj = models.Seller.objects.get(id=seller_id)
            store_obj.seller = seller_obj
            store_obj.save()
            # 3.重定向到首页
            return redirect('/seller/index/')

    else:
        # get 请求
        # 1.获取用户id
        seller_id = request.COOKIES.get('seller_id')
        # 2.查询当前用户的店铺
        seller_obj = models.Seller.objects.get(id=seller_id)
        try:
            store_obj = seller_obj.store
        except:
            pass
        # 3.返回页面
        return render(request, 'seller/store.html', locals())


# -------------------------商品类型-----------------------------


def goodstype_list(request):
    # 查询所有的商品类型
    goodstype_obj_list = models.GoodsType.objects.all()
    return render(request, 'seller/goods_type_list.html', {'goodstype_obj_list': goodstype_obj_list})


def add_goodstype(request):
    # 1.获取表单提交的内容
    goodstype_name = request.POST.get('goodstype_name')
    goodstype_img = request.FILES.get('goodstype_img')
    # 2.保存数据库
    goodstype_obj = models.GoodsType()
    goodstype_obj.name = goodstype_name
    goodstype_obj.logo = goodstype_img
    goodstype_obj.save()
    # 3.重定向到商品类型列表
    return redirect('/seller/goodstype_list/')


def edit_goodstype(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        goodstype_obj = models.GoodsType.objects.get(id=id)
        return render(request, 'seller/edit_goodstype.html', {'goodstype_obj': goodstype_obj})
    else:
        # post 请求
        # 1.获取表单提交的内容
        goodstypename = request.POST.get('goodstypename')
        goodstypeimg = request.FILES.get('goodstypeimg')
        id = request.POST.get('id')
        # 2.查询数据库并且修改
        goodstype_obj = models.GoodsType.objects.get(id=id)
        goodstype_obj.name = goodstypename
        goodstype_obj.logo = goodstypeimg
        goodstype_obj.save()
        # 3.重定向到商品类型列表
        return redirect('/seller/goodstype_list/')


def delete_goodstype(request):
    # 1.获取商品类型id
    id = request.GET.get('id')
    # 2.查询数据库并且删除
    goodstype_obj = models.GoodsType.objects.get(id=id)
    # 删除图片
    path = 'static/' + goodstype_obj.logo.name
    os.remove(path)
    # 删除数据
    goodstype_obj.delete()
    # 3.重定向到商品类型列表
    return redirect('/seller/goodstype_list/')


def goods_list(request):
    # 查询出当前店铺下所有的商品。
    seller_id = request.COOKIES.get('seller_id')
    store_obj = models.Store.objects.get(seller_id=seller_id)
    goods_obj_list = models.Goods.objects.filter(store_id=store_obj.id)
    return render(request, 'seller/goods_list.html', {'goods_obj_list': goods_obj_list})


def add_goods(request):
    if request.method == 'POST':
        # 1.获取表单提交的内容
        name = request.POST.get('name')
        price = request.POST.get('price')
        bzq = request.POST.get('bzq')
        productdate = request.POST.get('productdate')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        goodstype_id = request.POST.get('goodstype_id')
        goodsimg = request.FILES.get('goodsimg')
        # 2.创建对象保存到数据库
        goods_obj = models.Goods()
        goods_obj.name = name
        goods_obj.price = price
        goods_obj.bzq = bzq
        goods_obj.scrq = productdate
        goods_obj.desc = desc
        goods_obj.content = content
        goods_obj.image = goodsimg
        goods_obj.goodstype_id = goodstype_id
        seller_id = request.COOKIES.get('seller_id')
        store_obj = models.Store.objects.get(seller_id=seller_id)
        goods_obj.store = store_obj
        goods_obj.save()
        # 3.重定向到商品列表
        return redirect('/seller/goods_list/')
    else:
        pass
        # get 方式
        # 1. 获取所有的商品类型
        goodstype_obj_list = models.GoodsType.objects.all()
        # 2. 返回页面
        return render(request, 'seller/add_goods.html', {'goodstype_obj_list': goodstype_obj_list})
