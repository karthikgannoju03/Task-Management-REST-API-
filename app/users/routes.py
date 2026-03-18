from flask import jsonify
from app.users import users
from app.models import User

@users.route("/", methods=["GET"])
def get_users():

    users = User.query.all()

    data = []

    for u in users:
        data.append({
            "id": u.id,
            "username": u.username,
            "email": u.email
        })

    return jsonify(data)