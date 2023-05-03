from fastapi import FastAPI
from controllers.user_controller import router
from models.user import User
from uuid import uuid4
from connection.database import Database
from services.user_service import UserService


app = FastAPI()
app.include_router(router)


user_1 = User(
    id=uuid4(), 
    cpf='01234567890', 
    username='user_01', 
    password=UserService.hash_password('a1234567'), 
    first_name='Elon', 
    last_name='Musk',
    age='51')

with Database.connect() as session:
    try:
        session.add(user_1)
        session.commit()
    except Exception as e:
        print(f'main.py: {e}')
    finally:
        session.close()

if __name__ == '__main__':
    app.run()



