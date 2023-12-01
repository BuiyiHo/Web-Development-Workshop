import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class Program:

    def __init__(self, name, universityName, GPA_low, GPA_upper):
        self.name = name
        self.universityName = universityName
        self.GPA_low = GPA_low
        self.GPA_upper = GPA_upper

    def getName(self):
        return self.name

    def getUniversityName(self):
        return self.universityName

    def update(self, GPA):
        if GPA > self.GPA_upper:
            self.GPA_upper = GPA

        if GPA < self.GPA_low:
            self.GPA_low = GPA



