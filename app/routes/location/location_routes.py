from flask import request, jsonify, Flask
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller
import controller.sensor.sensor_controller as sensor_controller
DATABASE_NAME = 'IoT.db'
app = Flask(__name__)

@app.route('/api/v1/locations', methods=['GET'])
def get_location():
    location = location_controller.get_locations()
    return location   

@app.route('/api/v1/add_location', methods=['POST'])
def create_location():
    data = request.get_json()
    company_id, name, country, city, meta = data['company_id'], data['location_name'], data['location_country'], data['location_city'], data['location_meta']
    location = location_controller.insert_locations(company_id, name, country, city, meta)
    return jsonify(location), 201

@app.route('/api/v1/delete_location/<id>', methods=['DELETE'])
def delete_location(id):
    db = sqlite3.connect(DATABASE_NAME)
    cursor = db.cursor()    
    sensor_id = "SELECT s.id FROM location AS l, sensor AS s WHERE l.id = ? AND l.id = s.location_id"
    result = jsonify(cursor.execute(sensor_id, [id])) 
    sensor = sensor_controller.delete_sensor(result)
    location = location_controller.delete_location(id)

    return "OK", 200           

@app.route('/api/v1/update_location/<id>', methods=['PUT'])
def update_location(id):
    data = request.get_json()
    
    location = location_controller.update_location(data["location_name"], data["location_country"], data["location_city"], data["location_meta"], id)

    return "OK", 200    