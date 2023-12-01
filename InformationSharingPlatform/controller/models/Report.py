import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class Report:

    def __init__(self, year, offer):
        self.year = year
        self.offer = offer

    def summarize(self, offer, gpa):
        return self.name

    def getOffer(self):
        return self.offer

    def export(self, summarize):
        return self

    def getyear(self):
        return self.year