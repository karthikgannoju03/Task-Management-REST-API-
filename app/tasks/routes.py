from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.tasks import tasks
from app.models import Task
from app.extensions import db
from app.tasks.schemas import TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@tasks.route("/", methods=["GET"])
@jwt_required()
def get_tasks():

    user_id = get_jwt_identity()

    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify(tasks_schema.dump(tasks))


@tasks.route("/", methods=["POST"])
@jwt_required()
def create_task():

    user_id = get_jwt_identity()
    data = request.get_json()

    task = Task(
        title=data["title"],
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task_schema.dump(task)), 201


@tasks.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):

    task = Task.query.get(id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)

    db.session.commit()

    return jsonify(task_schema.dump(task))


@tasks.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):

    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Deleted"})