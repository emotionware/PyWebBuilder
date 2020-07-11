import sys
import os
import os.path
import mysql.connector


from os import path
from flask import Flask, jsonify, request, render_template, session

#String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx
from _4TPyModel.code.dbstring import GMTZone



from _4TPyModel.code.gridpopulate import getfields
from _4TPyModel.code.gridpopulate import getfields2
from _4TPyModel.code.gridpopulate import damecampos
from _4TPyModel.code.gridpopulate import damecampos2
from _4TPyModel.code.gridpopulate import damecampos3
from _4TPyModel.code.gridpopulate import damecampos4
from _4TPyModel.code.gridpopulate import damecampos5
from _4TPyModel.code.gridpopulate import damecampos6
from _4TPyModel.code.gridpopulate import damecampos7
from _4TPyModel.code.gridpopulate import dametipos
from _4TPyModel.code.gridpopulate import ordencampos
from _4TPyModel.code.gridpopulate import thegrupos
from _4TPyModel.code.dbexec import dbexecutor

from _4TPyModel.views import app 


#Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE 
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE

def topmenutemplate():
    #leer desde la base de datos el archivo de config del menu
    #return menutop();     
    return render_template('config/topmenu.html')

def topmenutemplate2():
    #leer desde la base de datos el archivo de config del menu
    #return menutop();
    return render_template('config/topmenu2.html')


def gridbuttons(tablename):
    #leer desde la base de datos el archivo de config del menu
    #return menutop();     
    return render_template('tables/' + tablename +  '_grid_buttons.html',campokey=str('ID' + tablename.replace("tbl","")).upper() )

def datafieldsx(tablename):
    resultado=''
    campox=[]
    tipox=[]


    resultado="{name: 'EDITAR', type:'string'}\r,"

   
    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')
    contador=0
    for campo in campox:        

        eltipo=tipox[contador]
        if tipox[contador]=='date':
            resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "', format: 'yyyy-MM-ddTHH:mm:ss-HH:mm'}\r,"

        if tipox[contador]=='time':
            resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "', format: 'HH:mm:ss-HH:mm'}\r,"            


        if contador==0:
            resultado = resultado + "{name: '" + campo + "', type: 'float'}\r,"

        if contador>0 and 'checklist' in tipox[contador] or tipox[contador]=='list' or tipox[contador]=='' or  tipox[contador]=='texto' or  tipox[contador]=='memo' or  tipox[contador]=='whatsapp'  or  tipox[contador]=='email' or  tipox[contador]=='url' or  tipox[contador]=='*':
            resultado = resultado + "{name: '" + campo + "', type: 'string'}\r,"

        if tipox[contador]=='checkbox':
            resultado = resultado + "{name: '" + campo + "', type: 'bool'}\r,"

        if tipox[contador]=='money':
            resultado = resultado + "{name: '" + campo + "', type: 'number'}\r,"

        if tipox[contador]=='number':
            resultado = resultado + "{name: '" + campo + "', type: 'number'}\r,"





       # if tipox[contador]!='date':
       #     resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "'}\r,"

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado

def datafieldsxx(tablename):
    resultado=''
    campox=[]
    tipox=[]


    resultado=""

   
    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')
    contador=0
    for campo in campox:        

        eltipo=tipox[contador]
        if tipox[contador]=='date':
            resultado = resultado + "{name: '" + campo + "', type: 'string'}\r,"

        if tipox[contador]=='time':
            resultado = resultado + "{name: '" + campo + "', type: 'string'}\r,"
            
        if 'checklist' in tipox[contador] or tipox[contador]=='list' or tipox[contador]=='' or  tipox[contador]=='texto' or  tipox[contador]=='memo' or  tipox[contador]=='whatsapp' or  tipox[contador]=='url' or  tipox[contador]=='*':
            resultado = resultado + "{name: '" + campo + "', type: 'string'}\r,"

        if tipox[contador]=='checkbox':
            resultado = resultado + "{name: '" + campo + "', type: 'bool'}\r,"

        if tipox[contador]=='money':
            resultado = resultado + "{name: '" + campo + "', type: 'number'}\r,"





       # if tipox[contador]!='date':
       #     resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "'}\r,"

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado
 

def datafieldsx2(tablename):
    resultado=''
    campox=[]
    tipox=[]

    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')
    mgrid=ordencampos(tablename,'mostrargrid')

    resultado="{ text: 'Editar', datafield: 'EDITAR', width: 60,  filterable: false, textPosition: 'left', theme:theme, columntype:'text', cellclassname: cellclass }\r,"

    contador=0
    for campo in campox:        

        eltipo=tipox[contador]
        if tipox[contador]=='date':

            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + " , columngroup: '" + migrupo(campo,tablename) + "', theme:theme  , filtertype: 'range',  datafield: '" + campo + "', width: '110',  cellsformat: 'dd.MM.yyyy', columntype: 'datetimeinput', createeditor: function (rowIndex, cellValue, editor) { editor.jqxDateTimeInput({ min: new Date(1000, 1, 1), max: new Date(5100, 1, 1), culture: 'es-ES' }); }, initeditor: function (rowindex, cellvalue, editor) { editor.jqxDateTimeInput({ value: cellvalue });}  }\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', hidden: true, theme:theme  ,datafield: '" + campo + "', width: '110',  cellsformat: 'dd.MM.yyyy', columntype: 'datetimeinput', createeditor: function (rowIndex, cellValue, editor) { editor.jqxDateTimeInput({ min: new Date(1000, 1, 1), max: new Date(5100, 1, 1), culture: 'es-ES' }); }, initeditor: function (rowindex, cellvalue, editor) { editor.jqxDateTimeInput({ value: cellvalue });}  }\r,"

            
        if tipox[contador]=='checkbox':   
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', datafield: '" + campo + "', theme:theme , columntype: 'checkbox' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', hidden: true, datafield: '" + campo + "', theme:theme , columntype: 'checkbox' , width: '110'}\r,"           




        if tipox[contador]=='number':   
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', datafield: '" + campo + "', theme:theme ,  cellsformat: 'n1', aggregates: ['sum'], columntype: 'string' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "',  hidden: true, datafield: '" + campo + "', theme:theme ,  aggregates: ['sum'], cellsformat: 'n1', columntype: 'string' , width: '110'}\r,"



        if tipox[contador]=='money':   
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', datafield: '" + campo + "', theme:theme ,  cellsformat: 'c2', aggregates: ['sum'], columntype: 'string' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "',  hidden: true, datafield: '" + campo + "', theme:theme ,  aggregates: ['sum'], cellsformat: 'c2', columntype: 'string' , width: '110'}\r,"

            
 
        if (tipox[contador]=='' or  tipox[contador]=='texto' or 'checklist' in tipox[contador] or tipox[contador]=='list' or tipox[contador]=='email' or  tipox[contador]=='memo' or  tipox[contador]=='whatsapp' or  tipox[contador]=='url' or  tipox[contador]=='*') and '_LINK' not in campo:
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', datafield: '" + campo + "', theme:theme ,  columntype: 'text' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "',  hidden: true, datafield: '" + campo + "', theme:theme ,  columntype: 'text' , width: '110'}\r,"

        if (tipox[contador]=='' or  tipox[contador]=='texto' or 'checklist' in tipox[contador] or tipox[contador]=='list' or  tipox[contador]=='email' or  tipox[contador]=='memo' or  tipox[contador]=='whatsapp' or  tipox[contador]=='url' or  tipox[contador]=='*') and '_LINK' in campo:
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', datafield: '" + campo + "', theme:theme ,columntype:'text',  width: '100', textPosition: 'left'    }\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "',  hidden: false, datafield: '" + campo + "', columntype:'text',theme:theme  , width: '100',  textPosition: 'left'   }\r,"
           
        if tipox[contador]=='time':

            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "', theme:theme , datafield: '" + campo + "', width: '110',  cellsformat: 'HH:mm:ss-HH:mm', columntype: 'datetimeinput', createeditor: function (rowIndex, cellValue, editor) { editor.jqxDateTimeInput({ min: new Date(1000, 1, 1), max: new Date(5100, 1, 1), culture: 'es-ES' }); }, initeditor: function (rowindex, cellvalue, editor) { editor.jqxDateTimeInput({ value: cellvalue });}  }\r,"
            else:
                resultado = resultado + "{text: '" + damecaption(campo,tablename) + "', editable: " + dameeditable(campo,tablename) + ", columngroup: '" + migrupo(campo,tablename) + "',  hidden: true, theme:theme , datafield: '" + campo + "', width: '110',  cellsformat: 'HH:mm:ss-HH:mm', columntype: 'datetimeinput', createeditor: function (rowIndex, cellValue, editor) { editor.jqxDateTimeInput({ min: new Date(1000, 1, 1), max: new Date(5100, 1, 1), culture: 'es-ES' }); }, initeditor: function (rowindex, cellvalue, editor) { editor.jqxDateTimeInput({ value: cellvalue });}  }\r,"

            

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado

def migrupo(campo,tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT grupo from tblconfigcampos_" + tablename + " where campo='" + campo.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0]).replace(" ","")


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

    #print (resultado)

    return resultado

def damecaption(campo,tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT caption from tblconfigcampos_" + tablename + " where campo='" + campo.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0])


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

    #print (resultado)

    return resultado

def dameeditable(campo,tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT editable from tblconfigcampos_" + tablename + " where campo='" + campo.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0])


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

    #print (resultado)
    resultado2='false'


    if resultado=='0':
        resultado2='false'

    if resultado=='1':
        resultado2='true'

    return resultado2

def datafieldsx2x(tablename):
    resultado=''
    campox=[]
    tipox=[]

    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')
    mgrid=ordencampos(tablename,'mostrargrid')

    resultado=""

    contador=0
    for campo in campox:        

        eltipo=tipox[contador]
        if tipox[contador]=='date':

            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + campo + "', theme:theme  ,datafield: '" + campo + "', theme:theme ,  columntype: 'string' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + campo + "', hidden: true, theme:theme  ,datafield: '" + campo + "', width: '110' }\r,"

            
        if tipox[contador]=='checkbox':   
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + campo + "', datafield: '" + campo + "', theme:theme , columntype: 'checkbox' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + campo + "', hidden: true, datafield: '" + campo + "', theme:theme , columntype: 'checkbox' , width: '110'}\r,"           

            

        if tipox[contador]=='money':   
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + campo + "', datafield: '" + campo + "', theme:theme ,  columntype: 'string' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + campo + "',  hidden: true, datafield: '" + campo + "', theme:theme , columntype: 'string' , width: '110'}\r,"

            
 
        if tipox[contador]=='' or  tipox[contador]=='texto' or  tipox[contador]=='email' or  tipox[contador]=='memo' or  tipox[contador]=='whatsapp' or  tipox[contador]=='url' or  tipox[contador]=='*':
            
            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + campo + "', datafield: '" + campo + "', theme:theme ,  columntype: 'text' , width: '110'}\r,"
            else:
                resultado = resultado + "{text: '" + campo + "',  hidden: true, datafield: '" + campo + "', theme:theme ,  columntype: 'text' , width: '110'}\r,"

            
           
        if tipox[contador]=='time':

            if mgrid[contador]==0:
                resultado = resultado + "{text: '" + campo + "', theme:theme , datafield: '" + campo + "', width: '110',  cellsformat: 'HH:mm:ss-HH:mm', columntype: 'string' }\r,"
            else:
                resultado = resultado + "{text: '" + campo + "',  hidden: true, theme:theme , datafield: '" + campo + "', width: '110',  cellsformat: 'HH:mm:ss-HH:mm', columntype: 'string'  }\r,"

            

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado

def datafieldsx3(tablename):
    resultado=''
    campox=[]
    tipox=[]

    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')

  

    contador=0
    for campo in campox:        

        eltipo=tipox[contador]
        if tipox[contador]=='date':
            tipox[contador]='date'
            resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "'}\r,"
            

        if tipox[contador]!='date':
            resultado = resultado + "{name: '" + campo + "', type: '" + tipox[contador] + "'}\r,"

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado

def quierolosgrupos(tablename):
    resultado=''
    grupox=[]

    grupox=thegrupos(tablename)

    contador=0
    for cadagrupo in grupox:
        resultado = resultado + "{ text: '" + cadagrupo + "', align: 'center', name: '" + cadagrupo.replace(" ","") + "' }\r,"

    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado

def losupdates(tablename):
    resultado=''
    campox=[]

    tipox=[]


    tipox=ordencampos(tablename,'buildtype')
   

    campox=ordencampos(tablename,'campos')
    
    # toISOString()

    contador=0
    for campo in campox:   

        if campox[contador]!=('id' + tablename.replace('tbl','')).upper():

            if tipox[contador]!='date':
                resultado += "'" + campox[contador] + "=' + " + chr(34) + chr(39) + chr(34) + " + String($('#grid').jqxGrid('getcellvalue', cell.rowindex, '" + campox[contador] + "')).replace('null','').replace('undefined','')" + " + " + chr(34) + chr(39) + chr(34) + " + " + chr(34) + chr(44) + chr(34) + chr(32) + " + "

            if tipox[contador]=='date':
                resultado += "'" + campox[contador] + "=' + " + chr(34) + chr(39) + chr(34) + " + formatDate( new Date( $('#grid').jqxGrid('getcellvalue', cell.rowindex, '" + campox[contador] + "')  ).toISOString() ) " + " + " + chr(34) + chr(39) + chr(34) + " + " + chr(34) + chr(44) + chr(34) + chr(32) + " + "




        #print(resultado)
    
        contador = contador + 1


    #quitando la ultima coma
    resultado =(resultado).strip()
    resultado=resultado[:-1]


   

    return resultado

def losinserts(tablename):
    resultado=''
    campox=[]

    tipox=[]


    tipox=ordencampos(tablename,'buildtype')
   

    campox=ordencampos(tablename,'campos')
    
    # toISOString()

    contador=0
    for campo in campox:   

        if campox[contador]!=('id' + tablename.replace('tbl','')).upper():

            if tipox[contador]!='date':
                resultado += chr(34) + chr(39) + chr(34) + " + $('#grid').jqxGrid('getcellvalue', cell.rowindex, '" + campox[contador] + "')" + " + " + chr(34) + chr(39) + chr(34) + " + " + chr(34) + chr(44) + chr(34) + chr(32) + " + "

            if tipox[contador]=='date':
                resultado += chr(34) + chr(39) + chr(34) + " + formatDate( new Date( checarnulos( '" + tipox[contador] + "',   $('#grid').jqxGrid('getcellvalue', cell.rowindex, '" + campox[contador] + "')) ).toISOString() ) " + " + " + chr(34) + chr(39) + chr(34) + " + " + chr(34) + chr(44) + chr(34) + chr(32) + " + "




        #print(resultado)
    
        contador = contador + 1


    #quitando la ultima coma
    resultado =(resultado).strip()
    resultado=resultado[:-1]


   

    return resultado

def loscampos(tablename):
    resultado=''
    campox=[]

    tipox=[]


    tipox=ordencampos(tablename,'buildtype')
   

    campox=ordencampos(tablename,'campos')
    
    # toISOString()

    contador=0
    for campo in campox:   

        if campox[contador]!=('id' + tablename.replace('tbl','')).upper():
            resultado += campox[contador] + "," 
             
        #print(resultado)
    
        contador = contador + 1


    #quitando la ultima coma
    resultado =(resultado).strip()
    resultado=resultado[:-1]


   

    return resultado

def asignaciones(tablename):
    resultado=''
    campox=[]
    tipox=[]


    campox=ordencampos(tablename,'campos')
    tipox=ordencampos(tablename,'buildtype')
     
    contador=0
    for campo in campox:   

        if campox[contador]!=('id' + tablename.replace('tbl','')).upper():
            
            if tipox[contador]!='date':
                resultado +=  '$.ajax({async: false,url: "/obtenervalor" + "?sentencia=select  ' + campox[contador] + '  from ' + tablename + ' where ID' + (tablename.replace('tbl','')).upper() + '="'' + value }).then(function (data) { $("#grid").jqxGrid(\'setcellvalue\', rowBoundIndex, "' + campox[contador] + '", String(data).replace("None",""));  $("#mensaje").val("Leyendo registros...espere..." + data);     });\r    '


            if tipox[contador]=='date':
                resultado +=  '$.ajax({async: false,url: "/obtenervalor" + "?sentencia=select  concat(' + campox[contador] + ',\' ' + GMTZone + '\' ) from ' + tablename + ' where ID' + (tablename.replace('tbl','')).upper() + '="'' + value }).then(function (data) { $("#grid").jqxGrid(\'setcellvalue\', rowBoundIndex, "' + campox[contador] + '", String(data).replace("None",""));  $("#mensaje").val("Leyendo registros...espere..." + data);     });\r   '


        #print(resultado)
    
        contador = contador + 1


    #quitando la ultima coma
    resultado = resultado[:-1]
    return resultado


def blocky(param,tablename):

    datos=''

    if param=='bl':
        pathx = os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_before_load.js')
        f = open(pathx, "r", encoding='utf8')
        datos = f.read()
        f.close()

    if param=='al':
        pathx = os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_after_load.js')
        f = open(pathx, "r", encoding='utf8')
        datos = f.read()
        f.close()


    return datos



class buildergrid:
    def buildergrid(tablename):
        campox=[]
        campox=ordencampos(tablename,'campos')

        #GUARDANDO DATAFIELDS1    
        #f = open(os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '_datafields1.4tpy'), "w",encoding='utf8')     
        #f.write(datafieldsx(tablename))
        #f.close()

        #GUARDANDO DATAFIELDS2   
        #f = open(os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '_datafields2.4tpy'), "w",encoding='utf8')     
        #f.write(datafieldsx2(tablename))
        #f.close()

        #GUARDANDO DATAFIELDS3
        #f = open(os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '_datafields3.4tpy'), "w",encoding='utf8')     
        #f.write(datafieldsx3(tablename))
        #f.close()



        grid=render_template("templategrid.html",tablename=tablename,topmenu=topmenutemplate(),buttons=gridbuttons(tablename),campokey=campox[0],datafields=datafieldsx(tablename),datafields2=datafieldsx2(tablename),datafields3=datafieldsx3(tablename),tabletitle=tabletitlex(tablename),elicono=dameicono(tablename),soloadmin=checarpermisos(tablename), grupos=quierolosgrupos(tablename) ,BLOCKY_BEFORE_LOAD=blocky('bl',tablename) ,BLOCKY_AFTER_LOAD=blocky('al',tablename)  )

        #archivo de configuración general        
        f = open(   os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '.html')     , "w",encoding='utf8')       
        f.write(grid)
        f.close()


        #################### MOBILE
        grid=render_template("templategridmobile.html",tablename=tablename,topmenu2=topmenutemplate2(),buttons=gridbuttons(tablename),campokey=campox[0],datafields=datafieldsx(tablename),datafields2=datafieldsx2(tablename),datafields3=datafieldsx3(tablename),tabletitle=tabletitlex(tablename),elicono=dameicono(tablename),soloadmin=checarpermisos(tablename), grupos=quierolosgrupos(tablename) ,BLOCKY_BEFORE_LOAD=blocky('bl',tablename) ,BLOCKY_AFTER_LOAD=blocky('al',tablename)  )

        #archivo de configuración general
        f = open(   os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '_mobile.html')     , "w",encoding='utf8')
        f.write(grid)
        f.close()
        #####################




        grid=render_template("importador.html",tablename=tablename,topmenu=topmenutemplate(),campokey=campox[0],datafields=datafieldsxx(tablename),datafields2=datafieldsx2x(tablename),datafields3=datafieldsx3(tablename),tabletitle=tabletitlex(tablename),asignaciones=asignaciones(tablename),losupdates=losupdates(tablename),loscampos=loscampos(tablename),losinserts=losinserts(tablename))

        #archivo de configuración general        
        f = open(   os.path.join(app.root_path,'templates', 'tables', tablename.lower() + '_importador.html')     , "w",encoding='utf8')       
        f.write(grid)
        f.close()


        # cortar conexiones
        sentencia = " call Kill_Process();"
        resultado = dbexecutor.executor(sentencia)


        return 'ok'


def dameicono(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT icon_grid from tblsystable where tabla='" + tablename.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0])


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

 
    ##print(resultado + '*******************************************************************************************************************')
    if resultado=='None':
        resultado='/static/iconos/grid.png'

    return resultado


def tabletitlex(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT caption_grid from tblsystable where tabla='" + tablename.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0])


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

 

    return resultado


def checarpermisos(tablename):

   
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
        )
    mycursor = mydb.cursor()
    laorden="SELECT soloadmin from tblsystable where tabla='" + tablename.lower() + "'"
    #print(laorden)
    mycursor.execute(laorden)
    myresult = mycursor.fetchall()
    

    #payload = []
    #content = {}
    resultado=''
    for result in myresult:
       #content = {'COLUMN_NAME': result[0], 'DATA_TYPE': result[1], 'COLUMN_COMMENT': result[2]}
       #payload.append(content)
       #content = {}
       resultado=str(result[0])


    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows

        
    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

 

    return resultado


