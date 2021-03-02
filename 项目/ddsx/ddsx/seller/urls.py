from django.urls import path
from seller import views

urlpatterns = [
    path('register/', views.register),  # 注册
    path('login/', views.login),  # 登录
    path('index/', views.index),  # 首页
    path('logout/', views.logout),  # 登出
    path('store/', views.store),  # 店铺
    path('goodstype_list/', views.goodstype_list),  # 商品类型列表
    path('add_goodstype/', views.add_goodstype),  # 添加商品类型
    path('edit_goodstype/', views.edit_goodstype),  # 修改商品类型
    path('delete_goodstype/', views.delete_goodstype),  # 删除商品类型
    path('goods_list/', views.goods_list),  # 商品列表
    path('add_goods/', views.add_goods),  # 添加商品
]
