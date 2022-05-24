from sre_parse import CATEGORIES
from flask import Blueprint, render_template, request, url_for, session, redirect,flash

from lib.models import Book, book

from lib.db import db

import datetime

book_info_change_delete = Blueprint('book_info_change', __name__)





# 教科書情報変更処理
@book_info_change_delete.route('/book_info_change/<int:id>/update', methods=['POST'])
def book_info_change(id):
    book=Book.query.get(id)
    book.user_id=Book.query('user_id').get(id) #書き方合ってるかわかりません。id行のuser_idを取得したいです。
    book.user_id=Book.query.get('user_id'.id) #書き方合ってるかわかりません。id行のuser_idを取得したいです。
    book.isbn_no=request.form.get('isbn_no')
    book.name=request.form.get('name')
    book.author=request.form.get('author')
    book.company=request.form.get('company')
    book.price=request.form.get('price')
    book.category=request.form.get('category')
    book.status=request.form.get('status')
    book.updated=datetime.datetime.now()
    try:
        db.session.merge(book)
        db.session.commit()
    except:
        flash('入力した値を再度確認してください')
        return redirect(url_for('homes.book_info_change', id=id))
    # flash('教科書情報が変更されました','success')←これ必要なのかわかりません。
    return redirect(url_for('top.home'))

# 教科書削除処理
@book_info_change_delete.route('/home/<int:id>/delete', methods=['POST'])
def book_info_delete(id):
  book = Book.query.get(id)
  db.session.delete(book)
  db.session.commit()
  flash('教科書が削除されました')
#   会員ページ(home.html)にflash文を追加してほしいです。エラーメッセージが表示できるようにしてください。
  return redirect(url_for('top.home'))