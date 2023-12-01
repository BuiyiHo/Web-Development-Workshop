import sqlite3

# 创建数据库链接
connection = sqlite3.connect('user.db')

# 执行db.sql中的SQL语句
with open('userdb.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

cur.execute("INSERT INTO userinfo (username, password, status) VALUES (?, ?, ?)",('q030026209','123456','student'))
cur.execute("INSERT INTO userinfo(username, password, status) VALUES (?, ?, ?)", ('0001','98765','admin'))
cur.execute("INSERT INTO userinfo(username, password, status) VALUES (?, ?, ?)", ('yangzheng','1','alumni'))
# 提交前面的数据操作
connection.commit()

# 关闭链接
connection.close()
