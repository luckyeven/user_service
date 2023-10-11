# user_service.py

from flask import Flask, jsonify
users = {
    '1': {'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'name': 'Bob', 'email': 'bob@example.com'}
}
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<id>')
def user(id):

    user_info = users.get(id, {})
    return jsonify(user_info)
# create user
@app.route("/create_user/<id>/<name>/<email>")
def create_user(id, name, email):
    users[id] = {'name': name, 'email': email}
    return jsonify(users[id])

# update user
@app.route("/update_user/<id>/<name>/<email>")
def update_user(id, name, email):
    users[id] = {'name': name, 'email': email}
    return jsonify(users[id])

# delete user
@app.route("/delete_user/<id>")
def delete_user(id):
    if users.get(id):
        del users[id]
        return 'User deleted'
    else:
        return 'User not found'

if __name__ == '__main__':
    app.run()

