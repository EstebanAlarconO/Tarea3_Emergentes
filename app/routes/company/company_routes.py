from flask import request, jsonify, Flask
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller
import controller.sensor.sensor_controller as sensor_controller
DATABASE_NAME = 'IoT.db'

def init_company_routes(app):
    @app.route('/api/v1/create_company', methods=['POST'])
    def create_company():
        data = request.get_json()
        name = data['company_name']
        company = company_controller.insert_company(name)
        return "Success", 201

    @app.route('/api/v1/delete_company/<company_api_key>', methods=['DELETE'])
    def delete_company(company_api_key):
        db = sqlite3.connect(DATABASE_NAME)
        cursor = db.cursor()    
        location_id = "SELECT l.id FROM location AS l, company AS c WHERE c.company_api_key = ? AND c.id = l.company_id"
        result = cursor.execute(location_id, [company_api_key]) 
        sensor = sensor_controller.delete_sensor(result)
        company_id = "SELECT id FROM company WHERE company_api_key = ?"
        result = cursor.execute(company_id, [company_api_key]) 
        location = location_controller.delete_location(result)
        company = company_controller.delete_company(company_api_key)

        return "OK", 200

    @app.route('/api/v1/get_by_key/<company_api_key>', methods=['GET'])
    def get_by_key(company_api_key):
        company = company_controller.get_by_key(company_api_key)
        return jsonify(company), 201

    @app.route('/api/v1/get_all_companies', methods=['GET'])
    def get_all_companies():
        companies = company_controller.get_companies()
        return jsonify(companies), 201