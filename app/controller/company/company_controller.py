import sqlite3
import string
import random
DATABASE_NAME = 'IoT.db'

def get_random_password():
    # choose from all lowercase letter
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(36))
    print("Random password is:", password)
    return password

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