from app.models.User import User, UserSchema
from flask import jsonify, json


class UserView:

    @staticmethod
    def dump_json(resp: User | list):
        if isinstance(resp, User):
            user_info = UserSchema()
            return jsonify(user_info.dump(resp))
        
        else:
            u_list = list()
            for object in resp:
                print(object)
                user_info = UserSchema()
                u_list.append(user_info.dump(object))
            return jsonify(u_list)
    
    @staticmethod
    def load_json(user: json):
        usr = UserSchema.load(user)
        return User(usr)
            