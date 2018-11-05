from flask import Flask, redirect, url_for, request
import json

app = Flask(__name__)

@app.route("/echo")
def echo():
    return "El servicio FIU esta activo!"

@app.route('/registrar', methods=['POST']) 
def registrar():
    PM10 = request.form['PM10']
    PM25 = request.form['PM2.5']
    f = open("datos/datos.csv", "a")
    f.write(PM10 + ',' + PM25) 
    return PM10 + '-' + PM25

@app.route('/data/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
 
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
 
    return send_from_directory(static_file_dir, path)
