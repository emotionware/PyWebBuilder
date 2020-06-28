import mysql.connector
import os
import json
import sys


#Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE 
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE


from flask import Flask, jsonify, request, render_template, session


#String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx


class dbexecutor():
    def executor(sentencia):

        try:

            mydb = mysql.connector.connect(
            host=hostx,
            user=userx,
            passwd=passwdx,
            database=databasex,
            port=portx
            )
        
            mycursor = mydb.cursor()
            mycursor.execute(sentencia)
            #myresult = mycursor.fetchall()     
    
            mydb.commit()
            
          
            if (mydb.is_connected()):
                    mycursor.close()
                    mydb.close()

            return 1
        
        except:
            return sys.exc_info()[0]
        
        finally:
            if (mydb.is_connected()):
                mycursor.close()
                mydb.close()



    def executor2(sentencia,tablename):

        try:

            mydb = mysql.connector.connect(
            host=hostx,
            user=userx,
            passwd=passwdx,
            database=databasex,
            port=portx
            )
        
            mycursor = mydb.cursor()
            mycursor.execute(sentencia)
            #myresult = mycursor.fetchall()     
    
            mydb.commit()
            
          
            if (mydb.is_connected()):
                    mycursor.close()
                    mydb.close()

            return 1
        
        except:
            return sys.exc_info()[0]
        
        finally:
            if (mydb.is_connected()):
                mycursor.close()
                mydb.close()


    def dameultimoid(tablename):        
        mydb = mysql.connector.connect(
            host=hostx,
            user=userx,
            passwd=passwdx,
            database=databasex,
            port=portx
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from " + tablename.lower() + " ORDER BY ID" + tablename.replace("tbl","") + " desc limit 1")
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




