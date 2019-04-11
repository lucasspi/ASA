from flask import Flask, url_for, request, json, jsonify
from user import User
from json import dumps
#from bottle import response

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

@app.route('/hello')
def api_hello(): #http://127.0.0.1:5000/hello?name=Luis
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/createuser')
def api_createuser():
    global myUser
    myUser.append(User(1, "Joao", 12, "São Paulo"))
    myUser.append(User(2, "Pedro",  13, "São Tomé"))
    myUser.append(User(3, "Jorge",  14, "São Bernardo"))
    myUser.append(User(4, "Valdir",  11, "São Roque"))
    myUser.append(User(5, "Antonio",  10, "São Cristóvão"))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/getuser', methods = ['GET'])
def api_getuser():
    global myUser
    user_data = request.get_json() # 
    print(user_data)
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    res = {'status': 'usuario nao encontrado'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            res = {'nome': elem.getUserNome()}
        
    return jsonify(res)

@app.route('/adduser', methods = ['POST'])
def api_newuser():
    global myUser
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_user = User(id, nome, idade, cidade)
    myUser.append(new_user)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/listusers', methods = ['GET'])
def api_listusers():
    payload = []
    content = {}
    
    for elem in myUser:        
        content = {'id': str(elem.getUserId()),'[nome]': elem.getUserNome(), 
        '[idade]': str(elem.getUserIdade()), '[cidade]': elem.getUserCidade()}
        payload.append(content)
        content = {}

    res =  json.dumps(payload)       
    
    return jsonify(UserList=res)

if __name__ == '__main__':
    app.run()