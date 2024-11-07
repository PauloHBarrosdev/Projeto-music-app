from app.models.User import User
from flask import jsonify


class UserView:
    @staticmethod
    def entry(resp: User | list):
        if isinstance(resp, User):
            user_info = {
                'user_id': resp.user_id,
                'name': resp.name,
                'user_group': resp.user_group,
                'birth_date': resp.birth_date,
                'email': resp.email   
            }

            return jsonify(user_info)
        
        else:
            u_list = list()
        for resp in resp:

            user_info = {
            'user_id': resp.user_id,
            'name': resp.name,
            'user_group': resp.user_group,
            'birth_date': resp.birth_date,
            'email': resp.email,    
        }
            
            u_list.append(user_info)
        return jsonify(u_list)
        