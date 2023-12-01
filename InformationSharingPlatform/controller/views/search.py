import sqlite3

from flask import Blueprint, request, flash, redirect, render_template, url_for, session

search_bp = Blueprint('search', __name__)


@search_bp.route('/searchGPA', methods=['GET', 'POST'])
def search_gpa():
    # gpa1 在前，原则上gpa1小于gpa2
    gpa1 = request.form.get('gpa1')
    gpa2 = request.form.get('gpa2')
    type = request.form.get('offertype')
    if gpa1 == '':
        gpa1 = None
    if gpa2 == '':
        gpa2 = None
    if gpa1 is None or gpa2 is None:
        flash('Please input your GPA range.')
        return render_template('searchGPA.html')
    if gpa1 is not None and gpa2 is not None:
        if gpa1 is not None and gpa2 is not None and gpa1 > gpa2:
            gpa1, gpa2 = gpa2, gpa1
            print(gpa2)
        if gpa1 is not None and gpa2 is not None and (float(gpa1) < 0.0 or float(gpa2) > 4.0):
            flash("Please input valid number which between 0 and 4.0")
            return render_template('searchGPA.html')
        conn = get_offer_connection()
        if type == 'research':
            p = conn.execute('select * from Roffer where gpa >=? and gpa<=?', (gpa1, gpa2)).fetchall()
        elif type == 'taught':
            p = conn.execute('select * from Toffer where gpa >=? and gpa<=?', (gpa1, gpa2)).fetchall()
        elif type =='company':
            p = conn.execute('select * from Coffer where gpa >=? and gpa<=?', (gpa1, gpa2)).fetchall()
        if not p:
            flash("Sorry, no offers in this section.")
            conn.close()
            return render_template('searchGPA.html')
        else:
            conn.close()
            return render_template('search.html', pos=p, gpa1=gpa1, gpa2=gpa2)
    return render_template('searchGPA.html')

# 根据GPA


@search_bp.route('/searchUniversityName', methods=['GET', 'POST'])
def search_u_name():
    type = request.form.get('offertype')
    u_name = request.form.get('university')
    program = request.form.get('program')
    conn = get_offer_connection()
    if type == 'research':
        program_name = conn.execute('select * from Roffer where program ==?', (program,)).fetchall()
        if not program_name:
            flash('Can not find program, please check your input')
            p = conn.execute('select * from Roffer where university ==?', (u_name,)).fetchall()
        else:
            p = conn.execute('select * from Roffer where university ==? and program ==?', (u_name, program)).fetchall()
        number = conn.execute('select count(university) as amount from Roffer where university ==?', (u_name,)).fetchall()
    else:
        program_name = conn.execute('select * from Toffer where program ==?', (program,)).fetchall()
        if not program_name:
            flash('Can not find program, please check your input')
            p = conn.execute('select * from Toffer where university ==?', (u_name,)).fetchall()
        else:
            p = conn.execute('select * from Toffer where university ==? and program ==?', (u_name, program)).fetchall()
        number = conn.execute('select count(university) as amount from Toffer where university ==?',
                              (u_name,)).fetchall()
    if not p:
        flash("Can not find university, please check your input.")
        conn.close()
        return render_template('searchUniversityName.html')
    else:
        conn.close()
        return render_template('search_n.html', pos=p, number=number, university=u_name)

    # 根据学校名


@search_bp.route('/Search_Plate', methods=['GET', 'POST'])
def Search_Plate():
    return render_template('Search_Plate.html')


def get_offer_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('offer.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn
