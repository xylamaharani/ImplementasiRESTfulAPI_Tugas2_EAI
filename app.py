from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)


# ### CONNECT DATABASE -- database used = aiven
app.config['MYSQL_HOST'] = 'mysql-c147a8b-student-ac4a.a.aivencloud.com'
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_IARwEPGR3sTvpRQ18Gf'
app.config['MYSQL_DB'] = 'Tugas2_EAI'
app.config['MYSQL_PORT'] = 10163 
mysql = MySQL(app)



# ### Authentication Logic
valid_tokens = {"valid": "justin"}
def verify_token(token):
    return token == valid_tokens['valid']

@app.before_request
def authenticate():
    token = request.headers.get('Authorization')
    if not token or not verify_token(token):
        return jsonify({"status_code": "401","status": "error", "message": "Unauthorized", "timestamp": datetime.now()}), 401


@app.route('/')
def method_name():
    return jsonify("Search for Your Flights Here!")


# first endpoint
### DAFTAR PENERBANGAN -- GET method --
@app.route('/flights', methods=['GET'])
def get_flights():
    airline_name = request.args.get('airline_name')
    cursor = mysql.connection.cursor()
    query = '''
        SELECT flights.flight_id, flights.flight_number, airlines.airline_name, departure_airport.airport_name AS departure_airport, departure_airport.city AS departure_city, departure_airport.country AS departure_country, arrival_airport.airport_name AS arrival_airport, arrival_airport.city AS arrival_city, arrival_airport.country AS arrival_country, flights.departure_time, flights.arrival_time, flights.fare 
        FROM flights 
        INNER JOIN airports AS departure_airport ON flights.departure_airport_code = departure_airport.airport_code 
        INNER JOIN airports AS arrival_airport ON flights.arrival_airport_code = arrival_airport.airport_code 
        INNER JOIN airlines ON flights.airline_id = airlines.airline_id
    '''
    ## filter data with airline_name
    if airline_name:
        query += ' WHERE airlines.airline_name = %s'
        cursor.execute(query, (airline_name,))
    
    ## show all data
    else:
        cursor.execute(query)
    
    column_names = [i[0] for i in cursor.description]
    data = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    cursor.close()
    return jsonify({"status_code": "200", "status": "success", "message": "Data retrieved successfully", "timestamp": datetime.now(), "data": data}), 200



# second endpoint
### TAMBAH PENERBANGAN -- POST method --
@app.route('/addFlights', methods=['POST'])
def add_flight():
    data = request.json
    cursor = mysql.connection.cursor()
    query = '''INSERT INTO flights (flight_number, airline_id, departure_airport_code, arrival_airport_code, departure_time, arrival_time, fare)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
    values = (data['flight_number'], data['airline_id'], data['departure_airport_code'], data['arrival_airport_code'], data['departure_time'], data['arrival_time'], data['fare'])
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()
    return jsonify({"status_code": "201","status": "add success", "message": "Flight added successfully", "timestamp": datetime.now()}), 201



# third endpoint
### EDIT PENERBANGAN -- PUT method --
@app.route('/updateFlights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    data = request.json
    cursor = mysql.connection.cursor()
    query = '''UPDATE flights
            SET flight_number = %s, airline_id = %s, departure_airport_code = %s, arrival_airport_code = %s, departure_time = %s, arrival_time = %s, fare = %s
            WHERE flight_id = %s
            '''
    values = (data['flight_number'], data['airline_id'], data['departure_airport_code'], data['arrival_airport_code'], data['departure_time'], data['arrival_time'], data['fare'], flight_id)
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()
    return jsonify({"status_code": "200","status": "success", "message": "Flight updated successfully", "timestamp": datetime.now()}), 200



# fourth endpoint
### HAPUS PENERBANGAN -- DELETE method --
@app.route('/deleteFlights/<identifier>', methods=['DELETE'])
def delete_flight(identifier):
    cursor = mysql.connection.cursor()
    if identifier.isdigit():
        flight_id = int(identifier)
        cursor.execute('DELETE FROM flights WHERE flight_id = %s', (flight_id,))
    else:
        arrival_country = identifier
        cursor.execute('''DELETE FROM flights WHERE arrival_airport_code 
                        IN 
                        (SELECT airport_code FROM airports WHERE country = %s)''', (arrival_country,))
    
    mysql.connection.commit()
    cursor.close()
    return jsonify({"status_code": "200","status": "success", "message": "Flight(s) deleted successfully", "timestamp": datetime.now()}), 200




# fifth endpoint
### TAMBAH DATA BANDARA -- POST method --
@app.route('/addairports', methods=['POST'])
def add_airport():
    data = request.json
    airport_code = data.get('airport_code')
    airport_name = data.get('airport_name')
    city = data.get('city')
    country = data.get('country')

    if not airport_code or not airport_name or not city or not country:
        return jsonify({"status_code": "400","status": "error", "message": "Data is incomplete", "timestamp": datetime.now()}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO airports (airport_code, airport_name, city, country) VALUES (%s, %s, %s, %s)", (airport_code, airport_name, city, country))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status_code": "201","status": "add success", "message": "Airport data added successfully", "timestamp": datetime.now()}), 201




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')