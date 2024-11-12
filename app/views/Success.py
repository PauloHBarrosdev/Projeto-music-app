from flask import jsonify

class SuccesView:
    
    @staticmethod
    def post_user():
        return jsonify({"message", "usuário(s) criado(s) com sucesso"}), 200