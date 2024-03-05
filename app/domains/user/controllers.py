from flask import Blueprint, request, jsonify

from app.domains.user.schemas import UserCreateSchema, UserUpdateSchema, \
    UserPatchSchema
from app.domains.user.services import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()


@user_bp.post('/')
def user_create():
    data = UserCreateSchema.parse_obj(request.get_json())
    user = user_service.create_user(data.dict())
    return jsonify(user), 201


@user_bp.get('/')
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200


@user_bp.get('/<int:user_id>')
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user), 200


@user_bp.put('/<int:user_id>')
def user_update(user_id: int):
    data = UserUpdateSchema.parse_obj(request.get_json())
    user = user_service.update_user(user_id, data)
    return jsonify(user), 200


@user_bp.patch('/<int:user_id>')
def user_patch(user_id: int):
    data = UserPatchSchema.parse_obj(request.get_json())
    user = user_service.patch_user(user_id, data)
    return jsonify(user), 200


@user_bp.delete('/<int:user_id>')
def user_delete(user_id: int):
    message = user_service.delete_user(user_id)
    return jsonify({'message': message}), 200
