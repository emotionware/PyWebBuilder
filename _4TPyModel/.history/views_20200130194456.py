import sys
import mysql
import os
import redis
 

from datetime import datetime
from flask import Flask, jsonify, request, render_template, session
from _4TPyStudioWeb import app
from _4TPyStudioWeb.code.dbexec import dbaction as ejecutor
from _4TPyStudioWeb.code.wservice import libros as libreria
 

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#show errors
app.debug = True

#Required for manage Sessions Var
app.secret_key = 'You Will Never Guess'


@app.route('/')
def hola():

    session['username']=None

    if session.get('username') is not None:
        return render_template('home.html')
    else:
        return render_template('login.html')

    #se valida el token y se indica si es válido o no o si existe o no
    
    #ejemplos a borrar después
    #sentencia="update morgan"
    #return ejecutor.exec(sentencia)

     



@app.route('/pp')
def hello_world():

    return render_template('index.html', title = "Welcome", paragraph = 'Lorem ipsum dolor sit amet')
 


@app.route('/checklogin', methods=['POST', 'GET'])
def checklogin():

    username = request.args.get('username')
    password= request.args.get('password')

    f=request.form.get('username')

    return f

    if (username=='Fer'):
        return "Si"
    else:
        return "No"
    


@app.route('/ws')
def muestralibros():
    return jsonify(libreria.books)
    
 

@app.route('/pagina')
def home():
    #se valida el token y se indica si es válido o no o si existe o no
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """ + str(session['mivar'])

@app.route('/pagina2')
def home2():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    cadena='<b> Hello, Flask! </b> on '

    return render_template("index.html",  content = cadena + formatted_now)

 

#crea nuevo token
@app.route('/creatoken', methods=['GET','POST'])
def creatoken():
    username = request.args.get('username')
    password= request.args.get('password')
    return username + " " + password

#valida si token es válido
@app.route('/validatoken', methods=['GET','POST'])
def validatoken():
    username = request.args.get('token')
    return username + " " + password

#ejecuta código SQL
@app.route('/sqlexec', methods=['GET','POST'])
def sqlexec():
    sentencia = request.args.get('sentencia')
    token= request.args.get('token')
    return username + " " + password

#hace búsquedas en tablas con el operador like
@app.route('/find', methods=['GET','POST'])
def find():
    vista = request.args.get('vista')
    termino= request.args.get('termino')
    token= request.args.get('token')
    return username + " " + password

#genera listas de autocompletado
@app.route('/autocomplete', methods=['GET','POST'])
def autocomplete():
    vista = request.args.get('vista')
    campo= request.args.get('campo')
    token= request.args.get('token')
    return username + " " + password

#edita un registro
@app.route('/editrecord', methods=['GET','POST'])
def editrecord():
    vista = request.args.get('vista')
    idobjeto= request.args.get('idobjeto')
    token= request.args.get('token')
    return username + " " + password

 




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)