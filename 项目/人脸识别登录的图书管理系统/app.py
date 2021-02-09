from flask import Flask, render_template, request
import face_recognition
import base64, pickle

app = Flask(__name__, template_folder='templates')


# @app.route('/', methods=['GET', 'POST'])
# def test():
#     return '测试代码'

@app.route('/login', methods=['GET', 'POST'], endpoint='log')
# Map([<Rule '/login' (HEAD, POST, OPTIONS, GET) -> log>,endpoint映射表对应视图端名称，视图函数应该可以重名
def login():
    if request.method == 'POST':
        image_object = request.files.get('img')
        print(image_object.name)
        image_object.save('1.png')
        return ''
    else:
        return render_template('face_login.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='0.0.0.0', port=5000)
