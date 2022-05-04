import flask
from flask import request

app = flask.Flask(__name__)
users = [
    {
        'id': 1,
        'name':'Mike',
        'Surname':'xz1',
        'email':'ghfhgfjhfgj@gmail.com',
        'password':'qwety1'

    },
    {
        'id': 2,
        'name':'Brad',
        'Surname':'xz2',
        'email':'hgfhgfhfgha@gmail.com',
        'password':'qwety2'

    },
    {
        'id': 3,
        'name':'Sanya',
        'Surname':'xz3',
        'email':'gfgdgh@gmail.com',
        'password':'qwery3'

    },
]

@app.route('/')
def index():
	return 'OK!'

@app.route('/users', methods=['GET'])
def get_users():
	return flask.jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
        data = request.json
        if 'id' in data and 'name' in data and 'Surname' in data and 'email' in data and 'password' in data:
            email = data['email']
            if len(list(filter(lambda x: x['email'] == email, users))) != 0:
                return flask.jsonify({
                    'code': 2,
                    'message': 'Пользователь уже есть в системе'
                })
            users.append(data)
            return flask.jsonify({
                'code': 0,
                'message': 'User created'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У пользователя есть обязательные поля: username, password, email'
        })


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id: int):
	global users
	index_for_delete = None
	for idx, user in enumerate(users):
		if user['id'] == id:
			index_for_delete = idx
			break
	if index_for_delete is not None:
		del users[index_for_delete]
		return 'Успешно удалено'
	else:
		return '<p style="color:red;">User not found</p>'


if __name__ == '__main__':
  app.run('localhost', 6000)