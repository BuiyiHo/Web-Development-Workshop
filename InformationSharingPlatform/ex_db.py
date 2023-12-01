import sqlite3

# 创建数据库链接
connection = sqlite3.connect('experience.db')

# 执行db.sql中的SQL语句
with open('ex.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

# 提交前面的数据操作
connection.commit()

# 关闭链接
connection.close()