import sqlite3
DATABASE_NAME = 'app\IoT.db'


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def init_db():

    db = get_db()

    with open('schema.sql') as f:
        db.executescript(f.read())

init_db()