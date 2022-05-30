from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import User, Book

from lib.db import db


user_info_change_bp = Blueprint('user_info_change', __name__)


# 以下で使うidを後ほどHTMLで指定する
@user_info_change_bp.route('/user_info_change/update/<int:id>', methods=['POST'])
def user_info_change(id):
    user_info = User.query.get(id)
    user_info.name = request.form.get('name')
    user_info.address = request.form.get('address')
    user_info.tel = request.form.get('tel')
    user_info.email = request.form.get('email')
    user_info.updated = datetime.datetime.now()
    try:
        db.session.merge(user_info)
        db.session.commit()
    except:
        flash('入力した内容を再度確認してください', 'error')
        return redirect(url_for('home.user_info_change', id=id))
    return redirect(url_for('top.home'))

#変更確認画面
@user_info_change_bp.route('/home/user_info_change/confirm', methods=['POST'])
def user_confirm():
    name=request.form.get('name')
    address=request.form.get('address')
    tel=request.form.get('tel')
    email=request.form.get('email')
    user_id=session.get('user_id')
    return render_template('homes/user_info_change_confirm.html', name=name,address=address,tel=tel,email=email,user_id=user_id)


# 以下で使うidを後ほどHTMLで指定する
@user_info_change_bp.route('/home/user_delete/<int:id>', methods=['POST'])
def user_info_delete(id):
    user_info = User.query.get(id)
    books_info = Book.query.filter(Book.user_id == id).all()
    try:
        db.session.delete(user_info)
        db.session.commit()
    except:
        return redirect(url_for('top.top'))
    for book_info in books_info:
        db.session.delete(book_info)
        db.session.commit()
    return redirect(url_for('top.top'))