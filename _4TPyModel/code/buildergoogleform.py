# String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx

import sys
import os
import os.path
import time
import string
import mysql.connector
import json
import re
import dis

from os import path
from flask import Flask, jsonify, request, render_template, session

# String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx

from _4TPyModel.views import app

from _4TPyModel.code.dbexec import dbexecutor

# Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE


class builderform:

    def builderform(tablename):

        constructor = "var address = '" + hostx + "';\r\n"
        constructor += "var user = '" + userx + "';\r\n"
        constructor += "var userPwd = '" + passwdx + "';\r\n"
        constructor += "var db = '" + databasex + "';\r\n"

        constructor += 'function formbuild() { \r\n'
        constructor += 'var form = FormApp.create("' + dametitulogrid(tablename) + '"); \r\n'
        constructor += 'var conexion=conectar_mysql(); //realizo conexion con mysql\r\n\r\n\r\n\r\n'

        constructor += "var guardar = SpreadsheetApp.create('" + dametitulogrid(tablename) + "');\r\n"
        constructor += "form.setDestination(FormApp.DestinationType.SPREADSHEET, guardar.getId());\r\n\r\n\r\n"

        constructor += "ScriptApp.newTrigger('enviar2database')\r\n"
        constructor += ".forForm(form)\r\n"
        constructor += ".onFormSubmit()\r\n"
        constructor += ".create();\r\n\r\n"

        campox = getfields4(tablename)
        captionx = getfields5(tablename)
        #grupocampox = getfields6(tablename)
        tipocampox = getfields7(tablename)
        #camposobligatorios = getfields8(tablename)
        #grupox = dimegrupos(tablename)
        tipoxform = tipocampox

        lasfuentesdedatos = ''


        contador = 0
        for cadacampo in campox:
            print(cadacampo + "CC->" + tipoxform[contador].lower())



            # procesando campos
            elcampo = ''

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador] == '' or tipoxform[contador].lower() == 'texto'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador].lower() == 'whatsapp'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador].lower() == 'url'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'
                elcampo += "var textValidation = FormApp.createTextValidation()\r\n"
                elcampo += ".requireTextIsUrl()\r\n"
                elcampo += ".setHelpText('No es una url válida')\r\n"
                elcampo += ".build();\r\n"
                elcampo += "item.setValidation(textValidation);\r\n"

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador].lower() == 'email'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'
                elcampo += "var textValidation = FormApp.createTextValidation()\r\n"
                elcampo += ".requireTextIsEmail()\r\n"
                elcampo += ".setHelpText('No es un email válido')\r\n"
                elcampo += ".build();\r\n"
                elcampo += "item.setValidation(textValidation);\r\n"

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador].lower() == 'list'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var ' + cadacampo + 'tipos=getlista' + cadacampo + 'tipos(conexion); //\r\n'
                elcampo += 'var item = form.addListItem(); //\r\n'
                elcampo += 'item.setChoiceValues(' + cadacampo + 'tipos); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

                lasfuentesdedatos += "function getlista" + cadacampo + 'tipos(){\r\n'
                lasfuentesdedatos += "var stmt = conexion.createStatement();\r\n"
                lasfuentesdedatos += "var results = stmt.executeQuery(\"SELECT concat(IDPRODUCT,'-',PRODUCTO) FROM tblproducts;\");\r\n"
                lasfuentesdedatos += "var numCols = results.getMetaData().getColumnCount();\r\n"
                lasfuentesdedatos += "var lalista = [];\r\n"
                lasfuentesdedatos += "while (results.next()) {\r\n"
                lasfuentesdedatos += "var rowString = '';\r\n"
                lasfuentesdedatos += "for (var col = 0; col < numCols; col++) {\r\n"
                lasfuentesdedatos += "rowString += results.getString(col + 1) + '\t';\r\n"
                lasfuentesdedatos += "lalista.push(rowString);\r\n"
                lasfuentesdedatos += "}\r\n"
                lasfuentesdedatos += "}\r\n"
                lasfuentesdedatos += "return lalista;\r\n"
                lasfuentesdedatos += "}\r\n\r\n"

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and  (tipoxform[contador].lower() == 'date'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addDateItem() //\r\n'
                elcampo += '.setRequired(true) //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and  (tipoxform[contador].lower() == 'gtime'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTimeItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and  (tipoxform[contador].lower() == 'password'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            # if tipoxform[contador].lower() == 'rating':
            #    elcampo += 'var form = FormApp.openById(form.getId());\r\n'
            #    elcampo += 'var item = form.addTextItem(); //\r\n'
            #    elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'



            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and (tipoxform[contador].lower() == 'memo'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addParagraphTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and ('checklist' in tipoxform[contador].lower()):

                # extrayendo opciones de check del comment
                partes = []
                partes = tipoxform[contador].lower().split('|')

                otraspartes = []
                otraspartes = partes[1].split(",")

                lasopciones = '.setChoices(['

                for cadaparte in otraspartes:
                    lasopciones += "item.createChoice('" + cadaparte + "'),\r\n"

                lasopciones = lasopciones[:-3]
                lasopciones += "])"

                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addCheckboxItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '")\r\n'
                elcampo += lasopciones + ';\r\n'

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and  (tipoxform[contador].lower() == 'money'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'
                elcampo += "var textValidation = FormApp.createTextValidation()\r\n"
                elcampo += ".requireNumber()\r\n"
                elcampo += ".setHelpText('No es un número válido')\r\n"
                elcampo += ".build();\r\n"
                elcampo += "item.setValidation(textValidation);\r\n"

            if ("AUXILIAR" not in cadacampo and "PROPIETARIO" not in cadacampo) and   (tipoxform[contador].lower() == 'number'):
                elcampo += 'var form = FormApp.openById(form.getId());\r\n'
                elcampo += 'var item = form.addTextItem(); //\r\n'
                elcampo += 'item.setTitle("' + captionx[contador] + '");\r\n\r\n\r\n'
                elcampo += "var textValidation = FormApp.createTextValidation()\r\n"
                elcampo += ".requireNumber()\r\n"
                elcampo += ".setHelpText('No es un número válido')\r\n"
                elcampo += ".build();\r\n"
                elcampo += "item.setValidation(textValidation);\r\n"

            constructor += elcampo

            contador += 1

        # constructor += "\r\n\r\n}\r\n"

        constructor += "function conectar_mysql(){\r\n"
        constructor += "var instanceUrl = 'jdbc:mysql://' + address;\r\n"
        constructor += "var dbUrl = instanceUrl + '/' + db;\r\n"
        constructor += "var dbUrl = instanceUrl + '/' + db;\r\n"
        constructor += "var conn = Jdbc.getConnection('jdbc:mysql://' + address + ':3306/' + db, user, userPwd);\r\n"
        constructor += "conn.setAutoCommit(false);\r\n"
        constructor += "return conn;\r\n"
        constructor += "}\r\n\r\n\r\n"

        constructor += lasfuentesdedatos

        constructor += "}\r\n\r\n"

        constructor += "function enviar2database(e){\r\n"
        constructor += "var conn = Jdbc.getConnection('jdbc:mysql://' + address + ':3306/' + db, user, userPwd);\r\n"
        constructor += "var itemResponses = e.response.getItemResponses();\r\n"
        constructor += 'var sentencia="insert into ' + tablename + "(" + secuenciadecampos(
            tablename) + ") values (" + secuenciadevalores(tablename) + ")\";\r\n"
        constructor += 'var stmt = conn.prepareStatement(sentencia);\r\n'
        constructor += 'Logger.log("%s", sentencia);\r\n'
        constructor += 'stmt.execute();\r\n'
        constructor += "}\r\n\r\n"

        # constructor += lasfuentesdedatos

        # archivo de configuración general
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_google_form.gs'), "w",
                 encoding='utf8')
        f.write(constructor)
        f.close()

        return "ok"


def secuenciadecampos(tablename):
    return getfields2(tablename)[:-1]


def secuenciadevalores(tablename):
    return getfields3(tablename)[:-1]


def tabletitlex(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT caption_form from tblsystable where tabla='" + tablename.lower() + "'"
    # print(laorden)
    mycursor.execute(laorden)
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
def dametitulogrid(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT caption_grid from tblsystable where tabla='" + tablename.lower() + "'"
    # print(laorden)
    mycursor.execute(laorden)
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
def dametitulodetail(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT caption_detail from tblsystable where tabla='" + tablename.lower() + "'"
    # print(laorden)
    mycursor.execute(laorden)
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
        "SELECT CAMPO FROM  tblconfigcampos_" + tablename + "   WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*' and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = ''
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos += result[0] + ","

        contador += 1
    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
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
        "SELECT CAMPO FROM  tblconfigcampos_" + tablename + "   WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = ''
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos += "'\" " + " + itemResponses[" + str(contador) + "].getResponse() + \"" + "',"
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
def getfields4(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT CAMPO FROM  tblconfigcampos_" + tablename + "   WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[0]))
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
def getfields5(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT CAPTION FROM  tblconfigcampos_" + tablename + "   WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[0]))
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
def getfields6(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT GRUPO FROM  tblconfigcampos_" + tablename + "   WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[0]))
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
def getfields7(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT ifnull(buildtype,'') FROM  tblconfigcampos_" + tablename + "  WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[0]))
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
def getfields8(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT OBLIGATORIO FROM  tblconfigcampos_" + tablename + "  WHERE mostrarcampo=1 and editable=1 and buildtype<>'checkbox' and buildtype<>'*'  and campo<>'PROPIETARIO' order by orden asc")
    myresult = mycursor.fetchall()

    # payload = []
    # content = {}
    campos = []
    contador = 0
    for result in myresult:
        # content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
        # payload.append(content)
        # content = {}
        campos.append(str(result[0]))
        contador += 1

        if contador == 0:
            contador += 1

    # cursor.fetchall() to fetch all rows
    # cursor.fetchone() to fetch single row
    # cursor.fetchmany(SIZE) to fetch limited rows

    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    return campos
