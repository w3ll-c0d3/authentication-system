from sqlmodel import select
from models.user import User
from typing import List
import bcrypt


class UserRepository:

    def __init__(self, session) -> None:
        self.session = session 

    def find_all(self) -> List[User] | None:
        statement = select(User)
        users = self.session.exec(statement).all()
        self.session.close()
        if users:
            return users
        return None
    
    def find_by_id(self, user_id) -> User | None:
        statement = select(User).where(User.id == user_id) 
        user = self.session.exec(statement).all()
        self.session.close()
        if user:
            return user
        return None

    def save(self, user: User) -> User | None:
        new_user_id: str = user.id
        try:
            self.session.add(user)
            self.session.commit()
            self.session.close()
            return self.find_by_id(new_user_id)
        except Exception as e:
            print(__class__.__name__, e)
            self.session.close()
        return None

    def update(self, id, user_body) -> User | None:
        # Verify if user exists
        statement = select(User).where(User.id == id)
        db_user = self.session.exec(statement).all()
        if db_user: # update user fields
            db_user = db_user[0]
            if user_body.cpf != None:
                db_user.cpf = user_body.cpf
            if user_body.age != None:
                db_user.age = user_body.age
            if user_body.first_name != None:
                db_user.first_name = user_body.first_name
            if user_body.last_name != None:
                db_user.last_name = user_body.last_name
            if user_body.password != None:
                db_user.password = user_body.password
            if user_body.username != None:
                db_user.username = user_body.username

            self.session.commit()
            self.session.close()
            return self.find_by_id(id)
        else:
            return None

    def delete(self, id) -> bool | None:
        statement = select(User).where(User.id == id)
        db_user = self.session.exec(statement).all()
        if db_user:
            self.session.delete(db_user[0])
            self.session.commit()
            self.session.close()
            return True
        return None
    
    def log_in(self, credentials: dict) -> bool:
        username: str = credentials.username ; password: str = credentials.password
        user_bytes: bytes = password.encode('utf-8')

        # Verify if user exists
        statement = select(User).where(User.username == username)
        user_db = self.session.exec(statement).all()

        if user_db:
            result: bool = bcrypt.checkpw(user_bytes, user_db[0].password.encode('utf-8'))
            if result:
                return True
        return False
