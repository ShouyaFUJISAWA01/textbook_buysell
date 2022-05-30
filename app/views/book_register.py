from flask import Blueprint, render_template, request, url_for, session, redirect,flash

import datetime

from lib.models import Book

from lib.db import db


book_register_bp = Blueprint('book_register', __name__)


# 教科書登録確認画面を表示
@book_register_bp.route('/book_register/confirm', methods=['POST'])
def book_register_confirm():
    if request.method == 'POST':
        title=request.form.get('title')
        user_id=session.get('user_id')
        isbn_no=request.form.get('isbn_no')
        author=request.form.get('author')
        publisher=request.form.get('publisher')
        price=request.form.get('price')
        category=request.form.get('category')
        status=request.form.get('status')
        try:
            return render_template('homes/book_register_confirm.html', title=title, user_id=user_id, isbn_no=isbn_no, author=author, publisher=publisher, price=price, category=category, status=status)
        except:
            flash('入力した値を再度確認してください', 'error')
            return redirect(url_for('home.book_register'))
    return redirect(url_for('top.home'))


# 教科書登録処理
@book_register_bp.route('/book_register/create', methods=['POST'])
def book_register():
    book=Book(
        title=request.form.get('title'),
        user_id=session.get('user_id'),
        isbd_no=request.form.get('isbn_no'),
        author=request.form.get('author'),
        publisher=request.form.get('publisher'),
        price=request.form.get('price'),
        category=request.form.get('category'),
        status=request.form.get('status'),
        updated = None
    )
    try:
        db.session.add(book)
        db.session.commit()
    except:
        flash('入力した値を再度確認してください', 'error')
        return redirect(url_for('home.book_register'))
    return redirect(url_for('top.home'))

