import unittest


class Test(unittest.TestCase):
    # 启动测试用例的方法
    def setUp(self):
        print('加载初始化数据')
    def add_test(self):
        self.assertEqual(3,3)
    def tearDown(self):
        '''释放数据，关闭测试用例'''
        print('结束测试')

if __name__ == '__main__':
    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(Test('add_test'))
    # 测试套件
    suite = unittest.Testsuite()
    suite.add_
