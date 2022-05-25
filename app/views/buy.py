#flask関連のパッケージを取得
from flask import render_template, request, url_for, session, redirect, Blueprint

# Itemモデルを取得
from lib.models import User, Book

# SQLAlchemyを取得
from lib.db import db

# Blueprintでitemアプリケーションを登録
buy_bp = Blueprint('buy', __name__)


#購入確認ページの表示
@buy_bp.route('/buy/confirm/<int:id>')
def buy_confirm(id):
    buy_items=Book.query.get(id)#idと一致する変数に代入
    return render_template('buy/buy_confirm.html',buy_items=buy_items) 


#購入完了ページの表示
@buy_bp.route('/buy/confirm/complete', methods=['POST'])
def buy_complete():
    return render_template('buy/buy_complete.html')
