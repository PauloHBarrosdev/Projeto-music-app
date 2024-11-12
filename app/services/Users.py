from app.models.User import User
from app.views.User import UserView
from app.views.NotFind import NotFindView
from app.views.Success import SuccesView
from flask import json
from app import db

class UserService:
    
    @staticmethod
    def get_user(id: int | None = None) -> dict:

        if id:
            query = User.query.get(id)
        else:
            query = User.query.all()

        if query is not None:
            response = UserView.dump_json(query)
            return response, 200
        
        else:
            not_find = NotFindView()
            return not_find.UserNotFind(id), 401
        
    @staticmethod
    def post_user(user_list: json):
        usr_view = UserView()
        for usr in user_list:
            new_user = usr_view.load_json(usr)
            db.session.add(new_user)
        return SuccesView.post_user()

        
        