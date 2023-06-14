from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for user login
users = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'},
    {'username': 'user3', 'password': 'pass3'}
]

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    # Check if the username and password match
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful'})
    
    # Return an error message if login fails
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/users', methods=['GET'])
def get_users():
    # Return the list of users
    return jsonify(users)

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    # Find the user with the given username
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = {
        'username': request.json['username'],
        'password': request.json['password']
    }
    
    # Add the new user to the list
    users.append(new_user)
    
    # Return the added user
    return jsonify(new_user), 201

@app.route('/api/users/<username>', methods=['PUT'])
def update_user(username):
    for user in users:
        if user['username'] == username:
            user['password'] = request.json['password']
            return jsonify(user)
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users/<username>', methods=['DELETE'])
def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)