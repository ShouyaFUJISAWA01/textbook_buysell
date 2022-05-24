from http.client import CREATED
from sre_parse import CATEGORIES
from flask import Blueprint, request, url_for, session, redirect,flash

import datetime

from lib.models import Book

from lib.db import db


book_register = Blueprint('book_register', __name__)

# 教科書登録処理
@book_register.route('/book_register/create', methods=['POST'])
def book_register():
    book=Book(
        name=request.form.get('name'),
        user_id=session.get('auth_id'),
        isbd_no=request.form.get('isbn_no'),
        author=request.form.get('author'),
        company=request.form.get('company'),
        price=request.form.get('price'),
        category=request.form.get('category'),
        status=request.form.get('status'),
        created=datetime.datetime.now()
    )
    try:
        db.session.add(book)
        db.session.commit()
    except:
        flash('入力した値を再度確認してください')
        return redirect(url_for('homes.book_register'))
    return redirect(url_for('homes.home'))

