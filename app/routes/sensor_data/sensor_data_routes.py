from flask import request, jsonify, Flask
import sqlite3
import controller.sensor_data.sensor_data_controller as sensor_data_controller
import controller.sensor.sensor_controller as sensor_controller
import json

DATABASE_NAME = 'IoT.db'

def init_sensor_data_routes(app):

    @app.route('/api/v1/sensor_data', methods = ['POST'])
    def insert_sensor_data():
        data = request.get_json()
        sensor_data = sensor_data_controller.insert_sensor_data(data['sensor_api_key'], data['json_data'])
        return "Success", 201

    @app.route('/api/v1/sensor_data', methods = ['GET'])
    def get_sensor_data():
        sensores = sensor_controller.get_all_sensors(request.args.get('company_api_key'))
        sensores_data = []
        for i in sensores:
            if(i[0] in json.loads(request.args.get('sensor_id'))):
                query = sensor_data_controller.get_sensor_data(i[5], request.args.get('from'), request.args.get('to'))
                sensores_data.append(query)
        return jsonify(sensores_data)