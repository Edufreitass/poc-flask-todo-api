from app import db
from app.domains.posts.models import Post


class PostService:
    def create_post(self, data):
        new_post = Post(
            title=data.title,
            body=data.body,
            user_id=data.user_id
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post.to_dict()

    def get_all_posts(self):
        posts = Post.query.all()
        return [post.to_dict() for post in posts]

    def get_post_by_id(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post.to_dict()

    def update_post(self, post_id, data):
        post = Post.query.get(post_id)
        if not post:
            raise ValueError(f'Post with id {post_id} not found')

        # Atualiza os campos se eles existirem no esquema de atualização
        if data.title is not None:
            post.title = data.title
        if data.body is not None:
            post.body = data.body
        if data.user_id is not None:
            post.user_id = data.user_id

        db.session.commit()
        return post.to_dict()

    def delete_post(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            raise ValueError(f'Post with id {post_id} not found')
        db.session.delete(post)
        db.session.commit()
        return 'Post deleted successfully'
