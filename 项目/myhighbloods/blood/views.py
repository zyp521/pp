from django.shortcuts import render
from rest_framework.views import APIView,Response
from .serializers import MyBloodSerializer
# Create your views here.
#实现类视图，类视图继承APIView
class BloodView(APIView):
    def get(self,request):
        #逻辑：地址上直接反映地址，把网页返回到浏览器的响应中。
        return render(request,"user.html")
    def post(self,request):
        myblood=MyBloodSerializer(data=request.data)
        print(myblood)
        if myblood.is_valid():
            myblood.save()
            #接口的体现：后台一定返回前台数据
            return Response(myblood.data)
        else:
            return Response({"result":"数据提交错误，没有被保存"})
#注意，实现数据分析结果接口通过函数实现，没有类视图
def showinfo(request):
    #把原来高血压数据分析中的步骤语句复制过来
    import pandas
    datas = pandas.read_csv("static/psm.csv")
    # 求出总人数
    all = datas["Hypertension"].count()
    #求出高血压患病人数
    ill = datas[datas["Hypertension"] == 1.0]["Hypertension"].count()
    # 高血压患病率=高血压患病人数/总人数
    rate = ill / all
    rate = round(rate, 2)
    #在总的1的大范围内减去患病率的数字就是未患病率的数字
    unrate = round(1 - rate, 2)
    #导入pyecharts进行画图
    from pyecharts.charts import Pie
    x = ["高血压患病率", "高血压未患病率"]
    y = [rate, unrate]
    pie = (
        Pie()
            .add("高血压患病率分析", [list(z) for z in zip(x, y)])
    )
    #原来做分析时用render方法渲染一个网页
    #render_embed把网页代码渲染到一个变量中
    page=pie.render_embed()
    #Django中把变量传到前台，需要设置一个字典
    content={"page":page}
    return render(request,"info.html",content)




