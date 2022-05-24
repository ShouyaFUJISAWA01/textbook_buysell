from flask import render_template, request, url_for,session, redirect

from lib.db import db

from lib.models import User

from app import app


#ログイン画面を表示
@app.route('/')
def top():
    return render_template('login.html')

#新規登録画面を表示
@app.route('/register')
def register():
    return render_template('register.html')

#フォームに入力された内容をuserテーブルに保存する
@app.route('/register/create', methods=['POST'])
def create():
    name=request.form.get('name'),
    address=request.form.get('address'),
    tel=request.form.get('tel'),
    email=request.form.get('email'),
    password=request.form.get('password'),
    
    user=User(name=name, address=address, tel=tel, email=email,password=password)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return redirect(url_for('register'))
    return redirect(url_for('top'))

#ログイン処理を行う
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter(User.email==email)
        user=User.filter(User.password==password).first()
        if user is None:
            return redirect(url_for('home'))
        session['user_id']=user.user_id
        return render_template('login.html')

#会員ページを表示
@app.route('/home')
def home():
    return render_template('home.html')

#ログアウト処理を行う
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('top'))
