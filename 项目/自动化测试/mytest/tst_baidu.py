from selenium import webdriver
import unittest
from utils.HTMLTestRunner_Chart import HTMLTestRunner
import time
class 百度测试(unittest.TestCase):
    #def __init__(self):
        #pass
    #启动测试用例的方法
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        #setUp是每个用例执行一次，imgs不断初始化
        self.imgs=[]
    def 验证百度输入框的有效性(self):
        so=self.driver.find_element_by_id("kw")
        #测试的用例一定要断言
        self.assertTrue(so.is_enabled(),True)
        self.imgs.append(self.driver.get_screenshot_as_base64())
    def 验证百度输入中公教育的搜索结果(self):
        so=self.driver.find_element_by_id("kw")
        so.send_keys("中公教育")
        #在输入中公教育后，得到具体结果的过程中，是有一定的过程等待。
        #用time.sleep()方法来进行一个过程上的等待，等待网络上有具体搜索结果的显示。
        self.driver.find_element_by_id("su").click()
        #点击结果后进行时间上的等待。
        time.sleep(10)
        self.imgs.append(self.driver.get_screenshot_as_base64())
        #任何的测试用例都要下断言
        self.assertEqual(so.get_attribute("value"),"中公")
    #关闭测试用例的方法
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    #TextTestRunner永远都在控制台上跑，不能够产生报告
    #如果要产生报告需要用测试套件TestSuite
    #测试套件TestSuite中可以添加很多个测试用例
    suite=unittest.TestSuite()
    #addTest表示在测试套件中添加测试用例
    suite.addTest(百度测试("验证百度输入框的有效性"))
    suite.addTest(百度测试("验证百度输入中公教育的搜索结果"))
    #runner=unittest.TextTestRunner()
    #runner.run(BaiduTest("test_input"))
    #调用html_testrunner形成测试报告的模块
    #输出网页文件,输出文件要求写字节
    with open("result1.html","wb") as f:
        runner=HTMLTestRunner(f,verbosity=2,title="百度网站测试报告",description="百度功能的相关测试")
        runner.run(suite)