from flask import Flask, request, jsonify
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller
import controller.sensor.sensor_controller as sensor_controller

DATABASE_NAME = 'IoT.db'

app = Flask(__name__)


@app.route('/api/v1/create_company', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data['company_name']
    company = company_controller.insert_company(name)
    return "Success", 201

@app.route('/api/v1/delete_company/<company_api_key>', methods=['DELETE'])
def delete_company(company_api_key):
    company = company_controller.delete_company(company_api_key)
    location = location_controller.delete_location(company_api_key)
    
    return "OK", 200

@app.route('/api/v1/get_by_key/<company_api_key>', methods=['GET'])
def get_by_key(company_api_key):
    company = company_controller.get_by_key(company_api_key)
    return jsonify(company), 201

@app.route('/api/v1/get_all_companies', methods=['GET'])
def get_all_companies():
    companies = company_controller.get_companies()
    return jsonify(companies), 201

@app.route('/create_sensor', methods = ['POST'])
def create_sensor():
    data = request.get_json()
    location_id = data['location_id']
    name = data['sensor_name']
    category = data['sensor_category']
    meta = data['sensor_meta']
    sensor = sensor_controller.insert_sensor(location_id, name, category, meta)
    return "Success", 201

@app.route('/api/v1/update_sensor/<id>', methods=['PUT'])
def update_sensor(id):
    sensor_info = sensor_controller.get_by_id(id)
    data = request.get_json()
    if(sensor_info[1] != data['location_id']):
        sensor_info[1] = data['location_id']
    if(sensor_info[2] != data['sensor_name']):
        sensor_info[2] = data['sensor_name']
    if(sensor_info[3] != data['sensor_category']):
        sensor_info[3] = data['sensor_category']
    if(sensor_info[4] != data['sensor_meta']):
        sensor_info[4] = data['sensor_meta']
    
    sensor = sensor_controller.update_sensor(id, sensor_info[1], sensor_info[2], sensor_info[3], sensor_info[4])
    return "Success", 201
@app.route('/delete_sensor', methods=['DELETE'])
def delete_sensor(sensor_api_key):

    sensor = sensor_controller.delete_sensor(sensor_api_key)
    
    return "OK", 200

@app.route('/get_all_sensors', methods=['GET'])
def get_all_sensors():
    sensors = sensor_controller.get_sensors()
    return jsonify(sensors), 201


@app.route('/api/v1/locations', methods=['GET'])
def get_location():
    location = location_controller.get_locations()
    return location   

@app.route('/api/v1/add_location/<company_api_key>', methods=['POST'])
def create_location(company_api_key):
    data = request.get_json()
    name, country, city, meta = data['location_name'], data['location_country'], data['location_city'], data['location_meta']
    location = location_controller.insert_locations(name, country, city, meta, company_api_key)
    return jsonify(location), 201

@app.route('/api/v1/delete_location/<company_api_key>', methods=['DELETE'])
def delete_location(company_api_key):

    location = location_controller.delete_location(company_api_key)

    return "OK", 200           

@app.route('/')
def hello():
    conn = sqlite3.connect(DATABASE_NAME)
    result = conn.execute("SELECT * FROM Admin")
    if len(result.fetchall()) == 0:
        conn.execute("INSERT INTO Admin (username, password) VALUES (?, ?)", ("admin", "admin"))
        result = conn.execute("SELECT * FROM Admin")
    return result.fetchall()