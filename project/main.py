from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .models import db, User, Task, SubTask, SubSubTask

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([task.to_dict() for task in tasks])

@main.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.json
    new_task = Task(title=data['title'], user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@main.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task or task.user_id != current_user.id:
        return jsonify({"error": "Task not found"}), 404
    data = request.json
    task.title = data['title']
    db.session.commit()
    return jsonify(task.to_dict())

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task or task.user_id != current_user.id:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})


# Routes for SubTasks
@main.route('/tasks/<int:task_id>/subtasks', methods=['GET'])
@login_required
def get_subtasks(task_id):
    subtasks = SubTask.query.filter_by(task_id=task_id).all()
    return jsonify([subtask.to_dict() for subtask in subtasks])

@main.route('/tasks/<int:task_id>/subtasks', methods=['POST'])
@login_required
def create_subtask(task_id):
    data = request.json
    new_subtask = SubTask(title=data['title'], task_id=task_id)
    db.session.add(new_subtask)
    db.session.commit()
    return jsonify(new_subtask.to_dict()), 201

# Routes for SubSubTasks
@main.route('/subtasks/<int:subtask_id>/subsubtasks', methods=['GET'])
@login_required
def get_subsubtasks(subtask_id):
    subsubtasks = SubSubTask.query.filter_by(subtask_id=subtask_id).all()
    return jsonify([subsubtask.to_dict() for subsubtask in subsubtasks])

@main.route('/subtasks/<int:subtask_id>/subsubtasks', methods=['POST'])
@login_required
def create_subsubtask(subtask_id):
    data = request.json
    new_subsubtask = SubSubTask(title=data['title'], subtask_id=subsubtask_id)
    db.session.add(new_subsubtask)
    db.session.commit()
    return jsonify(new_subsubtask.to_dict()), 201

# ... [rest of the code]
