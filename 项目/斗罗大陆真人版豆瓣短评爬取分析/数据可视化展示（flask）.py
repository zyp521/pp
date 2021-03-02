from flask import Flask, render_template, jsonify, request
from MyDB_ import MyDB
import settings


db = MyDB(h=settings.HOST, u=settings.USER, p=settings.PASSWORD, db=settings.DATABASE)

app = Flask(__name__,static_url_path='statics',static_folder='statics')


@app.route('/')
def index():
    return '测试画面'


@app.route('/find', methods=['get'])
def find_comment():
    pageNo = request.args.get('pageNo')
    pageSize = request.args.get('pageSize')
    sql = 'select * from douluo_comment limit %s,%s;'
    data = ((int(pageNo) - 1) * int(pageSize), int(pageSize))
    res = db.select(sql, data)
    res_dict = {}
    res_list = []
    for i in res:
        each_obj = dict(list(zip(('id', 'comment', 'type'), i)))
        res_list.append(each_obj)
    res_dict['data'] = res_list
    print(res_dict)
    return jsonify(res_dict)


@app.route('/report')
def analysis_report():


    return '数据分析报告'


if __name__ == '__main__':
    # 解决浏览器显示编码问题
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=5000)
