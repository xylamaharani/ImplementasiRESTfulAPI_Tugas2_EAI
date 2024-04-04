from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import requests
from datetime import datetime

app=Flask(__name__)

# ### CONNECT DATABASE -- database can be access from the folder
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vacay'
app.config['MYSQL_PORT'] = 3308
mysql=MySQL(app)

@app.route('/')
def root():
    return "Cari Penerbanganmu di Proyek Vacay"



@app.route('/flights_info', methods = ['GET', 'POST', 'PUT', 'DELETE'])
# ### DAFTAR PENERBANGAN -- GET method --
def flights_info():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM flights')
        column_names=[i[0] for i in cursor.description]
        data=[]
        for row in cursor.fetchall():
            data.append(dict(zip(column_names,row)))

        return jsonify(data)
        cursor.close()



# ### TAMBAH PENERBANGAN -- POST method --
    elif request.method == 'POST':
        flight_code = request.json['flight_code']
        keberangkatan = request.json['keberangkatan']
        maskapai = request.json['maskapai']
        departure = request.json['departure']
        destinasi = request.json['destinasi']
        transit = request.json['transit']

        keberangkatan_datetime = datetime.strptime(keberangkatan, '%a, %d %b %Y %H:%M:%S %Z')

        cursor = mysql.connection.cursor()
        val = (flight_code, keberangkatan_datetime, maskapai, departure, destinasi, transit)
        cursor.execute('INSERT INTO flights (flight_code, keberangkatan, maskapai, departure, destinasi, transit) VALUES (%s, %s, %s, %s, %s, %s)', val)

        mysql.connection.commit()
        return jsonify({'message': 'new flight has been successfully added'})
        cursor.close()



# ### EDIT PENERBANGAN -- PUT method --
    elif request.method == 'PUT':
        if 'id' in request.args:
            data = request.get_json()

            keberangkatan_datetime = datetime.strptime(data['keberangkatan'], '%a, %d %b %Y %H:%M:%S %Z')

            cursor = mysql.connection.cursor()
            val = (data['flight_code'], keberangkatan_datetime, data['maskapai'], data['departure'], data['destinasi'], data['transit'], request.args['id'])
            cursor.execute('UPDATE flights SET flight_code = %s, keberangkatan = %s, maskapai = %s, departure = %s, destinasi = %s, transit = %s WHERE flight_id = %s', val)

            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'flight detail has been updated'})



# ### HAPUS PENERBANGAN -- DELETE method --
    elif request.method == 'DELETE':
        if'id' in request.args:
            cursor = mysql.connection.cursor()
            val = (request.args['id'],)
            cursor.execute('DELETE FROM flights WHERE flight_id = %s',val)

            mysql.connection.commit()
            return jsonify({'message': 'flight has been deleted'})
            cursor.close()



# ### DETAIL PENERBANGAN -- GET method --
@app.route('/flights_detail', methods = ['GET'])
def flights_detail():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        val = (request.args['id'],)
        cursor.execute('SELECT * FROM flights WHERE flight_id = %s',val)
        
        column_names=[i[0] for i in cursor.description]
        data=[]
        for row in cursor.fetchall():
            data.append(dict(zip(column_names,row)))
        
        return jsonify(data)
        cursor.close()


if __name__=='__main__':
    app.run(host='0.0.0.0', port=50,debug=True)