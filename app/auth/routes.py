from flask import request, jsonify
from app.auth import auth
from app.models import User
from app.extensions import db
from app.auth.utils import generate_token

@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    user = User(
        username=data["username"],
        email=data["email"]
    )

    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"}), 201


@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):

        token = generate_token(user.id)

        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401