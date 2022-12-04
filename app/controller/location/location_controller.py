import sqlite3
DATABASE_NAME = 'IoT.db'




def insert_locations(company, name, country, city, meta):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()    
    statement = "INSERT INTO location(company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company, name, country, city, meta])
    db.commit()
    return True


def update_location(name, country, city, meta, id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "UPDATE location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE id = ?"
    cursor.execute(statement, [name, country, city, meta, id])
    db.commit()
    return True


def delete_location(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    for i in id:
        statement = "DELETE FROM location WHERE id = ?"
        cursor.execute(statement, [i[0]])
    db.commit()
    return True


def get_by_id(key,id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = """SELECT l.* FROM company AS c, location AS l 
                WHERE c.company_api_key = ? 
                AND c.id = l.company_id
                AND l.id = ?
                """ 
    cursor.execute(statement, [key,id])
    return cursor.fetchone()

def get_locations(key):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    query = """SELECT l.* FROM company AS c, location AS l 
                WHERE c.company_api_key = ? 
                AND c.id = l.company_id
                """ 
    cursor.execute(query,[key])
    return cursor.fetchall()    