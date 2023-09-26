# user_service.py

from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file into the application's environment
load_dotenv()

app = Flask(__name__)

# Access the FLASK_APP environment variable
flask_app = os.environ.get("FLASK_APP")

# You can now use the FLASK_APP variable in your Flask application
print(f"FLASK_APP: {flask_app}")


@app.route("/")
def home():
    return "User Service is live!"


@app.route('/user/<id>')
def user(id):
    users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
    }
    user_info = users.get(id, {})
    return jsonify(user_info)


if __name__ == '__main__':
    app.run(port=5000)

