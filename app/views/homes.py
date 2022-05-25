# flask関連のパッケージを取得
from flask import render_template, request, url_for, session, redirect, flash, Blueprint

# Itemモデルを取得
from lib.models import User, Book

# SQLAlchemyを取得
from lib.db import db

# Blueprintでitemアプリケーションを登録
home = Blueprint('home', __name__)

#購入ページの表示
@home.route('/buy')
def buy():
    user_id=session(user_id)
    items=Book.query.filter(Book.user_id==user_id).all()#データベースBookクラスから一覧を持ってくる
    return render_template('homes/buy.html', items=items)


#教科書登録ページの表示
@home.route('/book_register')
def book_register():
    return render_template('homes/book_register.html')


#教科書情報変更ページの表示
@home.route('/book_info_change/<int:id>')
def book_info_change(id):
    book_change=Book.query.get(id)
    return render_template('homes/book_info_change.html', book_change=book_change)


#会員情報変更ページの表示
@home.route('/user_info_change/<int:id>')
def user_info_change(id):
    user_change=User.query.get(id)#idと一致するもの
    return render_template('homes/user_info_change.html', user_change=user_change)


#会員管理ページの表示
@home.routte('/user_management')
def user_management():
    users=User.query.order_by(User.id.desc()).all()
    return render_template('homes/user_management.html', users=users)


#教科書管理ページの表示
@home.route('/book_management')
def book_management():
    books=Book.query.all()
    return render_template('homes/book_management.html', books=books)