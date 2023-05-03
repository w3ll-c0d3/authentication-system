from typing import List
from models.user import User, UserCreate, LogIn, UserUpdate
from connection.database import Database
from uuid import uuid4
from dao.user_repository import UserRepository
import bcrypt



class UserService:
    user_repository = UserRepository(Database.connect())

    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository

    @classmethod
    def get_users(cls) -> List[User]:
        users = cls.user_repository.find_all()
        return users

    @classmethod
    def get_user_by_id(cls, user_id: str) -> User:
        user = cls.user_repository.find_by_id(user_id)    
        return user

    @classmethod
    def save_user(cls, user: UserCreate) -> User:
        new_user = User(id=uuid4(), 
                        cpf=user.cpf, 
                        username=user.username, 
                        password=cls.hash_password(user.password).decode('utf-8'), 
                        first_name=user.first_name, 
                        last_name=user.last_name, 
                        age=user.age)
        user = cls.user_repository.save(new_user)
        return user

    @classmethod
    def update_user(cls, user_id: str, user_body: UserUpdate) -> User | None:
        user_body.password = cls.hash_password(user_body.password).decode('utf-8')
        user = cls.user_repository.update(user_id, user_body)
        return user

    @classmethod
    def delete_user(cls, user_id: str) -> bool:
        response = cls.user_repository.delete(user_id)
        return response

    @classmethod
    def log_in(cls, credentials: LogIn) -> bool:
        response = cls.user_repository.log_in(credentials)
        return response

    @classmethod
    def hash_password(cls, password: str) -> bytes:
        user_bytes: bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash: bytes = bcrypt.hashpw(user_bytes, salt)
        return hash
