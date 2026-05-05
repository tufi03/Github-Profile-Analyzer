from flask import Blueprint, jsonify, render_template
from app.services import fetch_user, get_users

api = Blueprint("api", __name__)

@api.route("/fetch_user/<username>")
def fetch_user_route(username):
    data, status = fetch_user(username)
    return jsonify(data), status

@api.route("/users")
def users():
    return jsonify(get_users())

