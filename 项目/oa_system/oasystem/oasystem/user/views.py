from oasystem.user.models import Department, Person, Position, Permission, Attendance
from flask import render_template, redirect, request
import os, time
from oasystem.user import userbp


# 添加职员的测试数据
@userbp.route('/add_test/')
def add_test():
    # 创建部门
    dept_obj = Department(name='研发部', desc='高大上')
    dept_obj.save()

    # 创建职位
    pos_obj = Position(name='开发工程师', level=1)
    pos_obj.department_id = dept_obj.id  # 设置关系
    pos_obj.save()

    # 创建员工
    per_obj = Person()
    per_obj.name = 'zs'
    per_obj.password = pwdjm('222')
    per_obj.jobnum = 'zs123'
    per_obj.position_id = pos_obj.id
    per_obj.save()

    return 'add test success'


from functools import wraps


def login_check(func):
    @wraps(func)
    def inner():
        person_name = request.cookies.get('person_name')
        if person_name:
            return func()
        else:
            return redirect('/login/')

    return inner


import hashlib


def pwdjm(pwd):
    md5 = hashlib.md5(pwd.encode())
    result = md5.hexdigest()  # 生成密文
    return result


@userbp.route('/')
@userbp.route('/index/')
@login_check
def index():
    # 思路： 通过查询部门找到职位，通过职位找到员工。
    # 组织数据结构 [{'dept_name':'研发部','count':10},{}]
    # 查询前5条新闻
    # 查询考勤前5条。
    return render_template('index.html')


# @userbp.route('/person_list/')
# @login_check
# def person_list():
#     # 1.查询数据库中的数据
#     person_obj_list = Person.query.all()
#     # 2.返回页面，并且渲染数据。
#     return render_template('person.html', person_obj_list=person_obj_list)


from flask import request, redirect


@userbp.route('/add_person/', methods=['GET', 'POST'])
def add_person():
    # request.method : 获取前端访问的方式
    print(request.method, type(request.method))  # GET,POST <class 'str'>

    if request.method == 'GET':
        # 1.获取所有的职位
        pos_obj_list = Position.query.all()
        # 2.返回页面，并且渲染数据
        return render_template('add_person.html', pos_obj_list=pos_obj_list)
    else:
        # post 方式提交执行

        # 1.获取表单提交的内容
        username = request.form.get('username')
        password = request.form.get('password')
        jobnum = request.form.get('jobnum')
        position_id = request.form.get('position_id')  # 开发工程师
        print(username, password, jobnum, position_id)
        # # 2.保存到数据库。
        person_obj = Person()
        person_obj.name = username
        person_obj.password = pwdjm(password)
        person_obj.jobnum = jobnum
        person_obj.position_id = position_id
        person_obj.save()

        # 3.重定向到职员列表页面。
        return redirect('/person_list/')


# 为啥不使用render_template。
# form表单中的action 可以不写，为啥也能访问到。

@userbp.route('/person_detail/')
def person_detail():
    # 获取get方式请求的参数
    id = request.args.get('id')
    person_obj = Person.query.get(id)
    return render_template('profile.html', person_obj=person_obj)


# 修改操作
@userbp.route('/edit_person/', methods=['GET', 'POST'])
def edit_person():
    if request.method == 'GET':
        # 1. 获取职员id
        id = request.args.get('id')
        # 2. 根据职员id 查询数据库,获取具体对象。
        person_obj = Person.query.get(id)
        # 3.获取所有的职位
        position_obj_list = Position.query.all()
        # 3. 返回页面并且渲染数据
        return render_template('edit_profile.html', person_obj=person_obj, position_obj_list=position_obj_list)
    else:
        # post 请求
        # 1.获取表单提交的内容
        id = request.form.get('id')
        username = request.form.get('username')
        jobnum = request.form.get('jobnum')
        nickname = request.form.get('nickname')
        gender = request.form.get('gender')
        age = request.form.get('age')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        position_id = request.form.get('position_id')  # 职位id

        t = str(time.time())

        # 获取图片对象
        photo = request.files.get('photo')  # <FileStorage: '1.jpg' ('image/jpeg')>
        if photo.filename:
            # 查询数据库是否有图片，如果有则删除否则不删除
            per_obj = Person.query.get(id)
            if per_obj.picture:
                # 删除项目中的图片
                os.remove(per_obj.picture)

            # 保存上传的新图片
            path = 'static/image/' + t + '_' + photo.filename
            photo.save(path)

        # # 2.查询数据库并且修改
        person_obj = Person.query.get(id)
        person_obj.name = username
        person_obj.jobnum = jobnum
        person_obj.nickname = nickname
        person_obj.gender = gender
        person_obj.age = age
        person_obj.phone = phone
        person_obj.email = email
        person_obj.address = address
        person_obj.position_id = position_id
        if photo.filename:
            person_obj.picture = path  # 保存图片路径
        person_obj.update()

        # # 3.重定向到职员列表页面
        return redirect('/person_list/')


# 删除操作
@userbp.route('/delete_person/')
def delete_person():
    # 1.获取职员id。
    id = request.args.get('id')
    # 2.查询数据库并且删除。
    person_obj = Person.query.get(id)
    # 先删除图片再删除职员记录。
    path = person_obj.picture
    # 如果没有图片则不需要删除
    if path:
        os.remove(path)
    # 无论是否有图片，都删除此对象。
    person_obj.delete()
    # 3.重定向到职员列表页面。
    return redirect('/person_list/')


@userbp.route('/search_person/')
def search_person():
    # 1.获取前端提交的姓名
    name = request.args.get('name')
    # 2.查询数据库
    # person_obj_list = Person.query.filter(Person.name == name).all()
    # 模糊查询
    person_obj_list = Person.query.filter(Person.name.like('%' + name + '%')).all()
    # 3.返回页面
    return render_template('person.html', person_obj_list=person_obj_list)


# 设置cookie
@userbp.route('/login/', methods=['GET', 'POST'])
def login():
    error_msg = ''
    username = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password = pwdjm(password)  # 对内容进行加密。
        person_obj = Person.query.filter(Person.name == username, Person.password == password).first()
        if person_obj:
            # 将用户名保存到cookie中
            response = redirect('/index/')
            response.set_cookie('person_name', username)
            response.set_cookie('person_id', str(person_obj.id))
            return response

        error_msg = '用户名或者密码错误'

    return render_template('login.html', error_msg=error_msg, username=username)


@userbp.route('/logout/')
@login_check
def logout():
    response = redirect('/login/')
    # 1.删除cookie
    response.delete_cookie('person_name')
    response.delete_cookie('person_id')
    # 2.重定向到登录界面
    return response


# ---------------------------------部门管理------------------------------
#  查看部门
@userbp.route('/dept_list/')
def dept_list():
    # 1.查询所有的部门
    dept_obj_list = Department.query.all()
    return render_template('department.html', dept_obj_list=dept_obj_list)


@userbp.route('/add_dept/', methods=['GET', 'POST'])
def add_dept():
    if request.method == 'POST':
        # 1.获取表单提交的内容
        name = request.form.get('name')
        description = request.form.get('description')
        # 2.保存到数据库
        dept_obj = Department(name=name, desc=description)
        dept_obj.save()
        # 3.重定向到部门列表
        return redirect('/dept_list/')

    return render_template('add_department.html')


@userbp.route('/edit_dept/', methods=['GET', 'POST'])
def edit_dept():
    if request.method == 'POST':
        # 1.获取表单提交的内容
        department_id = request.form.get('department_id')
        name = request.form.get('name')
        description = request.form.get('description')

        # 2.修改数据库
        dept_obj = Department.query.get(department_id)
        dept_obj.name = name
        dept_obj.desc = description
        dept_obj.update()
        # 3.重定向到部门列表
        return redirect('/dept_list/')
    else:
        # get 请求
        id = request.args.get('id')
        dept_obj = Department.query.get(id)
        return render_template('edit_department.html', dept_obj=dept_obj)


# 查看职位
@userbp.route('/position_list/')
def position_list():
    # 1.获取当前部门
    dept_id = request.args.get('dept_id')
    dept_obj = Department.query.get(dept_id)
    # 2.查找部门对应的职位
    position_obj_list = dept_obj.positions
    # print(position_obj_list)
    return render_template('position.html', position_obj_list=position_obj_list, dept_obj=dept_obj)


# 添加职位
@userbp.route('/add_position/', methods=['GET', 'POST'])
def add_position():
    # 1.获取表单提交的内容
    name = request.form.get('name')
    level = request.form.get('level')
    dept_id = request.form.get('dept_id')

    # 2.保存到数据库
    position_obj = Position()
    position_obj.name = name
    position_obj.level = level
    position_obj.department_id = dept_id
    position_obj.save()

    # 3.重定向到职位列表,注意需要携带部门的id但是参数名称不能任意写。
    return redirect('/position_list/?dept_id=' + dept_id)


# 删除职位
@userbp.route('/delete_position/')
def delete_position():
    # 1.获取职位id
    id = request.args.get('id')
    # 2.查询数据库并且删除
    position_obj = Position.query.get(id)

    # 查询对应的员工删除
    person_obj_list = position_obj.persons
    for person_obj in person_obj_list:
        person_obj.delete()

    position_obj.delete()
    # 3.重定向到职位列表
    return redirect('/position_list/?dept_id=' + str(position_obj.department_id))


# 编辑职位
@userbp.route('/edit_position/', methods=['GET', 'POST'])
def edit_position():
    # 1.获取表单提交的内容
    position_id = request.form.get('position_id')
    name = request.form.get('name')
    level = request.form.get('level')
    print(position_id, name, level)
    # 2.查询数据库并且修改
    position_obj = Position.query.get(position_id)
    position_obj.name = name
    position_obj.level = level
    position_obj.update()
    # 3.重定向到职位列表。
    return redirect('/position_list/?dept_id=' + str(position_obj.department_id))


# 删除部门
@userbp.route('/delete_dept/')
def delete_dept():
    # 1.获取部门id
    id = request.args.get("id")
    # 2.查询部门并且删除
    dept_obj = Department.query.get(id)
    # 先删除职员，然后删除职位。
    pos_obj_list = dept_obj.positions  # 获取职位列表
    # 每一个职位对应多个职员
    for pos_obj in pos_obj_list:
        per_obj_list = pos_obj.persons
        for per_obj in per_obj_list:
            per_obj.delete()

        # 删除职位
        pos_obj.delete()

    dept_obj.delete()

    # 3.重定向到部门列表
    return redirect('/dept_list/')


# -------------------------------------考勤管理---------------------------------
# 自己的考勤列表
@userbp.route('/att_list_me/')
def attendance_list_me():
    # 1.获取当前用户的id。
    person_id = request.cookies.get('person_id')
    # 2.根据id 当前用户所有的考勤。
    att_obj_list = Attendance.query.filter(Attendance.person_id == person_id).all()
    # 3.返回页面并且渲染数据。

    return render_template('attendance_me.html', att_obj_list=att_obj_list)


import datetime


# 添加自己的考勤
@userbp.route('/add_att_me/', methods=['GET', 'POST'])
def add_attendance_me():
    # 1.获取表单提交的内容
    reason = request.form.get('reason')  # 请假原因
    type = request.form.get('type')  # 请假类型
    day = request.form.get('day')  # 请假天数
    start = request.form.get('start')  # 开始日期
    end = request.form.get('end')  # 结束日期
    # print(reason, type, day, start, end)
    # 2.保存到数据库
    att_obj = Attendance()
    att_obj.reason = reason
    att_obj.atype = type
    att_obj.adate = day
    att_obj.start_time = datetime.datetime.strptime(start, '%Y-%m-%d')  # 2020-09-30
    att_obj.end_time = datetime.datetime.strptime(end, '%Y-%m-%d')
    person_id = request.cookies.get('person_id')  # 注意:写完后，先登出操作，然后在登录切记！！！
    att_obj.person_id = person_id
    att_obj.save()

    # 3.重定向到自己的考勤列表
    return redirect('/att_list_me/')


@userbp.route('/att_list_sub/', methods=['GET', 'POST'])
def attendance_list_sub():
    # 逻辑: 根据 小于当前用户的职级和相同部门查找职位 --->> 根据职位查找职员 --->> 根据职员查找考勤
    # 1.当前用户的id
    person_id = request.cookies.get('person_id')
    person_obj = Person.query.get(person_id)
    pos_obj = person_obj.position  # 职位对象
    level = pos_obj.level  # 当前用户的职级
    dept_id = pos_obj.department_id  # 当前用户部门id

    # 查询当前用户部门下，比当前用户职级小的职位。
    pos_obj_list = Position.query.filter(Position.level < level, Position.department_id == dept_id).all()
    # 根据职位查询员工
    persons_list = []
    for pos_obj in pos_obj_list:
        # 获取每一个职位对应的所有的员工
        persons_list += pos_obj.persons  # 将所有的员工保存起来。

    # 根据员工查询对应的考勤
    kq_list = []  # 保存所有的考勤
    for person_obj in persons_list:
        attendances_obj_list = person_obj.attendances
        kq_list += attendances_obj_list

    return render_template('attendance_subordinate.html', kq_list=kq_list)


# 修改下属考勤状态
@userbp.route('/update_att_sub/')
def update_attendance_sub():
    # 1.获取考勤id 和 状态
    id = request.args.get('id')
    status = request.args.get('status')

    # 2.根据id查询数据库并且修改状态
    att_obj = Attendance.query.get(id)
    att_obj.astauts = status
    person_name = request.cookies.get('person_name')
    att_obj.examine = person_name  # 审核人
    att_obj.update()

    return redirect('/att_list_sub/')


# -----------------------------------权限管理-----------------------
# 权限列表
@userbp.route('/permission_list/')
def permission_list():
    # 1.查询数据库中所有的权限
    per_obj_list = Permission.query.all()
    # 2.返回页面
    return render_template('permission.html', per_obj_list=per_obj_list)


# 添加权限
@userbp.route('/add_permission/', methods=['GET', 'POST'])
def add_permission():
    if request.method == 'POST':
        # 1.获取表单提交的数据
        name = request.form.get('name')
        description = request.form.get('description')
        # 2.保存到数据库
        permission_obj = Permission(name=name, desc=description)
        permission_obj.save()
        # 3.重定向到权限列表
        return redirect('/permission_list/')

    return render_template('add_permission.html')


# 修改权限
@userbp.route('/edit_permission/', methods=['GET', 'POST'])
def edit_permission():
    if request.method == 'POST':
        # 1.获取表单提交的内容
        id = request.form.get('id')
        name = request.form.get('name')
        description = request.form.get('description')
        # 2.根据id 查询数据库并且修改
        per_obj = Permission.query.get(id)
        per_obj.name = name
        per_obj.desc = description
        per_obj.update()
        # 3.重定向到权限列表
        return redirect('/permission_list/')
    else:
        # get 请求
        # 1.获取id
        id = request.args.get('id')
        # 2.查询数据库并且返回
        per_obj = Permission.query.get(id)
        return render_template('edit_permission.html', per_obj=per_obj)


# 删除权限
@userbp.route('/delete_permission/')
def delete_permission():
    # 1.获取id
    id = request.args.get('id')
    # 2.查询数据库并且删除
    per_obj = Permission.query.get(id)
    per_obj.delete()
    # 3.重定向到权限列表页面
    return redirect('/permission_list/')


# -------------------------关联职位---------------

# 思路： 查询当前权限关联的所有职位，和 查询出来的所有职位的id进行一个比较。

# 权限查询所有的职位
@userbp.route('/all_position_list/', methods=['GET', 'POST'])
def all_position_list():
    if request.method == 'GET':
        # 3.获取权限id
        per_id = request.args.get('per_id')
        # 4.查询权限对应的职位对象对象
        per_obj = Permission.query.get(per_id)
        pos_list = per_obj.positions
        # 获取职位id
        pos_id_list = []
        for pos_obj in pos_list:
            pos_id_list.append(pos_obj.id)

        # 1.查询所有的职位
        pos_obj_list = Position.query.all()
        return render_template('position_permission.html', pos_obj_list=pos_obj_list, per_id=per_id,
                               pos_id_list=pos_id_list)

    else:
        # post 请求
        # 2.获取权限id
        per_id = request.form.get('per_id')
        # 1.获取选中的checkbox的值
        # 注意使用 getlist()方法获取提交的内容
        position_ids = request.form.getlist('position_ids')
        print(position_ids)  # ['1', '4', '5']
        pos_list = []
        for position_id in position_ids:
            pos_obj = Position.query.get(position_id)
            pos_list.append(pos_obj)

        # 3.设置权限和职位的关系
        per_obj = Permission.query.get(per_id)
        per_obj.positions = pos_list
        per_obj.save()
        return redirect('/permission_list/')


# 全局装饰器
@userbp.add_app_template_global
def aa():
    result = {
        'news': False,
        'renshi': False
    }
    # 思路通过 用户---职位--权限，根据权限名称进行设置
    person_id = request.cookies.get('person_id')
    person_obj = Person.query.get(person_id)
    pos_obj = person_obj.position  # 职位对象
    permission_obj_list = pos_obj.permissions  # 权限对象。

    for permission_obj in permission_obj_list:
        if permission_obj.name == '新闻管理':
            result['news'] = True

        if permission_obj.name == '人事管理':
            result['renshi'] = True

    return result


# --------------------分页--------------------------
# 分页测试
@userbp.route('/fytest/')
def fytest():
    # 所有的职员
    # person_obj_list = Person.query.all()
    # print(person_obj_list)
    # 第一个参数开始的页码，例如第几页
    # 第二个参数，每一页返回的数据条数
    pagination_obj = Person.query.paginate(2, 1)
    # print(pagination_obj) # <flask_sqlalchemy.Pagination object at 0x0000000004C72488>
    # print(pagination_obj.items)  # 获取具体的对象
    # print(pagination_obj.has_prev)  # 判断是否有上一页,如果有返回True 否则返回False
    # print(pagination_obj.has_next)  # 是否有下一页,如果有返回True 否则返回False
    # print(pagination_obj.prev_num)  # 上一页页码。如果没有返回None
    # print(pagination_obj.next_num)  # 下一页页码。如果没有返回None
    # print(pagination_obj.page) # 当前页码。
    # print(pagination_obj.pages)  # 总页码数
    # print(pagination_obj.iter_pages()) # 可以循环遍历生成页码。
    for page in pagination_obj.iter_pages():
        print(page)
    return '分页...'


@userbp.route('/person_list/')
@login_check
def person_list():
    # 0.获取前端传递过来的页码
    page = int(request.args.get('page', 1))
    # 1.查询数据库中的数据
    pagination_obj = Person.query.paginate(page, 1)
    person_obj_list = pagination_obj.items
    # 3.判断页码范围
    if page <= 3:
        start = 0
        end = 5
    elif page > pagination_obj.pages - 3:
        start = pagination_obj.pages - 5
        end = pagination_obj.pages
    else:
        start = page - 3
        end = page + 2

    # 2.生成页码(使用自带的iter_pages效果不好)
    page_page = range(1, pagination_obj.pages + 1)[start:end]

    return render_template('person.html', person_obj_list=person_obj_list, page_page=page_page,
                           pagination_obj=pagination_obj)


# ============================ 首页返回数据====================

# 测试ajax
@userbp.route('/indextext/')
def indextest():
    return render_template('indextest.html')


from flask import jsonify


@userbp.route('/ajaxtest/')
def ajaxtest():
    # 返回json数据
    dic = {'status': 'ok'}
    print('xxxxxx')
    return jsonify(dic)  # 将python中的字典转换为json对象。


# 返回首页echarts数据
@userbp.route('/indexajax/')
def indexajax():
    # 1.查询部门以及对应的人数[{},{}]
    # 思路: 通过部门-->> 职位--->> 员工
    dept_obj_list = Department.query.all()

    dept_info_list = []

    for dept_obj in dept_obj_list:
        dic = {}
        dic['dept_name'] = dept_obj.name
        # print(dept_obj.name)
        # 获取部门对应的所有的职位
        positions_list = dept_obj.positions
        # 获取每个职位对应的员工
        # 计算职员总数
        # 研发部
        # 开发工程师   7
        # 高级开发工程师 1
        total_person_num = 0
        for position_obj in positions_list:
            person_obj_list = position_obj.persons
            num = len(person_obj_list)
            total_person_num += num

        dic['num'] = total_person_num

        # 将字典追加到列表中
        dept_info_list.append(dic)

    return jsonify(dept_info_list)
