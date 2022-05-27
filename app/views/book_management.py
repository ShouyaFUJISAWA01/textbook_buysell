from flask import render_template, request, url_for, session, redirect, flash, Blueprint

import datetime

from lib.models import Book

from lib.db import db


book_management = Blueprint('book_management', __name__)

#選択された教科書の情報変更ページを表示
@book_management.route('/book_info_change/show/<int:id>')
def book_info_show(id):
    book_info=Book.query.get(id)
    return render_template('book_management/book_info_change_admin.html', book_info=book_info)

#検索結果に一致する教科書情報を一覧表示する
@book_management.route('/book_info_change/search', methods=['POST'])
def book_search():
    searched_title = request.form.get('search')
    if searched_title == '':
        books = Book.query.all()
    else:
        books = Book.query.filter(Book.title==searched_title).all()
    return render_template('book_management/book_management.html', books=books)

#選択された教科書を削除し、教科書一覧を再表示する
@book_management.route('/book_info_change/admin_delete/<int:id>', methods=['POST'])
def book_delete(id):
    book_info = Book.query.get(id)
    try:
        db.session.delete(book_info)
        db.session.commit()
    except:
        return redirect(url_for('home.book_management'))
    return redirect(url_for('home.book_management'))

#選択された教科書内容を入力内容に更新し、一覧を再表示する
@book_management.route('/book_info_change/admin_update/<int:id>', methods=['POST'])
def book_update(id):
    book_info = Book.query.get(id)
    book_info.title = request.form.get('title')
    book_info.isbn_no = request.form.get('isbn')
    book_info.author = request.form.get('author')
    book_info.publisher = request.form.get('publisher')
    book_info.price = request.form.get('price')
    book_info.category = request.form.get('category')
    book_info.status = request.form.get('status')
    book_info.updated = datetime.datetime.now()

    try:
        db.session.merge(book_info)
        db.session.commit()
    except:
        flash('入力した内容を再度確認してください')
        return redirect(url_for('book_management.book_info_show', id=id))
    return redirect(url_for('home.book_management'))




