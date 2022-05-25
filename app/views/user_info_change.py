from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import User, Book

from lib.db import db


user_info_change = Blueprint('user_info_change', __name__)


# 以下で使うidを後ほどHTMLで指定する
@user_info_change.route('/user_info_change/update/<int:id>', methods=['POST'])
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
        return redirect(url_for('homes.user_info_change', id=id))
    return redirect(url_for('top.home'))

# 以下で使うidを後ほどHTMLで指定する
@user_info_change.route('/home/delete/<int:id>', methods=['POST'])
def user_info_delete(id):
    user_info = User.query.get(id)
    db.session.delete(user_info)
    db.session.commit()
    return redirect(url_for('top.home'))