import base64
import io
import sqlite3
from io import BytesIO
import numpy as np
import xlwt
from flask import render_template, request, session, Blueprint, flash, redirect, Flask, url_for, make_response
from matplotlib import pyplot as plt

report_bp = Blueprint('report', __name__)


def write_list_to_file(list1):
    with open('list_data.txt', 'w') as file:
        for item in list1:
            file.write(str(item) + '\n')


def read_list_from_file():
    list1 = []
    with open('list_data.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line != 'None':
                list1.append(int(line))
    return list1


@report_bp.route('/viewreport', methods=['GET', 'POST'])
def viewreport():
    loaded_list = read_list_from_file()
    year = request.args.get('year')
    conn = get_offer_connection()
    if str(year) in map(str, loaded_list):
        results = conn.execute(
            'select university, place, qs, count(university) as amount from Toffer where date '
            'between ? and ? group by university order by qs', (f'{year}-01-01', f'{year}-12-31')).fetchall()
        Roffer = conn.execute(
            'select university, place, qs, count(university) as amount from Roffer where date '
            'between ? and ? group by university order by qs', (f'{year}-01-01', f'{year}-12-31')).fetchall()
        coun = conn.execute(
            'select count(place) as amount from Toffer where date '
            'between ? and ? group by place', (f'{year}-01-01', f'{year}-12-31')).fetchall()
        labels = conn.execute(
            'select place as amount from Toffer where date '
            'between ? and ? group by place', (f'{year}-01-01', f'{year}-12-31')).fetchall()
        conn.close()
        # 转成一维array
        coun = np.array(coun)
        labels = np.array(labels)
        y = coun.reshape(-1)
        l = labels.reshape(-1)
        # 画图
        img = io.BytesIO()
        plt.title("The percentage of countries that give offers to UIC students")
        plt.pie(y, labels=l)
        plt.savefig(img, format='png')
        img.seek(0)
        # 传图
        plot_url = base64.b64encode(img.getvalue()).decode()
        return render_template('viewReportpage.html', year=year, result=results, plot_url=plot_url, Roffer=Roffer)
    conn.close()
    flash("The report not exists!")
    return render_template('viewreport.html', year=year)


# 展示yearly report
@report_bp.route('/report', methods=['GET', 'POST'])
def report():
    status = session.get('status')
    if status != 'admin':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    year = request.args.get('year')
    if year:
        session['year'] = year
    year = session.get('year')
    loaded_list = read_list_from_file()
    loaded_list.append(year)
    print(loaded_list)
    write_list_to_file(loaded_list)
    conn = get_offer_connection()
    results = conn.execute(
        'select university, place, qs, count(university) as amount from Toffer where date '
        'between ? and ? group by university order by qs', (f'{year}-01-01', f'{year}-12-31')).fetchall()
    offer = conn.execute('SELECT * FROM Toffer WHERE date BETWEEN ? AND ?',
                         (f'{year}-01-01', f'{year}-12-31')).fetchall()

    coun = conn.execute(
        'select count(place) as amount from Toffer where date '
        'between ? and ? group by place', (f'{year}-01-01', f'{year}-12-31')).fetchall()
    labels = conn.execute(
        'select place as amount from Toffer where date '
        'between ? and ? group by place', (f'{year}-01-01', f'{year}-12-31')).fetchall()
    conn.close()
    # 转成一维array
    coun = np.array(coun)
    labels = np.array(labels)
    y = coun.reshape(-1)
    l = labels.reshape(-1)
    # 画图
    img = io.BytesIO()
    plt.title("The percentage of countries that give offers to UIC students")
    plt.pie(y, labels=l)
    plt.savefig(img, format='png')
    img.seek(0)
    # 传图
    plot_url = base64.b64encode(img.getvalue()).decode()
    if offer:
        #下载文件
        if request.method == 'POST':
            fields = ["University Name", "Country", "QS Ranking", "Number of Students"]
            new = xlwt.Workbook(encoding='utf-8')
            sheet = new.add_sheet('report', cell_overwrite_ok=True)
            for i in range(0, len(fields)):
                sheet.write(0, i, fields[i])
            row = 1

            for row, offer_data in enumerate(results, start=1):
                sheet.write(row, 0, offer_data[0])
                sheet.write(row, 1, offer_data[1])
                sheet.write(row, 2, offer_data[2])
                sheet.write(row, 3, offer_data[3])
            sio = BytesIO()
            new.save(sio)  # 将数据存储为bytes
            sio.seek(0)
            response = make_response(sio.getvalue())
            response.headers['Content-Type'] = 'application/vnd.ms-excel'
            response.headers['Content-Disposition'] = f'attachment; filename=report_{year}.xls'
            return response
        #跳到展示界面
        elif request.method == 'GET':
             return render_template('report.html', offer=offer, year=year, result=results, plot_url=plot_url)
    else:
        if year:
            flash("No information in " + year + "!", 'error')
        else:
            flash("Please wait the admin to generate report.")
        return render_template('makereport.html')


@report_bp.route('/makereport', methods=['POST', 'GET'])
def makereport():
    status = session.get('status')
    if status != 'admin':
        flash('You have no authority!')
        return redirect(url_for('UICer.about'))
    return render_template('makereport.html')


def get_db_connection():
    # 创建数据库链接到database.db文件
    conn = sqlite3.connect('database.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn


@report_bp.route('/report<int:offer_id>', methods=['POST', 'GET'])
# 展示report的细节
def post_offer(offer_id):
    post = get_offerid(offer_id)
    return render_template('offerdetail.html', post=post)


def get_offerid(offer_id):
    conn = get_db_connection()
    post = conn.execute('select * from offer where id = ?',
                        (offer_id,)).fetchone()
    conn.close()
    return post


@report_bp.route('/stuviewreport', methods=['POST', 'GET'])
def stuviewreport():
    conn = get_db_connection()


def get_offer_connection():
    # 创建数据库链接到experience.db文件
    conn = sqlite3.connect('offer.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn
