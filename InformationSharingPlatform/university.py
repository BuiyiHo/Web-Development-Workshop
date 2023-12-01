import sqlite3

# 创建数据库链接
connection = sqlite3.connect('university.db')

# 执行db.sql中的SQL语句
with open('university.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()
cur.execute("insert into universitylist(name, qs, program, place) values (?, ?, ?, ?)",
            ("UIC", "2", "cst", "HK"))
cur.execute("insert into universitylist(name, qs, program, place) values (?, ?, ?, ?)",
            ("HKBU", "1", "cst", "HK"))
# 提交前面的数据操作
connection.commit()

# 关闭链接
connection.close()
