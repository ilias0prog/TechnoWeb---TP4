from app.database import bookstore
from app.schemas.user import UserSchema


def get_user_by_username(username: str):
    for user in bookstore['users']:
        if user['username'] == username:
            return UserSchema.model_validate(user)
    return None


def get_user_by_id(id: str):
    for user in bookstore['users']:
        if user['id'] == id:
            return UserSchema.model_validate(user)
    return None
