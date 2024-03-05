from flask import Blueprint, jsonify, request

from app.domains.posts.schemas import PostCreateSchema, PostUpdateSchema
from app.domains.posts.services import PostService

post_bp = Blueprint('post', __name__)
post_service = PostService()


@post_bp.post('/')
def add_post():
    data = PostCreateSchema.parse_obj(request.get_json())
    post = post_service.create_post(data)
    return jsonify(post), 201


@post_bp.get(rule='/')
def get_posts():
    posts = post_service.get_all_posts()
    return jsonify(posts), 200


@post_bp.get('/<int:post_id>')
def get_post_by_id(post_id):
    post = post_service.get_post_by_id(post_id)
    return jsonify(post), 200


@post_bp.put('/<int:post_id>')
def update_post(post_id):
    data = PostUpdateSchema.parse_obj(request.get_json())
    post = post_service.update_post(post_id, data)
    return jsonify(post), 200


@post_bp.delete('/<int:post_id>')
def delete_post(post_id):
    message = post_service.delete_post(post_id)
    return jsonify({'message': message}), 200
