import sqlite3
from flask import render_template, request, url_for, flash, redirect, Blueprint, session

from controller.models import knowledge_point

knowledge_bp = Blueprint('knowledge', __name__)


def get_db_connection():
    # 创建数据库链接到database.db文件
    conn = sqlite3.connect('database.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn


def get_sc_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('university.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post


@knowledge_bp.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@knowledge_bp.route('/posts/new', methods=('GET', 'POST'))
def new():
    status = session.get('status')
    if status != 'alumni':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        university = request.form['university']
        project = request.form['project']
        stu_id = session.get('id')

        if not title:
            flash('Title can not be empty!')
        elif not content:
            flash('Content can not be empty!')
        elif not university:
            flash('University can not be empty!')
        elif not project:
            flash('Project can not be empty!')
        else:
            n = knowledge_point.knowledge(title, content, university, stu_id, project)
            n.add_new()
            n.Database_close()
            flash('Successfully added!')
            return redirect(url_for('knowledge.Knowledge'))

    return render_template('new.html')


@knowledge_bp.route('/posts/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    status = session.get('status')
    if status == 'student':
        flash('You don not have access!')
        return render_template('about.html')
    post = get_post(post_id)
    id2 = session.get('id')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        university = request.form['university']
        project = request.form['project']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Knowledge point is required!')
        elif not university:
            flash('University is required!')
        elif not project:
            flash('Project is required!')
        else:
            conn = get_db_connection()
            id3 = conn.execute('select stu_id from posts where id ==? ', (post_id,)).fetchone()[0]
            if id2 == id3:
                conn.execute('UPDATE posts SET title = ?, content = ?, university = ?, project = ?'
                             ' WHERE id = ?',
                             (title, content, university, project, post_id))
                conn.commit()
                conn.close()
                return redirect(url_for('knowledge.Knowledge'))
            else:
                flash("You don't have access!")
                return redirect(url_for('knowledge.Knowledge'))

    return render_template('edit.html', post=post)


@knowledge_bp.route('/posts/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    status = session.get('status')
    if status == 'student':
        flash('You don not have access!')
        return render_template('about.html')
    id2 = session.get('id')
    post = get_post(post_id)
    conn = get_db_connection()
    id3 = conn.execute('select stu_id from posts where id ==? ', (post_id,)).fetchone()[0]
    if id2 == id3 or status == 'admin':
        conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        conn.commit()
        conn.close()
        flash('"{}" Delete successfully!'.format(post['title']))
    else:
        flash("You don't have access!")
    return redirect(url_for('knowledge.Knowledge'))


@knowledge_bp.route('/')
def Knowledge():
    # 调用上面的函数，获取链接
    conn = get_db_connection()
    # 查询所有数据，放到变量posts中
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # 把查询出来的posts传给网页
    return render_template('knowledge_index.html', posts=posts)
