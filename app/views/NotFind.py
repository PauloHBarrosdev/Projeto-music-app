from flask import jsonify

class NotFindView:

    def UserNotFind(self, id: int | None = None ):
        if id:
            id_str = str(id)
            ret = {"message": f"Não existe um usuário com o id {id} no banco."}
        else:
            ret = {"message": "Não existem usuários cadastrados"}
        return jsonify(ret)