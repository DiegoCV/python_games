from flask import Flask, request, abort, jsonify, make_response
#from flask_cors import CORS


app = Flask(__name__)
#CORS(app, supports_credentials=True)

def mi_validar():
    return 1

@app.route('/', methods=['GET'])
def index():
    return 500

@app.route('/test', methods=['GET'])
def superTest():
    return 'SuperTEst'

@app.route('/validarPersona', methods=['GET'])
def mmm():
    if(validarPersona(request.args['persona'])):
        return 'correcto'
    else:
        return 'incorrecto'

def validarPersona(persona):
    return persona == 'admin'

@app.route('/jjj/lo', methods=['GET'])
def registrarVendedor():
    if mi_validar():
        #Aqui deberia ir el llamado al controlador
        return reponder()
    else:
        return responderError()

@app.route('/fer/dsf', methods=['POST'])
def verificarVendedor(vendedor):
    if login(vendedor):
        usuario = {'codigo':vendedor['codigo'],'id':'01'}
        return reponderLogin(usuario)
    else:
        return responderError()

"""////////////////////////////////////////////////////
   ///////////////////////////////////////////////////
"""
@app.route('/grgrd/df', methods=['POST'])
def agendar_sesiones(usuario,sesion):
    if insertarSesion(sesion):
        #Aqui deberia ir el llamado al controlador
        return reponderTEST(usuario,sesion)
    else:
        return responderError()

"""////////////////////////////////////////////////////
   ///////////////////////////////////////////////////
"""





#Metodo ficticio, hay que reemplazar por el cintrolador
def insertarSesion(sesiones):
    return 1

def login(user):
    if user['codigo'] == 'admin' and user['pass'] == 'admin':
        return 1
    return 0

#app.run(host='192.168.1.35')

if __name__ == "__main__":
    app.run()
