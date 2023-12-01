import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class knowledge:
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    csr = conn.cursor()

    def __init__(self, course, content, university_name, stu_id, program_name):
        self.course = course
        self.content = content
        self.university_name = university_name
        self.stu_id = stu_id
        self.program_name = program_name

    def add_new(self):
        self.csr.execute('INSERT INTO posts (title, content, university ,stu_id, project) VALUES (?, ?, ?, ?, ?)',
                         (self.course, self.content, self.university_name, self.stu_id, self.program_name))

    def getUN(self):
        return self.csr.execute('SELECT university from post')

    def getPN(self):
        return self.csr.execute('SELECT project from post')

    def getRecord(self):
        return self.csr.execute('SELECT * from post')

    def Database_close(self):
        self.conn.commit()
        self.conn.close()
