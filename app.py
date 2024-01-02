from flask import Flask
app = Flask(__name__)

from . import db
from .db import books, Session