import sqlite3
import os

DATABASE_NAME = 'IoT.db'


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def init_db():

    db = get_db()

    with open('db/schema.sql') as f:
        db.executescript(f.read())

init_db()
os.rename("IoT.db", "app/IoT.db")