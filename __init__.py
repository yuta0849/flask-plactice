import sys
sys.path.insert(0, '/Users/ca01603/Desktop/flaskr')

from flask import Flask
app = Flask(__name__)
import flaskr

from flaskr import db
db.create_books_table()