from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def echo():
    return "El servicio FIU esta activo!"

@app.route('/registrar', methods=['POST']) 
def registrar():
    print (request.json)
    return json.dumps(request.json)
