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


def delete_sensor(key):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "DELETE FROM sensor WHERE sensor_api_key = ?"
    cursor.execute(statement, [key])
    db.commit()
    return True


def get_by_id(company_api_key, sensor_id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT t1.* FROM sensor AS t1, company AS t2, location AS t3 WHERE t2.company_api_key = ? AND t2.company_api_key = t3.company_api_key AND t3.id = t1.location_id AND t1.id = ?"
    cursor.execute(statement, [company_api_key, sensor_id])
    return cursor.fetchone()

def get_all_sensors():
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    query = "SELECT * FROM sensor"
    cursor.execute(query)
    return cursor.fetchall()