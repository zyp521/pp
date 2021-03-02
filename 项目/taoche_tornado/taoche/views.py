# 视图
import tornado.web
from elasticsearch import Elasticsearch


# 1.传统方式 使用 tornado 查询 es 获取数据 将数据返回给页面，页面进行渲染

class CarIndex1(tornado.web.RequestHandler):

    def initialize(self):
        # 1.链接es
        self.es = Elasticsearch(hosts='10.10.123.27', timeout=100)
        # 2.设置查询条件
        self.body = {
            'query': {
                'match_all': {}
            }
        }

    def get(self):
        result = self.es.search(index='carlist', doc_type='car', body=self.body)
        # print(result)
        car_list = []
        hits_list = result['hits']['hits']
        for hits_dic in hits_list:
            car_dic = hits_dic['_source']
            # print(car_dic)
            car_list.append(car_dic)

        self.render('car_index1.html', car_list=car_list)


# 回顾vue
class VueHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('vuetest.html')


class VueAjaxHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write({'status': 'ok'})


# 返回首页页面
class CarIndex2(tornado.web.RequestHandler):

    def get(self):
        self.render('car_index2.html')


# 返回 首页的json数据
class CarJsonHandler(tornado.web.RequestHandler):

    def initialize(self):
        # 1.链接es
        self.es = Elasticsearch(hosts='10.10.123.27', timeout=100)
        # 2.设置搜索条件
        self.body = {
            'query': {
                'match_all': {}
            }
        }

    def get(self):
        # 3.查询es
        car_dic = self.es.search(index='carlist', doc_type='car', body=self.body)
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(car_dic)


# 首页搜索功能
class CarIndex3(tornado.web.RequestHandler):

    def get(self):
        self.render('car_index3.html')


class CarJson3Handler(tornado.web.RequestHandler):

    def initialize(self):
        self.es = Elasticsearch(hosts='10.10.123.27', timeout=100)

    def get(self):
        # 1.获取搜索的内容
        search_key = self.get_query_argument('search_key', '')
        print(search_key)
        if search_key:  # 表示搜索逻辑
            self.body = {
                'query': {
                    'term': {
                        'c_name': search_key
                    }
                }
            }
        else:  # 查询所有
            self.body = {
                'query': {
                    'match_all': {}
                }
            }
        # 2.查询es
        # 3.返回json数据

        car_dic = self.es.search(index='carlist', doc_type='car', body=self.body)
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(car_dic)


# 分页
class CarIndex4(tornado.web.RequestHandler):

    def get(self):
        self.render('car_index4.html')


class CarJson4Handler(tornado.web.RequestHandler):

    def initialize(self):
        self.es = Elasticsearch(hosts='10.10.123.135', timeout=100)
        # 1.设置每页返回的条数
        self.size = 12
        self.body = {
            'from': 0,
            'size': self.size
        }

    def get(self):
        # 3.获取页码
        page = int(self.get_query_argument('page', '1'))
        # 4.计算内容开始位置
        # page = 1    from 0    0~11
        # page = 2    from 12   12~23
        # from =  (page-1)*size
        start_num = (page - 1) * self.size
        # 5.重新给from 参数赋值
        self.body['from'] = start_num

        search_key = self.get_query_argument('search_key', '')
        print(search_key)
        if search_key:
            # 2.修改查询结构
            self.body['query'] = {
                'term': {
                    'c_name': search_key
                }
            }
        else:
            # 2.修改查询结构
            self.body['query'] = {
                'match_all': {}
            }

        car_dic = self.es.search(index='carlist', doc_type='car', body=self.body)
        print(car_dic)

        # 6.计算总页码
        total = car_dic['hits']['total']
        total_page_num = total / self.size
        if total_page_num != int(total_page_num):
            total_page_num = int(total_page_num) + 1
        else:
            total_page_num = int(total_page_num)

        # 7. 限制页面范围
        p_range = range(1, total_page_num + 1)
        if page < 3:
            page_range = p_range[:5]
        elif page > total_page_num - 3:
            page_range = p_range[total_page_num - 5:]
        else:
            page_range = p_range[page - 3:page + 2]

        page_num_list = list(page_range)
        print(page_num_list)
        car_dic['page_num_list'] = page_num_list
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(car_dic)


# 按价位查询
class CarIndex5(tornado.web.RequestHandler):

    def get(self):
        self.render('car_index5.html')


class CarJson5Handler(tornado.web.RequestHandler):

    def initialize(self):
        self.es = Elasticsearch(hosts='10.10.123.135', timeout=100)
        self.size = 12
        self.body = {
            'from': 0,
            'size': self.size
        }

    def get(self):

        # 1.获取money值
        money = self.get_query_argument('money', '')
        if money:  # 安装价位搜索
            # 因为值的内容为  x3  5d8  d100
            if money.startswith('x'):
                min_money = 0
                max_money = 3
            elif money.startswith('d'):
                min_money = 100
                max_money = 1000
            else:
                money_list = money.split('d')
                min_money = int(money_list[0])
                max_money = int(money_list[1])

        page = int(self.get_query_argument('page', '1'))
        start_num = (page - 1) * self.size
        self.body['from'] = start_num

        search_key = self.get_query_argument('search_key', '')
        print(search_key)
        if search_key:
            if money:
                # 按照 车名称和价格搜索
                self.body['query'] = {
                    'bool': {
                        'must': [
                            {
                                'term': {
                                    'c_name': search_key
                                }
                            },
                            {
                                'range': {
                                    'c_price': {
                                        'gt': min_money,
                                        'lt': max_money
                                    }
                                }
                            }

                        ]

                    }
                }
            else:
                # 只按照车名称搜索
                self.body['query'] = {
                    'term': {
                        'c_name': search_key
                    }
                }
        else:
            # 全部搜索
            self.body['query'] = {
                'match_all': {}
            }

        car_dic = self.es.search(index='carlist', doc_type='car', body=self.body)
        print(car_dic)

        total = car_dic['hits']['total']
        total_page_num = total / self.size
        if total_page_num != int(total_page_num):
            total_page_num = int(total_page_num) + 1
        else:
            total_page_num = int(total_page_num)

        p_range = range(1, total_page_num + 1)
        if page < 3:
            page_range = p_range[:5]
        elif page > total_page_num - 3:
            page_range = p_range[total_page_num - 5:]
        else:
            page_range = p_range[page - 3:page + 2]

        page_num_list = list(page_range)
        print(page_num_list)
        car_dic['page_num_list'] = page_num_list
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(car_dic)
