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
    items=Book.query.order_by(Book.id.desc()).all()#データベースBookクラスから一覧を持ってくる
    return render_template('buy.html', items=items)


#教科書登録ページの表示(OK)
@home.route('/book_register')
def book_register():
    return render_template('book_register.html')


#教科書情報変更ページの表示
@home.route('/book_info_change')
def book_info_change(id):
    book_change=Book.query.get(id)
    return render_template('book_info_change.html', book_change=book_change)


#会員情報変更ページの表示
@home.route('/user_info_change/<int:id>')
def user_info_change(id):
    user_change=User.query.get(id)#idと一致するもの
    return render_template('user_info_change.html', user_change=user_change)


#会員管理ページの表示
@home.routte('/user_management')
def user_management():
    users=User.query.order_by(User.id.desc()).all()
    return render_template('user_management.html', users=users)


#教科書管理ページの表示
@home.route('/book_management')
def book_management():
    books=Book.query.all()
    return render_template('book_management.html', books=books)