import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("DROP TABLE IF EXISTS books")
    con.execute("CREATE TABLE books (title, price, arrival_day)")
    con.close()