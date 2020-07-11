import mysql.connector
import os
import json
import re
import dis
import uuid

from flask import Flask, request, jsonify, render_template, session
from flask.json import JSONEncoder

# Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE

from _4TPyModel.code.dbexec import dbexecutor

# String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx
from _4TPyModel.code.dbstring import GMTZone

from _4TPyModel.views import app


def populatearray(tablename, CAMPODISPLAY_startsWith, campofiltro, idobjetofiltro):
    # Get population sentence for this table
    populationsentence = givemepopulationsentence(tablename)

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    if campofiltro != 'null' and idobjetofiltro != 'null':
        laorden = "select * from (" + populationsentence + ") as Q where " + str(campofiltro) + "='" + str(
            idobjetofiltro) + "' "
        print(laorden)
        mycursor.execute(laorden)

    if CAMPODISPLAY_startsWith != '':
        laorden2 = "select ID" + tablename[
                                 3:] + ",concat(' ',CAMPODISPLAY) as CAMPODISPLAY  from (" + populationsentence + " ) as R WHERE CAMPODISPLAY LIKE '%" + CAMPODISPLAY_startsWith + "%' LIMIT 25"
        # print (laorden2 + '_____________________________________________________________________________________________')
        mycursor.execute(laorden2)

    if CAMPODISPLAY_startsWith == '' and campofiltro == 'null':
        mycursor.execute(populationsentence)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    return jsonify(json_data)


def populatexlsx(tablename, CAMPODISPLAY_startsWith, campofiltro, idobjetofiltro):
    # Get population sentence for this table
    populationsentence = givemepopulationsentence(tablename)

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    if campofiltro != 'null' and idobjetofiltro != 'null':
        laorden = "select * from (" + populationsentence + ") as Q where " + str(campofiltro) + "='" + str(
            idobjetofiltro) + "' "
        print(laorden)
        mycursor.execute(laorden)

    if CAMPODISPLAY_startsWith != '':
        laorden2 = "select ID" + tablename[
                                 3:] + ",concat(' ',CAMPODISPLAY) as CAMPODISPLAY  from (" + populationsentence + " ) as R WHERE CAMPODISPLAY LIKE '%" + CAMPODISPLAY_startsWith + "%' LIMIT 25"
        # print (laorden2 + '_____________________________________________________________________________________________')
        mycursor.execute(laorden2)

    if CAMPODISPLAY_startsWith == '' and campofiltro == 'null':
        mycursor.execute(populationsentence)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []

    for result in myresult:
        print(result)
        json_data.append(result)

    return json_data


def crearfiltrodemando(usuario):
    A = A


def populatepropiedad(tablename, idusername, tipouser, esadmin, idobjeto):
    campollave = ('ID' + tablename.replace('tbl', '')).upper()
    colafinal = "  and T1." + campollave + "=" + idobjeto
    # print(tipouser + 'TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER ')

    propiedad = ''

    if tipouser == '1':
        propiedad = ' WHERE T1.PROPIETARIO=' + idusername + colafinal

    if tipouser == '2':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select AGENTE from view_esquema_grupos WHERE SUPERVISOR=' + idusername + ' )' + colafinal

    if tipouser == '3':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select agente from view_esquema_grupos WHERE supervisor in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ') ) or t1.PROPIETARIO in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ' )' + colafinal

    # si el usuario es admin se quitan los filtro de propiedad
    if esadmin == '1' or 'view' in tablename:
        propiedad = ''

    # filtrodemando=crearfiltromando(usuario)

    # print(propiedad + 'PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD ')

    # Get population sentence for this table
    populationsentence = givemepopulationsentence(tablename)

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    laordenes = 'select count(*) as total from (' + populationsentence + ') t1 ' + propiedad
    # return laordenes

    print(laordenes + 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    mycursor.execute(laordenes)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    return str(campos[0])


def populate(tablename, CAMPODISPLAY_startsWith, campofiltro, idobjetofiltro, usuario, idusername, tipouser, esadmin):
    # print(tipouser + 'TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER TIPOUSER ')

    propiedad = ''

    if tipouser == '1':
        propiedad = ' WHERE T1.PROPIETARIO=' + idusername

    if tipouser == '2':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select AGENTE from view_esquema_grupos WHERE SUPERVISOR=' + idusername + ' )'

    if tipouser == '3':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select agente from view_esquema_grupos WHERE supervisor in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ') ) or t1.PROPIETARIO in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ' )'

    # si el usuario es admin se quitan los filtro de propiedad
    if esadmin == '1' or 'view' in tablename:
        propiedad = ''

    # filtrodemando=crearfiltromando(usuario)

    # print(propiedad + 'PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD PROPIEDAD ')

    # Get population sentence for this table
    populationsentence = givemepopulationsentence(tablename)

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    if campofiltro != 'null' and idobjetofiltro != 'null':
        laorden = "select * from (      select * from (" + populationsentence + ") as Q where " + str(
            campofiltro) + "='" + str(idobjetofiltro) + "'     ) t1  " + propiedad
        print(laorden)
        mycursor.execute(laorden)

    if CAMPODISPLAY_startsWith != '':
        laorden2 = "select * from (    select ID" + tablename[
                                                    3:] + ",concat(' ',CAMPODISPLAY) as CAMPODISPLAY  from (" + populationsentence + " ) as R WHERE CAMPODISPLAY LIKE '%" + CAMPODISPLAY_startsWith + "%' LIMIT 25   ) t1 " + propiedad
        print(
            laorden2 + ' ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp ')
        mycursor.execute(laorden2)

    if CAMPODISPLAY_startsWith == '' and campofiltro == 'null':
        print('select * from (' + populationsentence + ') t1 ' + propiedad)
        mycursor.execute('select * from (' + populationsentence + ') t1 ' + propiedad)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    return jsonify(json_data)


def agendadatos(campofiltro, idobjetofiltro):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    ejecutado = 0

    if campofiltro != None and campofiltro != '' and campofiltro != 'null':
        ejecutado = 1
        orden = "select * from tblagenda where " + campofiltro + "='" + str(idobjetofiltro) + "';"
        print(orden)
        mycursor.execute(orden)

    if ejecutado == 0:
        mycursor.execute("select * from tblagenda")

    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    return jsonify(json_data)


def volcadovista(tabla, idobjeto):
    return tabla + idobjeto

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    laorden = "select *  from view_notify_report_" + tabla + " where ID" + tabla.replace("tbl",
                                                                                         "") + " = '" + idobjeto + "'"
    # print(laorden + '****************************************************************************************************************')
    return laorden
    mycursor.execute(laorden)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    data = []
    for result in myresult:
        data.append(dict(zip(field_names, result)))

    return data



def populatequery(query):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    mycursor.execute("select *  from " + query)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    resultado = jsonify(json_data)

    return resultado
def populatequery2(query,cwhere):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    laorden="select *  from " + query + cwhere
    print(laorden)

    mycursor.execute(laorden)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    resultado = jsonify(json_data)

    return resultado


def buscadorarray(query):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    print(query + "????????????????????????????????????????????????????????????????????????")
    mycursor.execute(query)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    return jsonify(json_data)


def buscadorxlsx(query):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    print(query + "????????????????????????????????????????????????????????????????????????")
    mycursor.execute(query)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(result)

    return json_data


#    for x in myresult:
#        print(x)


def buscador(query, usuario, idusername, tipouser, esadmin):
    propiedad = ''

    if tipouser == '1':
        propiedad = ' WHERE T1.PROPIETARIO=' + idusername

    if tipouser == '2':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select AGENTE from view_esquema_grupos WHERE SUPERVISOR=' + idusername + ' )'

    if tipouser == '3':
        propiedad = ' where t1.PROPIETARIO=' + idusername + ' or t1.PROPIETARIO in (select agente from view_esquema_grupos WHERE supervisor in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ') ) or t1.PROPIETARIO in (select supervisor from view_esquema_grupos WHERE gerente=' + idusername + ' )'

    # si el usuario es admin se quitan los filtro de propiedad
    if esadmin == '1':
        propiedad = ''

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    print(
        "select * from (" + query + " ) t1 " + propiedad + "????????????????????????????????????????????????????????????????????????")
    mycursor.execute("select * from (" + query + " ) t1 " + propiedad)

    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))

    return jsonify(json_data)


#    for x in myresult:
#        print(x)


def quierolaclasusulawhere(tablename, buscar):
    campos = ' '

    loscampos = []
    loscampos = getfields2(tablename)

    for elcampo in loscampos:
        campos += " (" + elcampo + " like '%" + buscar + "%')  or"

    campos = campos[:-2]
    return campos






def givemepopulationsentence(tablename):
    dbexecutor.executor('call Kill_Process();')

    with open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_population.4tpy'),
              encoding='utf-8-sig') as f:
        return f.read()


def generarelementos(tablename):
    resultado = ''
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	t1.TABLA_FUENTE,	t2.NOMBRE_REPORTE,	concat(		t2.URL_REPORTE_PDF,		'&campofiltro=',		t1.CAMPO_ACCESO,		'&idobjetofiltro=_XXX_'	) AS URL_REPORTE_PDF FROM 	tblperspectivaexterna t1 INNER JOIN tblperspectivaexternadetalle t2 ON t1.IDPERSPECTIVAEXTERNA = t2.IDPERSPECTIVAEXTERNA WHERE 	t2.ACTIVO = 'true'  and t1.TABLA_FUENTE='" + tablename + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}

    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        resultado += "<tr><td><a href='" + result[2] + "' target='' >" + result[1] + "<a><td><tr>"

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return resultado


def damedestinatariosdealta(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT EMAIL from tblaltanotify_" + tablename)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def resolversentencia(sentencia):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(sentencia)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = ''
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos = result[0]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def esvalido(username, password):
    token = str(uuid.uuid4())

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT count(*) as total from tblsysuser where username='" + username + "' and password='" + password + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    if campos[0] > 0:
        guardartoken(token)
        return token
    else:
        return 'No autorizado'


def valtoken(token):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) as total from tbltoken where token='" + token + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    if campos[0] > 0:
        return 'valido'
    else:
        return 'novalido'




def guardartoken(token):
    dbexecutor.executor("insert into tbltoken (token,expira,expirado) values ('" + token + "',DATE_ADD(NOW(), INTERVAL 8 HOUR),0);")

def cuentaregistros(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) as total from " + tablename)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    return str(campos[0])


def checaremail(username, password):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT email from tblsysuser where   username='" + username + "' and password='" + password + "'")
    myresult = mycursor.fetchall()

    resultado = ''
    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])
        resultado = result[0]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    return str(resultado)


def checaradmin(username, password):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT count(*) as total from tblsysuser where admin='true' and  username='" + username + "' and password='" + password + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    if campos[0] > 0:
        # guardar token
        return '1'
    else:
        return '0'


def quieroelid(username, password):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT idsysuser as total from tblsysuser where username='" + username + "' and password='" + password + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    return campos[0]


def dimetipo(username):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT idtipouser from tblsysuser where username='" + username + "'"
    print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    return campos[0]

def url_for(voice):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT urlaction from tblvoiceaction where mensaje='" + voice + "'"
    print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()


    # payload = []
    # content = {}
    resultado=''
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        resultado=result[0]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    return resultado


def checarpermisos(tablename, idusername):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT 	t1.USERNAME, 	t1.IDSYSUSER, 	t1.`NAME`, 	t2.TABLA, 	CASE WHEN ifnull(t2.ACCESO, 'false') = 'false' THEN  0 WHEN ifnull(t2.ACCESO, 'false') = 'true' THEN 	1 END AS ACCESO,  CASE WHEN ifnull(t2.MODIFICAR, 'false') = 'false' THEN 	0 WHEN ifnull(t2.MODIFICAR, 'false') = 'true' THEN 	1 END AS MODIFICAR FROM 	tblsysuser t1 LEFT JOIN tblsyspermiso t2 ON t1.IDSYSUSER = t2.IDSYSUSER     WHERE t1.IDSYSUSER='" + idusername + "' and t2.TABLA='" + tablename + "'"
    print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[4]) + str(result[5]))

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    # print(str(len(campos)) + 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')

    if campos == []:
        campos.append(str('0') + str('0'))

    return campos[0]


def damedestinatariosdecambioestatus(tablename, idestatus):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT EMAIL from tblestatusnotify_" + tablename.lower() + " where estatus='" + idestatus + "'  ")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    # print(campos[0] + '999999999999999999999999999999999999999999999999999999999999999999')
    return campos


def getfields(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	COLUMN_NAME,	DATA_TYPE,	COLUMN_COMMENT FROM 	view_field_details WHERE 	TABLE_SCHEMA = '" + databasex + "' AND TABLE_NAME = '" + tablename.lower() + "'")
    myresult = mycursor.fetchall()

    payload = []
    content = {}
    for result in myresult:
        content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        payload.append(content)
        content = {}

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return jsonify(payload)


def getfields2(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	COLUMN_NAME,	DATA_TYPE,	COLUMN_COMMENT FROM  view_field_details   WHERE 	TABLE_SCHEMA = '" + databasex + "' AND TABLE_NAME = '" + tablename.lower() + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def quierotodosloscampos(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	COLUMN_NAME,	DATA_TYPE,	COLUMN_COMMENT FROM view_field_details WHERE 	TABLE_SCHEMA = '" + databasex + "' AND TABLE_NAME = '" + tablename.lower() + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    lalista = ''

    contador=0

    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

        if result[1] == 'date':
            lalista = lalista + "CONVERT_TZ(" + result[0] + ",'+00:00','" + GMTZone + "') as " + result[0] + " ,"

        if result[1] != 'date' and contador>0:
            lalista = lalista + result[0] + ","

        if result[1] != 'date' and contador==0:
            lalista = lalista + 'cast( ' + result[0] + " as UNSIGNED) as  " + result[0] + " ,"


        contador+=1

            # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    lalista = lalista[:-1]
    return lalista


def damecampos(tablename):
    damecampos = ''
    for distro in getfields2(tablename):
        damecampos = damecampos + '0,DATOS,0,' + distro + ',' + distro + '\r'

    return damecampos


def damecampos2(tablename):
    damecampos = ''
    for distro in getfields2(tablename):
        damecampos = damecampos + distro + ',functionname\r'

    return damecampos


def damecampos3(tablename):
    # '#Format is campo,mostrar (1=mostrar,0-ocultar,2=disabled)'
    damecampos = ''
    for distro in getfields2(tablename):
        if 'AUXILIAR' in str(distro) or 'BLOQUEADO' in str(distro) or 'ELIMINADO' in str(distro):
            damecampos = damecampos + str(distro) + ',O\r'

        if ('AUXILIAR' not in str(distro)) and ('BLOQUEADO' not in str(distro)) and (
                'ELIMINADO' not in str(distro)) and ('GUID' not in str(distro)):
            damecampos = damecampos + str(distro) + ',1\r'

        if 'GUID' in str(distro):
            damecampos = damecampos + str(distro) + ',2\r'

    return damecampos


def damecampos4(tablename):
    # '#Format is campo,width,height
    damecampos = ''
    for distro in getfields2(tablename):
        damecampos = damecampos + distro + ',100,20\r'

    return damecampos


def damecampos5(tablename):
    # '#Format is campo,helptext
    damecampos = ''
    for distro in getfields2(tablename):
        damecampos = damecampos + distro + ',helptext\r'

    return damecampos


def damecampos6(tablename):
    # '#Format is campo,mandatory
    damecampos = ''
    for distro in getfields2(tablename):
        damecampos = damecampos + distro + ',0\r'

    return damecampos


def damecampos7(tablename):
    res = []
    damecampos = ''
    for distro in getfields2(tablename):
        res.append(distro)

    return res


def dametipos(tablename):
    res = []
    for distro in getfields3(tablename):
        res.append(distro)

    return res


def getfields3(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	COLUMN_NAME,case when	DATA_TYPE='varchar' then 'string' else DATA_TYPE end as DATA_TYPE,	COLUMN_COMMENT FROM 	view_field_details WHERE 	TABLE_SCHEMA = '" + databasex + "' AND TABLE_NAME = '" + tablename.lower() + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[1])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def dametiposform(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT 	COLUMN_NAME,	DATA_TYPE,	ifnull(COLUMN_COMMENT,'') as COLUMN_COMMENT FROM view_field_details WHERE 	TABLE_SCHEMA = '" + databasex + "' AND TABLE_NAME = '" + tablename.lower() + "'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[2])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def thegrupos(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT GRUPO FROM tblconfigcampos_" + tablename.lower() + " WHERE MOSTRARCAMPO=1 group by grupo ORDER BY grupo ASC")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}

        campos.append(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def tablasparabuildscript():
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT tablename from tblsysbuild where build='true'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    resultado = ''

    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        resultado += "<a href='/builder?tablename=" + result[0] + "' target='_blank'>Regenerar tabla --> " + result[
            0] + "</a> <br>"

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return resultado[:-1]


def cacheregen():
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("call CACHE_FIELD_TYPES();")
    mydb.commit()

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return 'ok'


def ordencampos(tablename, tipoorden):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT GRUPO, ORDEN,CAMPO, CAPTION, MOSTRARCAMPO, EDITABLE, ANCHO, ALTO, HELPTEXT,  OBLIGATORIO,BUILDTYPE, MOSTRARGRID, MOSTRARFORM FROM tblconfigcampos_" + tablename.lower() + " WHERE MOSTRARCAMPO=1 ORDER BY grupo ASC, orden ASC")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        if tipoorden == 'grupo':
            campos.append(result[0])

        if tipoorden == 'campos':
            campos.append(result[2])

        if tipoorden == 'caption':
            campos.append(result[3])

        if tipoorden == 'mostrarcampo':
            campos.append(result[4])

        if tipoorden == 'editable':
            campos.append(result[5])

        if tipoorden == 'ancho':
            campos.append(result[6])

        if tipoorden == 'alto':
            campos.append(result[7])

        if tipoorden == 'helptext':
            campos.append(result[8])

        if tipoorden == 'obligatorio':
            campos.append(result[9])

        if tipoorden == 'buildtype':
            campos.append(result[10])

        if tipoorden == 'mostrargrid':
            campos.append(result[11])

        if tipoorden == 'mostrarform':
            campos.append(result[12])

            # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def tablasparabuild():
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT tablename from tblsysbuild where build='true'")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    resultado = ''

    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        resultado += result[0] + ","

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return resultado[:-1]


def cacheregen():
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("call CACHE_FIELD_TYPES();")
    mydb.commit()

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return 'ok'


def purgar(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()

    laorden = "delete from " + tablename.lower() + " where ELIMINADO='true';"
    print(laorden)
    mycursor.execute(laorden)
    mydb.commit()

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return 'ok'


def damehijos(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT t1.detail from tblsysmasterdetail t1 inner JOIN tblsystable t2 on t2.TABLA=t1.DETAIL where t1.master='" + tablename.lower() + "'  order by t2.CAPTION_DETAIL asc    ;")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

        # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def dimegrupos(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT GRUPO from tblconfigcampos_" + tablename.lower() + " group by grupo ORDER BY grupo ASC")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(result[0])

        # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos


def dameultimoid(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * from " + tablename.lower() + " ORDER BY ID" + tablename.replace("tbl", "") + " desc limit 1")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    resultado = ''
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        resultado = str(result[0])

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return resultado


def damedisplay(tablename, idobjeto):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT CAMPODISPLAY from " + tablename.lower() + " WHERE " + "ID" + tablename[3:] + "=" + idobjeto)
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    resultado = ''
    for result in myresult:
        resultado = result[0]

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return resultado


def damedatosobjeto(tabla, idobjeto):
    # Get population sentence for this table

    listacampos = []
    listacampos = ordencampos(tabla, "campos")

    lacadena = ''

    for elcampo in listacampos:
        lacadena = lacadena + elcampo + ','

    lacadena = lacadena[:-1]
    populationsentence = "select " + lacadena + " from " + tabla + " where " + 'ID' + tabla.replace("tbl",
                                                                                                    "") + " = " + idobjeto

    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(populationsentence)
    # mycursor.execute('select * from tblarticulo order by IDarticulo desc limit 10')
    myresult = mycursor.fetchall()

    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    json_data = []
    for result in myresult:
        json_data.append(dict(zip(field_names, result)))
    return jsonify(json_data)



