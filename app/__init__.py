from flask import Flask


from lib.db import init_db

app = Flask(__name__)

app.config.from_object('app.config')
app.config.from_object('lib.config')


init_db(app)

# 「Views.py」をインポート
from app.views import book_info_change, book_management, book_register, top, user_info_change, user_management

app.register_blueprint(book_info_change.book_info_change_delete)
app.register_blueprint(book_management.book_management)
app.register_blueprint(book_register.book_register_bp)
app.register_blueprint(top.top_bp)
app.register_blueprint(user_info_change.user_info_change_bp)
app.register_blueprint(user_management.user_management)