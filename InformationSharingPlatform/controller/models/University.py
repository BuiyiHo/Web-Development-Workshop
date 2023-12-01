import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class University:

    def __init__(self, name, program_list):
        self.name = name
        self.program_list = program_list

    def getName(self):
        return self.name

    def addProgram(self):
        return self

    def getProgram_list(self):
        return self




