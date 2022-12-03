import sqlite3
import string
import random
DATABASE_NAME = 'IoT.db'

def get_api_key():
    # choose from all lowercase letter
    characters = string.ascii_letters + string.digits
    api_key = ''.join(random.choice(characters) for i in range(36))
    return api_key

def insert_sensor(location_id, sensor_name, sensor_category, sensor_meta):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "INSERT INTO sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, get_api_key()])
    db.commit()
    return True


def update_sensor(id, location_id, sensor_name, sensor_category, sensor_meta):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "UPDATE sensor SET location_id = ?, sensor_name = ?, sensor_category = ?, sensor_meta = ? WHERE id = ?"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, id])
    db.commit()
    return True


def delete_sensor(sensor_id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()

    if(type(sensor_id) == list):
        for i in sensor_id:
            statement = "DELETE FROM sensor WHERE sensor_id = ?"
            cursor.execute(statement, [i])
    else:
        statement = "DELETE FROM sensor WHERE sensor_id = ?"
        cursor.execute(statement, [sensor_id])
    db.commit()
    return True


def get_by_id(company_api_key, sensor_id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = """SELECT s.* FROM sensor AS s, company AS c, location AS l 
                WHERE c.company_api_key = ? 
                AND c.id = l.company_id
                AND l.id = s.location_id 
                AND s.id = ?
                """  
    cursor.execute(statement, [company_api_key, sensor_id])
    return cursor.fetchone()

def get_all_sensors(company_api_key):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    query =  """SELECT s.* FROM sensor AS s, company AS c, location AS l 
                WHERE c.company_api_key = ? 
                AND c.id = l.company_id
                AND l.id = s.location_id
            """  
    cursor.execute(query, [company_api_key])
    return cursor.fetchall()