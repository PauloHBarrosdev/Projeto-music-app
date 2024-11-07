from app import models
from app.models.User import User
from app.views.User import UserView
from app.views.NotFind import NotFindView

class UserService:
    
    @staticmethod
    def get_user(id: int | None = None) -> dict:

        if id:
            query = User.query.get(id)
        else:
            query = User.query.all()

        if query is not None:
            userview = UserView()
            response = userview.entry(query)
            return response, 200
        
        else:
            not_find = NotFindView()
            return not_find.UserNotFind(id), 401
        