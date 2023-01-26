from flask import Flask, request, jsonify, json
from gevent.pywsgi import WSGIServer
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        print('hello world')
        return jsonify({'data': data})

@app.route('/register', methods=['POST'])
def add_user():
    print("we here")
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')
    role = data.get('role')
    password = data.get('password')
    headers = {"Content-type": "application/json"}
    r = requests.post('http://localhost:8080/register', json={'name':name, 'email':email, 'password':password, 'address':address, "role":role}, headers=headers)
    node_response = json.loads(r.text)
    if node_response['token']:
        return jsonify({'status': 'success', 'message': node_response})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    headers = {"Content-type": "application/json"}
    r = requests.post('http://localhost:8080/login', json={'email': email, 'password': password}, headers=headers)
    node_response = json.loads(r.text)
    if node_response['token']:
        return jsonify({'status': 'success', 'message': node_response})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    print('server started at 5000 ')