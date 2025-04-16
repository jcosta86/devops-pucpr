from typing import List, Optional
from app.models import User, UserCreate

fake_db: List[User] = []
id_counter = 1

def create_user(user_create: UserCreate) -> User:
    global id_counter
    user = User(id=id_counter, **user_create.dict())
    fake_db.append(user)
    id_counter += 1
    return user

def get_user(user_id: int) -> Optional[User]:
    return next((user for user in fake_db if user.id == user_id), None)

def list_users() -> List[User]:
    return fake_db

def update_user(user_id: int, user_data: UserCreate) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.name = user_data.name
        user.email = user_data.email
        return user
    return None

def delete_user(user_id: int) -> bool:
    global fake_db
    user = get_user(user_id)
    if user:
        fake_db = [u for u in fake_db if u.id != user_id]
        return True
    return False
