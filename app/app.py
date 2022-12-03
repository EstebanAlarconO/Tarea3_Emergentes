from flask import Flask, request, jsonify
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller

DATABASE_NAME = 'IoT.db'

app = Flask(__name__)


@app.route('/create_company', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data['company_name']
    key = "a123s233d233"
    company = company_controller.insert_company(name, key)
    return "Success", 201

@app.route('/delete_company/<company_api_key>', methods=['DELETE'])
def delete_company(company_api_key):
    
    company = company_controller.delete_company(company_api_key)
    
    return "OK", 200

@app.route('/get_by_name', methods=['GET'])
def get_by_name():
    data = request.get_json()
    name = data['company_name']
    companie = company_controller.get_by_name(name)
    return jsonify(companie), 201

@app.route('/get_all_companies', methods=['GET'])
def get_all_companies():
    companies = company_controller.get_companies()
    return companies

@app.route('/locations', methods=['GET'])
def get_location():
    location = location_controller.get_locations()
    return location

@app.route('/add_location/<company_api_key>', methods=['POST'])
def create_location(company_api_key):
    data = request.get_json()
    name, country, city, meta = data['location_name'], data['location_country'], data['location_city'], data['location_meta']
    location = location_controller.insert_locations(company_api_key, name, country, city, meta)
    return jsonify(location), 201           

@app.route('/')
def hello():
    conn = sqlite3.connect(DATABASE_NAME)
    result = conn.execute("SELECT * FROM Admin")
    if len(result.fetchall()) == 0:
        conn.execute("INSERT INTO Admin (username, password) VALUES (?, ?)", ("admin", "admin"))
        result = conn.execute("SELECT * FROM Admin")
    return result.fetchall()