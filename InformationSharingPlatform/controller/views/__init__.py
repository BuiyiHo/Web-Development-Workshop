import sqlite3

from flask import Blueprint, render_template, app

index_bp = Blueprint('index', __name__, static_folder="static", static_url_path='/static/')


@index_bp.route('/')
def index():
    return render_template('welcome.html')
