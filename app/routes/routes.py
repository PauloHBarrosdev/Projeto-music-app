from app import app
from app.models.User import User
from flask import jsonify
from app.views.User import UserView



@app.get('/user')
def retorna_users():

    query = User.query.all()
    userview = UserView()
    response = userview.json(query)
    print(response)
    return response

@app.get('/user/<id>')
def retorna_user(id):

    query = User.query.get(id)
    userview = UserView()
    response = userview.json(query)
    print(response)
    return response

    