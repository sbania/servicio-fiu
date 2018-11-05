from flask import Flask, redirect, url_for, request
import json

app = Flask(__name__)

@app.route("/")
def echo():
    return "El servicio FIU esta activo!"

@app.route('/registrar', methods=['POST']) 
def registrar():
    PM10 = request.form['PM10']
    PM25 = request.form['PM2.5']
    f = open("datos.csv", "a")
    f.write(PM10 + ',' + PM25) 
    return PM10 + '-' + PM25
