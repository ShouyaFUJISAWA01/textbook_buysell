from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import User, Book

from lib.db import db


user_management = Blueprint('user_management', __name__)


@user_management.route('/user_info_change/show/<int:id>')
def user_info_show(id):
    user_info = User.query.get(id)
    return render_template('user_management/user_info_change_admin.html', user_info=user_info)


@user_management.route('user_info_change/search', methods=['POST'])
def user_search():
    searched_name = request.form.get('search')
    print(searched_name)
    if searched_name == '':
        users = User.query.all()
    else:
        users = User.query.filter(User.name==searched_name).all()
    return render_template('homes/user_management.html', users=users)


@user_management.route('/user_info_change/admin_delete/<int:id>', methods=['POST'])
def user_delete(id):
    user_info = User.query.get(id)
    books_info = Book.query.filter(Book.user_id == id).all()
    for book_info in books_info:
        db.session.delete(book_info)
        db.session.commit()
    try:
        db.session.delete(user_info)
        db.session.commit()
    except:
        return redirect(url_for('home.user_management'))
    return redirect(url_for('home.user_management'))


@user_management.route('/user_info_change/admin_update/<int:id>', methods=['POST'])
def user_update(id):
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
        flash('入力した内容を再度確認してください')
        return redirect(url_for('user_management.user_info_show', id=id))
    return redirect(url_for('home.user_management'))

#変更確認画面
@user_management.route('/user_info_change/confirm/<int:id>', methods=['POST'])
def user_confirm(id):
    name=request.form.get('name')
    address=request.form.get('address')
    tel=request.form.get('tel')
    email=request.form.get('email')
    user_id=id
    return render_template('homes/user_info_change_confirm.html', name=name,address=address,tel=tel,email=email,user_id=user_id)
