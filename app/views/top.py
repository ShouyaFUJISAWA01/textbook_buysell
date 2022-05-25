from flask import render_template, request, url_for,session, redirect, Blueprint

import datetime

from lib.db import db

from lib.models import User,Book

top_bp=Blueprint('top', __name__)


#ログイン画面を表示
@top_bp.route('/top')
def top():
    return render_template('top/login.html')

#新規登録画面を表示
@top_bp.route('/top/register')
def register():
    return render_template('top/register.html')

#フォームに入力された内容をuserテーブルに保存する
@top_bp.route('/top/register/create', methods=['POST'])
def create():
    name=request.form.get('name')
    address=request.form.get('address')
    tel=request.form.get('tel')
    email=request.form.get('email')
    password=request.form.get('password')
    
    user=User(name=name, address=address, tel=tel, email=email,password=password, updated=None)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return redirect(url_for('top.register'))
    return redirect(url_for('top.top'))

#ログイン処理を行う
@top_bp.route('/top/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter(User.email==email)
        user=user.filter(User.password==password).first()
        if user is None:
            return redirect(url_for('top.top'))
        session['user_id']=user.id
        return redirect(url_for('top.home'))

#会員ページを表示
@top_bp.route('/top/home')
def home():
    user_id=session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    books=Book.query.filter(Book.user_id == user_id).all()
    return render_template('top/home.html', books=books, user=user, user_id=user_id)
    


#ログアウト処理を行う
@top_bp.route('/top/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('top.top'))
