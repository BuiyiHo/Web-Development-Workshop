import sqlite3
from flask import render_template, request, url_for, flash, redirect, Blueprint, session

experience_bp = Blueprint('experience', __name__)


def get_post2(post_id):
    conn = get_ex_connection()
    post = conn.execute('SELECT * FROM experience WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post


@experience_bp.route('/viewExperience')

def view():

    # 调用上面的函数，获取链接
    conn = get_ex_connection()
    # 查询所有数据，放到变量posts中
    p2 = conn.execute('SELECT * FROM experience').fetchall()
    conn.close()
    # 把查询出来的posts传给网页
    return render_template('viewExperience.html', experience=p2)
# 显示工作经历


@experience_bp.route('/viewExperience/posts2/<int:post_id>')
def post2(post_id):
    p2 = get_post2(post_id)
    return render_template('post2.html', post2=p2)


@experience_bp.route('/viewExperience/posts2/shareExperience', methods=('GET', 'POST'))
def share_e_experience():
    id2 = session.get('id')
    status = session.get('status')
    if status != 'alumni':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        company = request.form['company']
        job = request.form['job']
        stu_id = session.get('id')

        if not title:
            flash('Title can not be empty!')
        elif not content:
            flash('Content can not be empty!')
        elif not company:
            flash('Company can not be empty!')
        elif not job:
            flash('Position can not be empty!')
        else:
            conn = get_ex_connection()
            conn.execute('INSERT INTO experience (title, content, company ,stu_id, job) VALUES (?, ?, ?, ?, ?)',
                         (title, content, company, stu_id, job))
            conn.commit()
            conn.close()
            flash('Successfully added!')
            return redirect(url_for('experience.view'))

    return render_template('shareExperience.html')


@experience_bp.route('/viewExperience/posts2/<int:post_id>/edit2', methods=('GET', 'POST'))
def edit2(post_id):
    status = session.get('status')
    if status == 'student':
        flash('You don not have access!')
        return render_template('about.html')
    p2 = get_post2(post_id)
    id2 = session.get('id')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        company = request.form['company']
        job = request.form['job']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Knowledge point is required!')
        elif not company:
            flash('Company is required!')
        elif not job:
            flash('Job is required!')
        else:
            conn = get_ex_connection()
            id3 = conn.execute('select stu_id from experience where id ==? ', (post_id,)).fetchone()[0]
            if id2 == id3:
                conn.execute('UPDATE experience SET title = ?, content = ?, company = ?, job = ?'
                             ' WHERE id = ?',
                             (title, content, company, job, post_id))
                conn.commit()
                conn.close()
                return redirect(url_for('experience.view'))
            else:
                flash("You don't have access!")
                return redirect(url_for('experience.view'))

        return render_template('edit2.html', post2=p2)

    return render_template('edit2.html', post2=p2)


@experience_bp.route('/viewExperience/posts2/<int:post_id>/delete2', methods=('POST',))
def delete2(post_id):
    status = session.get('status')
    if status == 'student':
        flash('You don not have access!')
        return render_template('about.html')
    p2 = get_post2(post_id)
    id2 = session.get('id')
    print(status)
    conn = get_ex_connection()
    id3 = conn.execute('select stu_id from experience where id ==? ', (post_id,)).fetchone()[0]
    if id2 == id3 or status == 'admin':
        conn.execute('DELETE FROM experience WHERE id = ?', (post_id,))
        conn.commit()
        conn.close()
        flash('"{}" Delete successfully!'.format(p2['title']))
    else:
        flash("You don't have access!")
    return redirect(url_for('experience.view'))
# 删除工作经历


def get_ex_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('experience.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn