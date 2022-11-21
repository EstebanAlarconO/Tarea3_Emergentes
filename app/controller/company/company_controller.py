import sqlite3
DATABASE_NAME = 'IoT.db'

def insert_company(company_name, company_api_key):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()    
    statement = "INSERT INTO company(company_name, company_api_key) VALUES (?, ?)"
    cursor.execute(statement, [company_name, company_api_key])
    db.commit()
    return True

def delete_company(key):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "DELETE FROM company WHERE company_api_key = ?"
    cursor.execute(statement, [key])
    db.commit()
    return True

def get_by_name(company_name):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT * FROM company WHERE company_name = ?"
    cursor.execute(statement, [company_name])
    return cursor.fetchone()

def get_companies():
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    query = "SELECT * FROM company"
    cursor.execute(query)
    return cursor.fetchall()