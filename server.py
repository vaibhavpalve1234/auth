from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['get'])
def server():
    return jsonify({'status': 'success', 'message': 'Dashboard loagin route'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')
    role = data.get('role')
    password = data.get('password')

    # Send a request to the Node.js server to check the credentials against the database
    node_response = requests.post('http://node-server:3000/register', json={'name':name, 'email':email, 'password':password, 'address':address, "role":role})

    # If the credentials are valid, return a success message
    if node_response.json()['status'] == 'success':
        return jsonify({'status': 'success', 'message': 'Login successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Send a request to the Node.js server to check the credentials against the database
    node_response = requests.post('http://node-server:3000/login', json={'email': email, 'password': password})

    # If the credentials are valid, return a success message
    if node_response.json()['status'] == 'success':
        return jsonify({'status': 'success', 'message': 'Login successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

if __name__ == '__main__':
    print('server started ')
    app.run()