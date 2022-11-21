import sqlite3
DATABASE_NAME = 'IoT.db'




def insert_locations(name, country, city, meta, company):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()    
    statement = "INSERT INTO location(company_api_key, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company, name, country, city, meta])
    db.commit()
    return True


def update_location(name, country, city, meta, company, id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "UPDATE location SET company_id = ?, location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE id = ?"
    cursor.execute(statement, [company, name, country, city, meta, id])
    db.commit()
    return True


def delete_location(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "DELETE FROM location WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT * FROM location WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_locations():
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    query = "SELECT * FROM location"
    cursor.execute(query)
    return cursor.fetchall()    