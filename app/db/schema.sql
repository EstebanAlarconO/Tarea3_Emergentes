DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS sensor_data;

CREATE TABLE admin (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company_name TEXT UNIQUE NOT NULL,
  company_api_key TEXT UNIQUE NOT NULL
);

CREATE TABLE location ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company_api_key INTEGER NOT NULL,
  location_name TEXT NOT NULL,
  location_country TEXT NOT NULL,
  location_city TEXT NOT NULL,
  location_meta TEXT NOT NULL,
  FOREIGN KEY (company_api_key) REFERENCES company (company_api_key)
);

CREATE TABLE sensor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  location_id INTEGER NOT NULL,
  sensor_name TEXT NOT NULL,
  sensor_category TEXT NOT NULL,
  sensor_meta TEXT NOT NULL,
  sensor_api_key TEXT NOT NULL,
  FOREIGN KEY (location_id) REFERENCES location (id)
);

CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (sensor_id) REFERENCES sensor (id)
)