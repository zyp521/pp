from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

# 定义白名单
white_list = [
    '/seller/login/',
    '/seller/register/',
    '/'  # 放行首页
]


class AuthMD(MiddlewareMixin):

    def process_request(self, request):
        path = request.path_info
        print(path)
        # 1.前台的路径都放行
        if path.find('/buyer/') != -1:  # 路径中有buyer,放行
            print('前台路径放行...')
            return None

        # 2.白名单中的url 进行放行
        if path in white_list:
            print('白名单放行...')
            return None

        # 3. 判断是否登录，如果登录了则放行
        seller_id = request.COOKIES.get('seller_id')
        if seller_id:
            print('登录放行...')
            return None
        return redirect('/seller/login/')
