from django.urls import path, include
from buyer import views

urlpatterns = [
    path('index/', views.index),  # 首页
    path('more_goods_list/', views.more_goods_list),  # 查看更多
    path('goodsajaxview/', views.GoodsAjaxView.as_view()),  # 查看更多ajax
    path('goods_details/', views.goods_details),  # 商品详情
    path('register/', views.register),  # 注册
    path('login/', views.login),  # 登录
    path('logout/', views.logout),  # 登出
    path('add_cart/', views.add_cart),  # 添加购物车
    path('my_cart/', views.my_cart),  # 我的购物车
    path('change_car_num/', views.change_car_num),  # 修改购物车中的数量
    path('delete_car/', views.delete_car),  # 删除购物车
    path('user_center_info/', views.user_center_info),  # 用户中心
    path('orders_list/', views.orders_list),  # 订单列表
    path('add_address/', views.add_address),  # 添加地址
    path('change_address_status/', views.change_address_status),  # 改变地址选中状态
    path('update_address/', views.update_address),  # 修改地址
    path('now_buy/', views.now_buy),  # 立即购买
    path('my_orders/', views.my_orders),  # 我的订单
    path('zfb/', views.zfb),  # 支付宝
    path('update_orders_status/', views.update_orders_status),  # 修改订单状态
    path('register_email/', views.register_email),  # 邮箱注册
    path('register_email_ajax/', views.register_email_ajax),  # 邮箱注册,接受ajax请求

]
# 与项目无关的内容
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('router', views.GoodsViewSet, basename='')

from django.views.decorators.cache import cache_page

urlpatterns += [
    path('more_goods_list_v1/', views.more_goods_list_v1),  # 查看更多，传统方式返回
    path('more_goods_list_ajax/', views.more_goods_list_ajax),  # 查看更多ajax
    path('vuetest/', views.vuetest),  # vue使用
    path('cbv/', views.CBV.as_view()),  # cbv
    path('goodsapiview/', views.GoodsAPIView.as_view()),  # APIView
    path('goodsmixinsview/', views.GoodsMixinsView.as_view()),  # APIView
    path('goodstyview/', views.GoodsTyBView.as_view()),  # 通用视图类
    path('goodsviewset/', views.GoodsViewSet.as_view({'get': 'list'})),  # 使用viewset
    path('', include(router.urls)),  # 使用viewset
    path('zfbtest/', views.zfbtest),  # 测试支付宝
    path('set_session/', views.set_session),  # 设置session
    path('get_session/', views.get_session),  # 获取session
    path('delete_session/', views.delete_session),  # 删除session
    path('testfunc/', views.testfunc),  # 自定义方法
    path('testmiddlevare/', views.testmiddlevare),  # 测试中间件
    path('email_test/', views.email_test),  # 测试django发送邮件
    # path('cache_test/', views.cache_test),  # 缓存测试
    # path('cache_test/', cache_page(10)(views.cache_test)),  # 缓存测试
    path('cache_test/', views.cache_test),  # 缓存测试
    path('set_cache/', views.set_cache),  # 设置缓存
    path('update_cache/', views.update_cache),  # 更新缓存

]
