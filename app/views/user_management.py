from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import User, Book

from lib.db import db


user_management = Blueprint('user_management', __name__)


@user_management.route('/user_info_change/show/<int:id>')
def user_info_show(id):
    user_info = User.query.get(id)
    return render_template('user_info_change_admin.html', user_info=user_info)


@user_management.route('user_info_change/search', methods=['POST'])
def user_search():
    searched_name = request.form.get('search')
    if searched_name == '':
        user_info = User.query.all()
    else:
        user_info = User.query.filter(User.name==searched_name)
    return render_template('user_info_change_admin', user_info=user_info)


@user_management.route('/user_info_change/delete/<int:id>', methods=['POST'])
def user_delete(id):
    user_info = User.query.get(id)
    db.session.delete(user_info)
    db.session.commit()
    return redirect(url_for('user_management.user_search'))


@user_management.route('/user_info_change/update', methods=['POST'])
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
    return redirect(url_for('user_management.user_search'))