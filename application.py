from flask import Flask, redirect, url_for, request, send_from_directory
import json
import os
import datetime

app = Flask(__name__)

@app.route("/")
def echo():
    return "El servicio FIU esta activo!"

@app.route('/registrar', methods=['POST']) 
def registrar():
    t = datetime.datetime.utcnow()
    PM10 = request.form['PM10']
    PM25 = request.form['PM25']
    f = open("datos/datos.csv", "a")
    f.write(str(t) + ',' + PM25 + ',' + PM10 + '\n') 
    return str(t) + '-' + PM25 + '-' + PM10

@app.route("/reiniciar")
def reiniciar():
    f = open("datos/datos.csv", "w")
    f.write('Time' + ',' + 'PM2.5' + ',' + 'PM10' + '\n') 
    return "Los datos fueron eliminados"

@app.route('/datos/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
     if not os.path.isfile(os.path.join('datos', path)):
        path = os.path.join(path, 'index.html')
        return send_from_directory('datos', path)
