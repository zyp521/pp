class Buttetin:
    '''
    年度公报类对象：用于公报对象的二次加工过滤和持久化保存
    '''

    def __init__(self, year='未知', province='未知', city='未知', name='统计公报', content='未知',
                 release_date='2021/3/26', url='http://www.tjcn.org/tjgb/'):
        self.year = year
        self.province = province
        self.city = city
        self.name = name
        self.content = content
        self.release_date = release_date
        self.url = url

    def save(self):

        pass
