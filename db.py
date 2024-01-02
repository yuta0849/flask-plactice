from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Date, inspect
from sqlalchemy.orm import sessionmaker

DATABASE = 'mysql+pymysql://yuta_suzuki:chihayaSHOGO118!@localhost/books?charset=utf8'
engine = create_engine(DATABASE, echo=True)
metadata = MetaData()

# Reflect
metadata.reflect(bind=engine)

# inspector を用意
inspector = inspect(engine)

# booksテーブルの定義を条件付きで行う
if not inspector.has_table("books"): 
    books = Table('books', metadata,
                  Column('title', String(255)),  # 各カラムを定義
                  Column('price', Integer),
                  Column('arrival_day', Date))
    metadata.create_all(engine)  # 定義したテーブルをデータベースに作成
else:
    books = Table('books', metadata, autoload_with=engine)  # ここを修正

Session = sessionmaker(bind=engine)