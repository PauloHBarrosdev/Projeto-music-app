from app import app
from app.models.User import User
from flask import jsonify
from app.views.User import UserView
from app.services.Users import UserService



@app.get('/user')
def retorna_users() -> dict:
    usr_service = UserService()
    return usr_service.get_user()

@app.get('/user/<id>')
def retorna_user(id: int) -> dict:
    usr_service = UserService()
    return usr_service.get_user(id)

@app.post('/user')
def cria_user(user_list: list[User]) -> dict:
    usr_service = UserService()
    return usr_service.get_user()
    