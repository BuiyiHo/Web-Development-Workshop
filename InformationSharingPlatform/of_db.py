import sqlite3

# 创建数据库链接
connection = sqlite3.connect('offer.db')

# 执行db.sql中的SQL语句
with open('of.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

cur.execute("insert into Toffer(GPA, date, university, program, qs, place) values (?, ?, ?, ?, ?, ?)",
            ("3.0", "2021-10-3", "UIC", "cst", "2", "HK"))


# 提交前面的数据操作
connection.commit()

# 关闭链接
connection.close()
