import mysql.connector

from flask import Flask, jsonify, request, render_template, session


def topmenutemplate():
    #leer desde la base de datos el archivo de config del menu
    #return menutop();     
    return render_template('config/topmenu.html')

def topmenutemplate2():
    #leer desde la base de datos el archivo de config del menu
    #return menutop();
    return render_template('config/topmenu2.html')

def menutop():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="ks2106",
        database="4tpystudio"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT replace(replace(value,'\r\n',''),'','') as value FROM tblconfig where concept='topmenu';")
    myresult = mycursor.fetchall()
    
    #cursor.fetchall() to fetch all rows
    #cursor.fetchone() to fetch single row
    #cursor.fetchmany(SIZE) to fetch limited rows


    resultadofinal=str(myresult[0]).replace("('","").replace("',)","")
    resultadofinal=str(myresult[0]).replace("\'","'") 


    if (mydb.is_connected()):
            mycursor.close()
            mydb.close()

    return resultadofinal


#    for x in myresult:
#        print(x)
