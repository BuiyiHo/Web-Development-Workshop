import sqlite3

from flask import Flask, Blueprint

from controller.views import index_bp
from controller.views.Offer import offer_bp
from controller.views.UICer import UICer_bp
from controller.views.experience import experience_bp
from controller.views.report import report_bp
from controller.views.search import search_bp
from settings import DevelopmentConfig
from controller.views.knowledge_point import knowledge_bp


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config['SECRET_KEY'] = 'Eric'
    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 注册蓝图
    Blueprint('my_blueprint', __name__, static_folder='static', static_url_path='/static')
    app.register_blueprint(index_bp, url_prefix='/', static_folder='static', static_url_path='/static')
    app.register_blueprint(knowledge_bp, url_prefix='/knowledge', static_folder='static', static_url_path='/static')
    app.register_blueprint(UICer_bp, url_prefix='/UICer', static_folder='static', static_url_path='/static')
    app.register_blueprint(offer_bp, url_prefix='/offer', static_folder='static', static_url_path='/static')
    app.register_blueprint(experience_bp, url_prefix='/viewExperience', static_folder='static', static_url_path='/static')
    app.register_blueprint(report_bp, url_prefix='/report', static_folder='static', static_url_path='/static')
    app.register_blueprint(search_bp, url_prefix='/search', static_folder='static', static_url_path='/static')
    return app