from flask import request, jsonify, Flask
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller
import controller.sensor.sensor_controller as sensor_controller
import json
DATABASE_NAME = 'IoT.db'

def init_company_routes(app):
    @app.route('/api/v1/create_company', methods=['POST'])
    def create_company():
        data = request.get_json()
        name = data['company_name']
        company = company_controller.insert_company(name)
        return "Success", 201

    @app.route('/api/v1/delete_company/<id>', methods=['DELETE'])
    def delete_company(id):
        company = company_controller.delete_company(id)

        return "OK", 200

    @app.route('/api/v1/get_by_key/<company_api_key>', methods=['GET'])
    def get_by_key(company_api_key):
        company = company_controller.get_by_key(company_api_key)
        return jsonify(company), 201

    @app.route('/api/v1/get_all_companies', methods=['GET'])
    def get_all_companies():
        companies = company_controller.get_companies()
        return jsonify(companies), 201