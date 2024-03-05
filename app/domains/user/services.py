from app import db
from app.common.exceptions import UserNotFoundError
from app.domains.user.models import User


class UserService:
    def create_user(self, data):
        user = User(name=data['name'], age=data['age'])
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    def get_all_users(self):
        users = User.query.all()
        return [user.to_dict() for user in users]

    def get_user_by_id(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict()

    def update_user(self, user_id, data):
        user = User.query.get(id)
        if not user:
            raise UserNotFoundError(user_id=user_id)

        if data.age is not None:
            user.age = data.age

        db.session.commit()
        return user.to_dict()

    def patch_user(self, user_id, data):
        user = User.query.get(id)
        if not user:
            raise UserNotFoundError(user_id=user_id)

        # Get the dictionary representation of the Pydantic model without unset values
        user_data = data.dict(exclude_unset=True)

        for field, value in user_data.items():
            setattr(user, field, value)

        db.session.commit()
        return user.to_dict()

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            raise UserNotFoundError(user_id=user_id)
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully'
