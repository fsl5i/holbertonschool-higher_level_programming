#!/usr/bin/python3
"""
task_04_flask.py
Simple API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (DO NOT prefill with test data)
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint
    """
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """
    Status endpoint
    """
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Return a list of all usernames
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return user data for a given username
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user via POST request
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
