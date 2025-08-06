
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {
    1: {"id": 1, "name": "rohee"},
    2: {"id": 2, "name": "Anjali"}
    }

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    user_id = max(users.keys()) + 1 if users else 1
    user = {"id": user_id, "name": data['name']}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    user['name'] = data['name']
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'result': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)