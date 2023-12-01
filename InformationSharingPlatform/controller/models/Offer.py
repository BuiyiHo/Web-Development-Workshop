import sqlite3  # 引入sqlite3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required


class offer:
    conn = sqlite3.connect("offer.db")
    conn.row_factory = sqlite3.Row

    def __init__(self, GPA, ID, Image, DATE, v):
        self.GPA = GPA
        self.ID = ID
        self.Image = Image
        self.DATE = DATE
        self.v = v

    def getGPA(self):
        return self.GPA

    def getDATE(self):
        return self.DATE

    def getID(self):
        return self.ID

    def verify(self):
        return self.v

    def Database_close(self):
        self.conn.commit()
        self.conn.close()


class companyOffer(offer):
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row

    def __init__(self, GPA, ID, Image, DATE, v, title, companyName):
        offer.__init__(self, GPA, ID, Image, DATE, v)
        self.title = title
        self.companyName = companyName

    def getGPA(self):
        offer.getGPA(self)

    def getDATE(self):
        offer.getDATE(self)

    def getID(self):
        offer.getID(self)

    def verify(self):
        offer.verify(self)

    def Database_close(self):
        offer.Database_close(self)

    def getTitle(self):
        return self.title

    def getCompanyName(self):
        return self.companyName


class taughtCourseOffer(offer):
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row

    def __init__(self, GPA, ID, Image, DATE, v, universityName, programName):
        offer.__init__(self, GPA, ID, Image, DATE, v)
        self.universityName = universityName
        self.programName = programName

    def getGPA(self):
        offer.getGPA(self)

    def getDATE(self):
        offer.getDATE(self)

    def getID(self):
        offer.getID(self)

    def verify(self):
        offer.verify(self)

    def getUniName(self):
        return self.universityName

    def getProgramName(self):
        return self.programName

    def Database_close(self):
        offer.Database_close(self)


class researchOffer(taughtCourseOffer):
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row

    def __init__(self, GPA, ID, Image, DATE, v, universityName, programName, supervisor, topic, NoPapers, NoResearch):
        taughtCourseOffer.__init__(self, GPA, ID, Image, DATE, v, universityName, programName)
        self.supervisor = supervisor
        self.topic = topic
        self.NoPapers = NoPapers
        self.NoResearch = NoResearch

    def getGPA(self):
        taughtCourseOffer.getGPA(self)

    def getDATE(self):
        taughtCourseOffer.getDATE(self)

    def getID(self):
        taughtCourseOffer.getID(self)

    def verify(self):
        taughtCourseOffer.verify(self)

    def getUniName(self):
        taughtCourseOffer.getUniName(self)

    def getProgramName(self):
        taughtCourseOffer.getProgramName(self)

    def getSupervisor(self):
        return self.supervisor

    def papersNO(self):
        return self.NoPapers

    def researchNO(self):
        return self.NoResearch

    def Database_close(self):
        taughtCourseOffer.Database_close(self)
