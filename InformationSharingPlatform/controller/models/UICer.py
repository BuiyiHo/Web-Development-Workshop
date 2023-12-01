import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class uicer:

    def __init__(self, name, gpa, email, password):
        self.name = name
        self.gpa = gpa
        self.email = email
        self.password = password

    def verification(self, password):
        return self


class alumni(uicer):
    def __init__(self, name, gpa, email, password, status, anonymous):
        uicer.__init__(self, name, gpa, email, password)
        self.status = status
        self.anonymous = anonymous
