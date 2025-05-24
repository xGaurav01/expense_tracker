from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_user_by_id, get_all_users, delete_user, get_user_by_email
from middleware.auth import generate_token, login_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def api_register():
    data = request.get_json()
    user_id = create_user(data['name'], data['email'], data['password'])
    return jsonify({"message": "User registered", "user_id": user_id}), 200

@user_bp.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    user = get_user_by_email(data['email'])
    
    if user and user['password'] == data['password']:  # access as dict keys
        token = generate_token(user['id'])
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401



@user_bp.route('/me', methods=['GET'])
@login_required
def api_get_profile():
    user = get_user_by_id(request.user_id)
    return jsonify({"user": user})

@user_bp.route('/users', methods=['GET'])
def api_get_all_users():
    users = get_all_users()
    return jsonify({"users": users})

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    deleted = delete_user(user_id)
    if deleted:
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404
