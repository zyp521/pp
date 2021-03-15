#下面是一个简易的面向对象的加法程序
#这种方法实现的简易加法是对小数是有问题的.
#对小数部分的加法做一个处理,按照四舍五入的方法保留两位小数
class TestMath:
    def add(self,a,b):
        #这种直接return a+b是一种不科学的加法,不能计算小数的加法
        #return a+b
        return round(a+b,2)
import unittest
#做一个加法测试的用例
class MyTest(unittest.TestCase):
    def setUp(self):
        print("测试用例的启动")
    def five_plus_two_equal_seven(self):
        test=TestMath()
        #在写测试用例的时候,必须要写断言
        self.assertEqual(test.add(5,2),7)
    def zero_dot_one_plus(self):
        test=TestMath()
        #再次写断言，断言0.1+0.2=0.3
        self.assertEqual(test.add(0.1,0.2),0.3)
    def fu_zhi_plus(self):
        test=TestMath()
        self.assertEqual(test.add(-0.2,0.3),0.1)
    def tearDown(self):
        print("测试用例的关闭")
if __name__=="__main__":
    #TextTestRunner就是测试的执行类
    runner=unittest.TextTestRunner()
    runner.run(MyTest("five_plus_two_equal_seven"))
    runner.run(MyTest("zero_dot_one_plus"))
    runner.run(MyTest("fu_zhi_plus"))