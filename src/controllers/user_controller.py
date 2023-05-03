from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from models.user import UserCreate, LogIn, UserUpdate

router = APIRouter(
    prefix = '/users',
    tags = ['users']
)
class UserController:

    @router.get('/', status_code=200)
    def get_users():
        response = UserService.get_users()
        if response:
            return response
        raise HTTPException(
            status_code=404,
            detail=f'Users not found.'
        )

    @router.get('/{user_id}', status_code=200)
    def get_user_by_id(user_id: str):
        response = UserService.get_user_by_id(user_id)
        if response:
            return response
        raise HTTPException(
            status_code=404,
            detail=f'User with id: {user_id} not found.'
        )

    @router.post('/', status_code=201)
    def save_user(user: UserCreate):
        response = UserService.save_user(user)
        if response:
            return response
        raise HTTPException(
            status_code=400,
            detail='Bad request.'
        ) 

    @router.post('/auth', status_code=200)
    def log_in(credentials: LogIn):
        response = UserService.log_in(credentials)
        if response:
            return {"Access granted."}
        raise HTTPException(
            status_code=401,
            detail='Unauthorized.'  
        ) 

    @router.put('/{user_id}', status_code=200)
    def update_user(user_id: str, user_body: UserUpdate):
        response = UserService.update_user(user_id, user_body)
        if response:
            return response
        raise HTTPException(
            status=400,
            detail='Bad request.'
        )

    @router.delete('/{user_id}', status_code=200)
    def delete_user(user_id: str):
        response = UserService.delete_user(user_id)
        if response:
            return {f"User with id {user_id} deleted."}
        raise HTTPException(
            status_code=404,
            detail=f'User with id: {user_id} not found.'
        )
