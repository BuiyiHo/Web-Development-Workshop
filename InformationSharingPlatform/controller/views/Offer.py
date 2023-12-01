import sqlite3

from flask import Blueprint, request, flash, redirect, render_template, url_for, session

offer_bp = Blueprint('offer', __name__)


@offer_bp.route('/provideOffer_T', methods=('GET', 'POST'))
def provideOffer_T():
    status = session.get('status')
    if status != 'alumni':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    if request.method == 'POST':
        DATE = request.form['date']
        GPA = request.form['gpa']
        UniverName = request.form['university']
        ProgramName = request.form['program']

        if not DATE:
            flash('DATE can not be empty!')
        elif not GPA:
            flash('GPA can not be empty!')
        elif float(GPA) > 4 or float(GPA) <= 0:
            flash("Wrong!The range of GPA is between 0 and 4")
        elif not UniverName:
            flash('UniverName can not be empty!')
        elif not ProgramName:
            flash('ProgramName can not be empty!')
        else:
            conn = get_sc_connection()
            univername = conn.execute('SELECT * from universitylist where name ==?', (UniverName,)).fetchall()
            conn.close()
            if not univername:
                flash("Your university is not in the list, please add your university and program, thank you.")
                return redirect(url_for('offer.adduniversity'))
            else:
                conn = get_sc_connection()
                qs = conn.execute('select qs from universitylist where name==?', (UniverName,)).fetchone()[0]
                print(qs)
                place = conn.execute('select place from universitylist where name==?', (UniverName,)).fetchone()
                if place is not None:
                    place = place[0]
                    print(place)
                conn = get_offer_connection()
                conn.execute("insert into Toffer(GPA, date, university, qs, place, program) values (?, ?, ?, ?, ?, ?)",
                             (GPA, DATE, UniverName, qs, place, ProgramName))
                conn.commit()
                conn.close()
                flash('Successfully added!')
                return redirect(url_for('offer.provideOffer_T'))
    return render_template('provideOffer_T.html')


@offer_bp.route('/provideOffer_C', methods=('GET', 'POST'))
def provideOffer_C():
    status = session.get('status')
    if status != 'alumni':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    if request.method == 'POST':
        DATE = request.form['date']
        GPA = request.form['gpa']
        title = request.form['title']
        companyName = request.form['company']

        if not DATE:
            flash('DATE can not be empty!')
        elif not GPA:
            flash('GPA can not be empty!')
        elif float(GPA) > 4 or float(GPA) <= 0:
            flash("Wrong!The range of GPA is between 0 and 4")
        elif not title:
            flash('title can not be empty!')
        elif not companyName:
            flash('companyName can not be empty!')
        else:
            conn = get_offer_connection()
            conn.execute('INSERT INTO Coffer (date, gpa, title, company) VALUES (?, ?, ?, ?)',
                         (DATE, GPA, title, companyName))
            conn.commit()
            conn.close()
            flash('Successfully added!')
            return redirect(url_for('offer.provideOffer_C'))

    return render_template('provideOffer_C.html')


@offer_bp.route('/provideOffer_R', methods=('GET', 'POST'))
def provideOffer_R():
    status = session.get('status')
    if status != 'alumni':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    if request.method == 'POST':
        DATE = request.form['date']
        GPA = request.form['gpa']
        UniverName = request.form['university']
        ProgramName = request.form['program']
        Supervisor = request.form['supervisor']
        Topic = request.form['topic']
        NOpapers = request.form['paper']
        NOresearch = request.form['research']

        if not DATE:
            flash('DATE can not be empty!')
        elif not GPA:
            flash('GPA can not be empty!')
        elif float(GPA) > 4 or float(GPA) <= 0:
            flash("Wrong!The range of GPA is between 0 and 4")
        elif not UniverName:
            flash('UniverName can not be empty!')
        elif not ProgramName:
            flash('ProgramName can not be empty!')
        elif not Supervisor:
            flash('Supervisor can not be empty!')
        elif not Topic:
            flash('Topic can not be empty!')
        elif not NOpapers:
            flash('The NO. of papers can not be empty!')
        elif not NOresearch:
            flash('The NO. of research can not be empty!')
        else:
            conn = get_sc_connection()
            univername = conn.execute('SELECT * from universitylist where name ==?', (UniverName,)).fetchall()
            conn.close()
            if not univername:
                flash("Your university is not in the list, please add your university and program, thank you.")
                return redirect(url_for('offer.adduniversity'))
            else:
                conn = get_sc_connection()
                qs = conn.execute('select qs from universitylist where name==?', (UniverName,)).fetchone()[0]
                print(qs)
                place = conn.execute('select place from universitylist where name==?', (UniverName,)).fetchone()
                if place is not None:
                    place = place[0]
                    print(place)
                conn = get_offer_connection()
                conn.execute(
                    'INSERT INTO Roffer (date, gpa, university ,program, supervisor, topic, NOpapers, NOresearch, '
                    'place)'
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (DATE, GPA, UniverName, ProgramName, Supervisor, Topic, NOpapers, NOresearch, place))
                conn.commit()
                conn.close()
                flash('Successfully added!')
                return redirect(url_for('offer.provideOffer_R'))

    return render_template('provideOffer_R.html')


@offer_bp.route('/adduniversity', methods=('GET', 'POST'))
def adduniversity():
    if request.method == 'POST':
        name = request.form['university']
        program = request.form['program']
        qs = request.form['qs']
        place = request.form['place']
        if not name:
            flash('School name can not be empty!')
        elif not program:
            flash('Program can not be empty!')
        else:
            conn = get_sc_connection()
            conn.execute('INSERT INTO universitylist (name, program, qs, place) VALUES (?, ?, ?, ?)',
                         (name, program, qs, place))
            conn.commit()
            conn.close()
            flash('Successfully added!')
            return redirect(url_for('UICer.about'))
    return render_template('adduniversity.html')


def get_sc_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('university.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn


def get_offer_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('offer.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn
