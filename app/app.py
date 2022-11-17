from flask import Flask
import sqlite3
import controller.location.location_controller as location_controller
DATABASE_NAME = 'IoT.db'

app = Flask(__name__)

@app.route('/locations', methods=['GET'])
def get_location():
    location = location_controller.get_locations()
    return location



@app.route('/')
def hello():
    conn = sqlite3.connect(DATABASE_NAME)

    result = conn.execute("SELECT * FROM Admin")
    return result.fetchall()