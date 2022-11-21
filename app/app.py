from flask import Flask, request
import sqlite3
import controller.company.company_controller as company_controller
import controller.location.location_controller as location_controller

DATABASE_NAME = 'IoT.db'

app = Flask(__name__)

@app.route('/locations', methods=['GET'])
def get_location():
    location = location_controller.get_locations()
    return location

@app.route('/create_company', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data['company_name']
    key = "a123s233d233"
    company = company_controller.insert_company(name, key)
    return "Success", 201

@app.route('/get_companies', methods=['GET'])
def get_all_companies():
    companies = company_controller.get_companies()
    return companies   

@app.route('/')
def hello():
    conn = sqlite3.connect(DATABASE_NAME)
    result = conn.execute("SELECT * FROM Admin")
    return result.fetchall()