# 编写自己的中间件
# 1.导入
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


# 2.继承
class MD1(MiddlewareMixin):

    def process_request(self, request):
        """
        在视图函数之前执行
        :param request:
        :return: 如果返回响应对象则不再执行视图函数。
        不写返回值和 返回None 表示不拦截 （放行），
        """
        print('process request')
        # return HttpResponse('拦截L..')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        在 process_request 之后，在 视图函数之前执行。

        :param request:
        :param view_func: 表示视图函数的内存地址
        :param view_args: 接受视图函数位置参数
        :param view_kwargs:接受视图函数的关键字参数
        :return: 如果返回响应对象则不再执行视图函数。
        不写返回值和 返回None 表示不拦截 （放行）。
        """
        print('process view...')
        # print(id(view_func))
        # return HttpResponse('process_view')

    def process_template_response(self, request, response):
        """
        响应对象中必须包含 render 方法。
        在视图函数之后执行。
        :param reqeust:
        :param response:
        :return: 必须要有返回值
        """
        print('process_template_response')

        return response

    def process_response(self, request, response):
        """
        在视图函数之后执行。
        :param request:
        :param response:
        :return: 必须要有返回值
        """
        print('process_response')
        return response

    def process_exception(self, request, exception):
        """
        在视图函数抛出异常之后执行
        :param request:
        :param execption:
        :return:
        """
        print('process_exception')
        print(exception)
        return HttpResponse('您操作有误，请仔细操作!!!')
