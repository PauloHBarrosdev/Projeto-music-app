from app import app
from app.models.User import User
from app.services.Users import UserService
from flask import request



@app.get('/user')
def get_users() -> dict:
    usr_service = UserService()
    return usr_service.get_user()

@app.get('/user/<id>')
def get_user(id: int) -> dict:
    usr_service = UserService()
    return usr_service.get_user(id)

@app.post('/user')
def post_user() -> dict:
    usr_service = UserService()
    print(request.get_json())
    return usr_service.post_user(request.get_json()) 
    