from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

#initialize firebase application
cred = credentials.Certificate('firestore-new.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


# Firestore collection reference for users
users_ref = db.collection('users')

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    # Query Firestore to find the user with the given username
    query = users_ref.where('username', '==', username).limit(1)
    users = query.get()

    # Check if the user exists and the password matches
    for user in users:
        user_data = user.to_dict()
        if user_data['password'] == password:
            return jsonify({'message': 'Login successful'})
    
    # Return an error message if login fails
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/users', methods=['GET'])
def get_users():
    # Query all users from Firestore
    users = users_ref.get()

    # Convert Firestore user documents to a list of dictionaries
    user_list = []
    for user in users:
        user_data = user.to_dict()
        user_list.append(user_data)

    # Return the list of users
    return jsonify(user_list)

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    # Query Firestore to find the user with the given username
    query = users_ref.where('username', '==', username).limit(1)
    users = query.get()

    # Check if the user exists
    for user in users:
        user_data = user.to_dict()
        return jsonify(user_data)
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = {
        'username': request.json['username'],
        'password': request.json['password']
    }
    
    # Add the new user to Firestore
    users_ref.add(new_user)
    
    # Return the added user
    return jsonify(new_user), 201

@app.route('/api/users/<username>', methods=['PUT'])
def update_user(username):
    # Query Firestore to find the user with the given username
    query = users_ref.where('username', '==', username).limit(1)
    users = query.get()

    # Check if the user exists
    for user in users:
        user_ref = user.reference
        user_ref.update({'password': request.json['password']})
        updated_user = user.to_dict()
        return jsonify(updated_user)
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users/<username>', methods=['DELETE'])
def delete_user(username):
    # Query Firestore to find the user with the given username
    query = users_ref.where('username', '==', username).limit(1)
    users = query.get()

    # Check if the user exists
    for user in users:
        user_ref = user.reference
        user_ref.delete()
        return jsonify({'message': 'User deleted'})
    
    # Return an error message if the user is not found
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)