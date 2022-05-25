from flask import Flask


from lib.db import init_db

app = Flask(__name__)

app.config.from_object('app.config')
app.config.from_object('lib.config')


init_db(app)

# 「Views.py」をインポート
from app.views import book_info_change, book_management, book_register, top, user_info_change, user_management,buy,homes

app.register_blueprint(book_info_change.book_info_change_delete, url_prefix='/')
app.register_blueprint(book_management.book_management, url_prefix='/')
app.register_blueprint(book_register.book_register_bp, url_prefix='/')
app.register_blueprint(top.top_bp, url_prefix='/')
app.register_blueprint(user_info_change.user_info_change_bp, url_prefix='/')
app.register_blueprint(user_management.user_management, url_prefix='/')
app.register_blueprint(buy.buy_bp, url_prefix='/')
app.register_blueprint(homes.home_bp, url_prefix='/')