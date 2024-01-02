from .app import app
from flask import render_template, request, redirect, url_for
from flask import render_template

from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy.orm import sessionmaker
from .db import books, Session

DATABASE = 'mysql+pymysql://yuta_suzuki:chihayaSHOGO118!@localhost/books?charset=utf8'
engine = create_engine(DATABASE, echo=True)

@app.route('/')
def index():
    session = Session()
    result = session.query(books).all()
    session.close()

    books_list = []
    for row in result:
        books_list.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})

    return render_template('index.html', books=books_list)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    session = Session()
    sql = insert(books).values(title=title, price=price, arrival_day=arrival_day)
    session.execute(sql)
    session.commit()
    session.close()

    return redirect(url_for('index'))