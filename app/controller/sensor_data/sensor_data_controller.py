from flask import request, jsonify, Flask
import sqlite3
import datetime
DATABASE_NAME = 'IoT.db'

def epoch_to_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time)

def insert_sensor_data(sensor_api_key, json_data):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT sensor_name, location_id FROM sensor WHERE sensor_api_key = ?"
    cursor.execute(statement, [sensor_api_key])
    sensor = cursor.fetchone()
    for i in json_data:
        statement = "INSERT INTO "+sensor[0]+str(sensor[1])+ " (sensor_api_key, medicion, tiempo) VALUES (?,?,?)"
        cursor.execute(statement, [sensor_api_key, i["medicion"], i["tiempo"]])
    db.commit()
    return True

def get_sensor_data(sensor_api_key, from_date, to):

    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT sensor_name, location_id FROM sensor WHERE sensor_api_key= ?"
    cursor.execute(statement, [sensor_api_key])
    nombre, locacion = cursor.fetchone()
    statement = "SELECT * from "+nombre+str(locacion)+" WHERE sensor_api_key = ? AND tiempo >= ? AND tiempo <= ?"
    cursor.execute(statement,[sensor_api_key, epoch_to_date(int(from_date)), epoch_to_date(int(to))])
    return cursor.fetchall()

def delete_sensor_data(sensor_id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()
    statement = "SELECT sensor_name, location_id FROM sensor WHERE id= ?"
    cursor.execute(statement, [sensor_id])
    nombre, locacion = cursor.fetchone()
    statement = "DROP TABLE IF EXISTS "+nombre+str(locacion)+" ;"
    cursor.execute(statement)
    db.commit()
    return True

