from flask import request, jsonify, Flask
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller
import controller.sensor.sensor_controller as sensor_controller
DATABASE_NAME = 'IoT.db'

def init_sensor_routes(app):

    @app.route('/api/v1/create_sensor', methods = ['POST'])
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
    @app.route('/get_all_sensors', methods=['GET'])
    def get_all_sensors():
        sensors = sensor_controller.get_all_sensors()
        return jsonify(sensors), 201

    @app.route('/api/v1/get_by_id/<company_api_key>/<sensor_id>', methods = ['GET'])
    def get_sensor_by_id(company_api_key, sensor_id):
        sensor = sensor_controller.get_by_id(company_api_key, sensor_id)
        return jsonify(sensor), 201

    @app.route('/api/v1/delete_sensor/<sensor_id>', methods=['DELETE'])
    def delete_sensor(sensor_id):

        sensor = sensor_controller.delete_sensor(sensor_id)
        
        return "OK", 200    