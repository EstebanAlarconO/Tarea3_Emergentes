from flask import Flask, request, jsonify
import sqlite3
import routes.company.company_routes as company_routes
import routes.location.location_routes as location_routes
import routes.sensor.sensor_routes as sensor_routes

DATABASE_NAME = 'IoT.db'

app = Flask(__name__)

company_routes.init_company_routes(app)
location_routes.init_location_routes(app)
sensor_routes.init_sensor_routes(app)

@app.route('/')
def hello():
    conn = sqlite3.connect(DATABASE_NAME)
    result = conn.execute("SELECT * FROM Admin")
    if len(result.fetchall()) == 0:
        conn.execute("INSERT INTO Admin (username, password) VALUES (?, ?)", ("admin", "admin"))
        result = conn.execute("SELECT * FROM Admin")
    return jsonify(result.fetchall())