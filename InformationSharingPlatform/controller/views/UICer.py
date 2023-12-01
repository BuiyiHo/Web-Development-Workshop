import sqlite3

from flask import Blueprint, request, flash, redirect, render_template, url_for, session, make_response

UICer_bp = Blueprint('UICer', __name__)


def get_userinfo():
    # 创建数据库链接到user.db文件
    conn = sqlite3.connect('user.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn


@UICer_bp.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash['username can not be empty']
        elif not password:
            flash['password can not be empty']
        else:
            conn = get_userinfo()
            conn.execute('insert into userinfo (username, password) values (?, ?)', (username, password))
            conn.commit()
            conn.close()
            flash('successfully signed in')
            redirect(url_for('UICer.show'))
    return render_template('signin.html')


@UICer_bp.route('/login', methods=('GET', 'POST'))
def login():
    # 取用户输入值
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        conn = get_userinfo()
        cur = conn.cursor()
        # 比对数据库
        post = cur.execute('select * from userinfo where username ==? and password ==?', (user, pwd)).fetchone()
        if post:
            session['id'] = post[0]
            session["status"] = post[3]
            status = post[3]
            # 不同身份跳转到不同的目录页
            if status == "student":
                print('caonima')
                return redirect(url_for('UICer.about'))
            if status == "admin":
                print('ao')
                return redirect(url_for('UICer.about'))
            if status == "alumni":
                print('wr3er')
                return redirect(url_for('UICer.about'))
        # 密码用户错误弹窗
        else:
            flash("Wrong Username or password!")
            return render_template('login.html')
    else:
        return render_template('login.html')


@UICer_bp.route('/changepwd', methods=('GET', 'POST'))
def changepwd():
    id = session.get('id')
    status = session.get('status')
    # if request.method == 'GET':
    #     return render_template('changepwd.html')
    # if request.method == 'POST':
    newpwd = request.form.get('newpassword')
    oldpwd = request.form.get('oldpassword')
    bt_sub = request.form.get('change')
    bt_back = request.form.get('back')
    conn = get_userinfo()
    userpwd = conn.execute('SELECT password FROM userinfo WHERE id ==? ', (id,)).fetchone()[0]

    if bt_sub == "change":
        if not oldpwd:
            flash('You must enter old password')
            return render_template('changepwd.html')
        elif not newpwd:
            flash('Please enter your new password')
            return render_template('changepwd.html')
        elif oldpwd != userpwd:
            flash('Old password is wrong')
            return render_template('changepwd.html')
        else:
            conn.execute('UPDATE userinfo SET password=?''WHERE id ==?', (newpwd, id))
            conn.commit()
            conn.close()
            flash('You have changed your password successfully!')
            return redirect(url_for('UICer.login'))
    elif bt_back:
        if status == "student":
            return render_template('index_stu.html')
        if status == "admin":
            return render_template('index_admin.html')
        if status == "alumni":
            return render_template('index_alumni.html')

    else:
        return render_template('changepwd.html')


@UICer_bp.route('/show')
def show():
    status = session.get('status')
    if status != 'admin':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    conn = get_userinfo()
    posts = conn.execute('select * from userinfo').fetchall()

    return render_template('show.html', posts=posts)


@UICer_bp.route('/about', methods=['GET', 'POST'])
def about():
    bt_sub = request.form.get('changepwd')
    bt_out = request.form.get('logout')
    if bt_sub:
        return redirect(url_for('UICer.changepwd'))
    if bt_out:
        session.clear()
        flash('You logged out.')
        response = make_response(redirect(url_for('UICer.login')))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return render_template('about.html')
