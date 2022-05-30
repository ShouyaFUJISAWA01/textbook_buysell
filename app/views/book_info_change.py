from flask import Blueprint, render_template, request, url_for, redirect,flash,session

from lib.models import Book

from lib.db import db

import datetime

book_info_change_bp = Blueprint('book_info_change', __name__)





# 教科書情報変更処理
@book_info_change_bp.route('/book_info_change/<int:id>/update', methods=['POST'])
def book_info_change(id):
    book=Book.query.get(id)
    book.user_id = session.get('user_id')
    book.isbn_no=request.form.get('isbn_no')
    book.title=request.form.get('title')
    book.author=request.form.get('author')
    book.publisher=request.form.get('publisher')
    book.price=request.form.get('price')
    book.category=request.form.get('category')
    book.status=request.form.get('status')
    book.updated=datetime.datetime.now()
    try:
        db.session.merge(book)
        db.session.commit()
    except:
        flash('入力した値を再度確認してください', 'error')
        return redirect(url_for('home.book_info_change', id=id))
    return redirect(url_for('top.home'))

#教科書情報変更確認画面
@book_info_change_delete.route('/home/book_delete/confirm/<int:id>', methods=['POST'])
def book_confirm(id):
    title=request.form.get('title')
    isbn_no=request.form.get('isbn_no')
    author=request.form.get('author')
    publisher=request.form.get('publisher')
    price=request.form.get('price')
    category=request.form.get('category')
    status=request.form.get('status')
    return render_template('homes/book_confirm.html',title=title, isbn_no=isbn_no, author=author, publisher=publisher,price=price, category=category, status=status, id=id )


@book_info_change_bp.route('/home/book_delete/confirm/<int:id>')
def show_book_delete_page(id):
    book_info = Book.query.get(id)
    return render_template('homes/book_delete_confirm.html', book_info=book_info)

# 教科書削除処理
@book_info_change_bp.route('/home/book_delete/<int:id>', methods=['POST'])
def book_info_delete(id):
    book = Book.query.get(id)
    try:
        db.session.delete(book)
        db.session.commit()
    except:
        return redirect(url_for('top.home'))
    return redirect(url_for('top.home'))