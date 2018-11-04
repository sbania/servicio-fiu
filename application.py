from flask import Flask

app = Flask(__name__)

@app.route("/")
def echo():
    return "El servicio FIU esta activo!"

@app.route('/registrar', methods=['POST']) 
def registrar():
    if not request.json:
        abort(400)
    print (request.json)
    return json.dumps(request.json)
