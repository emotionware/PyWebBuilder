import sys
import os
import os.path

from os import path
from flask import Flask, jsonify, request, render_template, session

# String Connection
from _4TPyModel.code.dbstring import hostx
from _4TPyModel.code.dbstring import userx
from _4TPyModel.code.dbstring import passwdx
from _4TPyModel.code.dbstring import databasex
from _4TPyModel.code.dbstring import portx
from _4TPyModel.code.gridpopulate import getfields
from _4TPyModel.code.gridpopulate import getfields2
from _4TPyModel.code.gridpopulate import damecampos
from _4TPyModel.code.gridpopulate import damecampos2
from _4TPyModel.code.gridpopulate import damecampos3
from _4TPyModel.code.gridpopulate import damecampos4
from _4TPyModel.code.gridpopulate import damecampos5
from _4TPyModel.code.gridpopulate import damecampos6
from _4TPyModel.code.gridpopulate import damecampos7
from _4TPyModel.code.gridpopulate import dametiposform
from _4TPyModel.code.gridpopulate import quierotodosloscampos
from _4TPyModel.code.dbexec import dbexecutor

from _4TPyModel.views import app

# Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE


class builderadaptation:
    def builderadaptation(tablename):

        campox = []
        campox = getfields2(tablename)

        res = dbexecutor.executor('call Kill_Process();')

        # Create extra fields
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_char varchar(255) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR2_char varchar(255) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_Memo varchar(400) DEFAULT NULL COMMENT 'memo';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR2_Memo varchar(400) DEFAULT NULL COMMENT 'memo';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_Check varchar(10) DEFAULT NULL COMMENT 'checkbox';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR2_Check varchar(10) DEFAULT NULL COMMENT 'checkbox';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_date date DEFAULT NULL COMMENT 'date';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_date date DEFAULT NULL COMMENT 'date';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_time varchar(50) DEFAULT NULL COMMENT 'time';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR1_decimal double(12,2) DEFAULT NULL COMMENT 'money';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN AUXILIAR2_decimal  double(12,2) DEFAULT NULL COMMENT 'money';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN OBSERVACIONES varchar(400) DEFAULT NULL COMMENT 'memo';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN ELIMINADO varchar(10) DEFAULT NULL COMMENT 'checkbox';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN CREADOR varchar(40) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN BLOQUEADO varchar(10) DEFAULT NULL COMMENT 'checkbox';"
        resultado = dbexecutor.executor(sentencia)
        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN GUID varchar(50) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN CREADOR varchar(50) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN PROPIETARIO varchar(50) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN CAMPODISPLAY varchar(255) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN FECHAALTA date DEFAULT NULL COMMENT 'date';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN FECHAMODIFICACION date DEFAULT NULL COMMENT 'date';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN HORAMODIFICACION varchar(50) DEFAULT NULL COMMENT 'time';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN IMAGENADJUNTA varchar(255) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN ULTIMOUSUARIO varchar(40) DEFAULT NULL COMMENT 'texto';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "ALTER TABLE  " + tablename + "  add COLUMN IDESTATUS_" + tablename + " int(11) DEFAULT NULL COMMENT '*';"
        resultado = dbexecutor.executor(sentencia)

        # cargando todos los campos a un array
        todosloscampos = []
        todosloscampos = damecampos7(tablename)

        res = dbexecutor.executor('call Kill_Process();')

        # CREANDO TABLAS DE ESTATUS
        sentencia = "CREATE TABLE tblestatus_" + tablename + " (   IDESTATUS_" + tablename + " int(11) Not NULL AUTO_INCREMENT,CAMPODISPLAY VARCHAR(80) DEFAULT 'NULL', PRIMARY KEY (IDESTATUS_" + tablename + ") ,  UNIQUE KEY `CAMPONOREPETIBLE` (`CAMPODISPLAY`) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "DROP TRIGGER IF EXISTS  tblestatus_" + tablename + "_BI; "
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE TRIGGER  tblestatus_" + tablename + "_BI BEFORE INSERT On tblestatus_" + tablename + ' FOR EACH ROW \r BEGIN \r '
        sentencia = sentencia + "Set New.CAMPODISPLAY := CONCAT(' ',New.CAMPODISPLAY);" + '\r'
        sentencia = sentencia + "End;"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "DROP TRIGGER IF EXISTS  tblestatus_" + tablename + "_BU; "
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE TRIGGER  tblestatus_" + tablename + "_BU BEFORE UPDATE On tblestatus_" + tablename + ' FOR EACH ROW \r BEGIN \r '
        sentencia = sentencia + "Set New.CAMPODISPLAY := CONCAT(' ',New.CAMPODISPLAY);" + '\r'
        sentencia = sentencia + "End;"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        # archivo population DE LOS ESTATUS
        # if os.path.exists(os.path.join(app.root_path,'templates', 'tables', tablename + '_population.4tpy')):
        # f = open(  os.path.join(app.root_path,'templates', 'tables', tablename +  '_population.4tpy')   , "w",encoding='utf8')
        # f.write("select * from tblestatus_" + tablename + " order by CAMPODISPLAY ASC " )
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        # f.close()

        # archivo population DE notificación de alta
        # if os.path.exists(os.path.join(app.root_path,'templates', 'tables', tablename + '_population.4tpy')):
        f = open(os.path.join(app.root_path, 'templates', 'tables', 'tblaltanotify_' + tablename + '_population.4tpy'),
                 "w", encoding='utf8')
        f.write("select * from tblaltanotify_" + tablename + " order by IDALTANOTIFY_" + tablename + " ASC ")
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        f.close()

        # archivo population DE notificación de cambio de estatus
        # if os.path.exists(os.path.join(app.root_path,'templates', 'tables', tablename + '_population.4tpy')):
        f = open(
            os.path.join(app.root_path, 'templates', 'tables', 'tblestatusnotify_' + tablename + '_population.4tpy'),
            "w", encoding='utf8')
        f.write("select * from tblestatusnotify_" + tablename + " order by IDESTATUSNOTIFY_" + tablename + " ASC ")
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        f.close()

        res = dbexecutor.executor('call Kill_Process();')

        # CREANDO TABLAS DE NOTIFY x CAMBIO ESTATUS
        sentencia = "CREATE TABLE tblestatusnotify_" + tablename + " (   IDESTATUSNOTIFY_" + tablename + " int(11) Not NULL AUTO_INCREMENT,ESTATUS VARCHAR(80) DEFAULT 'NULL', EMAIL VARCHAR(100) DEFAULT 'NULL', PRIMARY KEY (IDESTATUSNOTIFY_" + tablename + ") ,  UNIQUE KEY `NOTIFICACION_REPETIDA` (ESTATUS,EMAIL) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        resultado = dbexecutor.executor(sentencia)

        # CREANDO TABLAS DE NOTIFY x CAMBIO ESTATUS
        sentencia = "CREATE view view_notify_report_" + tablename + "  as select * from " + tablename + ";"
        resultado = dbexecutor.executor(sentencia)

        # CREANDO TABLAS DE NOTIFY x ALTA
        sentencia = "CREATE TABLE tblaltanotify_" + tablename + " (   IDALTANOTIFY_" + tablename + " int(11) Not NULL AUTO_INCREMENT, EMAIL VARCHAR(100) DEFAULT 'NULL', PRIMARY KEY (IDALTANOTIFY_" + tablename + ") ,  UNIQUE KEY `NOTIFICACION_REPETIDA` (EMAIL) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        # CREANDO TABLAS DE CONFIG
        sentencia = "CREATE TABLE tblconfigcampos_" + tablename + " (   IDCONFIGCAMPOS_" + tablename + " int(11) Not NULL AUTO_INCREMENT,GRUPO VARCHAR(255) DEFAULT 'A. GENERAL', ORDEN INT(11) DEFAULT 0,   CAMPO VARCHAR(100) Default NULL, EDITABLE INT(1) DEFAULT 1 COMMENT 'CHECKBOX' , MOSTRARCAMPO INT(11) Default 1  COMMENT 'CHECKBOX', OBLIGATORIO INT(11) Default 0  COMMENT 'CHECKBOX', ANCHO INT(11) DEFAULT NULL, ALTO INT(11) DEFAULT NULL, HELPTEXT VARCHAR(255) DEFAULT NULL, BUILDTYPE varchar(255) default null,  CAPTION VARCHAR(200) DEFAULT NULL,  MOSTRARGRID INT(11) Default 0  COMMENT 'CHECKBOX',  MOSTRARFORM INT(11) Default 0  COMMENT 'CHECKBOX', PRIMARY KEY (IDCONFIGCAMPOS_" + tablename + ") ,  UNIQUE KEY `CAMPONOREPETIBLE` (`CAMPO`) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
        resultado = dbexecutor.executor(sentencia)

        # ANEXANDO CAMPO NUEVO A configcampos MOSTRARFORM
        sentencia = "ALTER TABLE tblconfigcampos_" + tablename + " ADD COLUMN MOSTRARFORM  int(11) DEFAULT 0 COMMENT 'checkbox' AFTER MOSTRARGRID;"
        resultado = dbexecutor.executor(sentencia)



        for cadacampoq in todosloscampos:
            sentencia = "update tblconfigcampos_" + tablename + "  set mostrarcampo=1, GRUPO='X. CONTROL' where campo='PROPIETARIO' "
            resultado = dbexecutor.executor(sentencia)

        # poblando la tabla de config
        sentencia = ''
        for cadacampo in todosloscampos:
            if 'AUXILIAR' in cadacampo or 'GUID' in cadacampo or 'IMAGENADJUNTA' in cadacampo or 'IDESTATUS_' in cadacampo or 'FECHAMODIFICACION' in cadacampo or 'HORAMODIFICACION' in cadacampo or 'ULTIMOUSUARIO' in cadacampo or 'PROPIETARIO' in cadacampo or 'CAMPODISPLAY' in cadacampo or 'HORAMODIFICACION' in cadacampo or 'FECHAMODIFICACION' in cadacampo or 'ULTIMOUSUARIO' in cadacampo or 'CREADOR' in cadacampo:
                sentencia = "insert into tblconfigcampos_" + tablename + "(campo,caption,grupo,orden,editable,mostrarcampo,ancho,alto,helptext,obligatorio) values('" + cadacampo + "','" + cadacampo + "','A. DATOS','0','1','0','250','25','','0');"

                resultado = dbexecutor.executor(sentencia)
            else:
                if 'ELIMINADO' in cadacampo or 'FECHAALTA' in cadacampo or 'PROPIETARIO' in cadacampo or 'BLOQUEADO' in cadacampo or 'CREADOR' in cadacampo:
                    sentencia = "insert into tblconfigcampos_" + tablename + "(campo,caption,grupo,orden,editable,mostrarcampo,ancho,alto,helptext,obligatorio) values('" + cadacampo + "','" + cadacampo + "','X. CONTROL','0','1','1','250','25','','0');"

                    resultado = dbexecutor.executor(sentencia)
                else:
                    sentencia = "insert into tblconfigcampos_" + tablename + "(campo,caption,grupo,orden,editable,mostrarcampo,ancho,alto,helptext,obligatorio) values('" + cadacampo + "','" + cadacampo + "','A. DATOS','0','1','1','250','25','','0');"

                    resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        tiposformx = []
        tiposformx = dametiposform(tablename)
        # poblando la tabla de config
        sentencia = ''
        for cadatipo in tiposformx:
            sentencia = "update tblconfigcampos_" + tablename + " t1, (select * from view_field_details where table_schema='" + databasex + "' and table_name='" + tablename + "') t2 set t1.buildtype=ifnull(t2.COLUMN_COMMENT,'') where t1.campo=t2.column_name;"
            resultado = dbexecutor.executor(sentencia)

        # haciendo no editable el campo ID
        sentencia = "update tblconfigcampos_" + tablename + " set editable=0,orden='-10000', mostrarcampo=1 where campo='ID" + tablename.replace(
            'tbl',
            '').upper() + "' or campo='FECHAALTA' or campo='CREADOR' or campo='BLOQUEADO' or campo='ELIMINADO'   ;"
        resultado = dbexecutor.executor(sentencia)

        # ocultando el campo
        sentencia = "update tblconfigcampos_" + tablename + " set mostrarcampo=0 where campo='CREADOR';"
        resultado = dbexecutor.executor(sentencia)

        # haciendo no editable el campo ID
        sentencia = "update tblconfigcampos_" + tablename + "  SET CAPTION = UC_Words(CAPTION);"
        resultado = dbexecutor.executor(sentencia)

        # caption de fecha alta
        sentencia = "update tblconfigcampos_" + tablename + "  SET CAPTION = 'Fecha Alta' where caption='Fechaalta';"
        resultado = dbexecutor.executor(sentencia)

        # haciendo no editable el campo ID
        sentencia = "update tblconfigcampos_" + tablename + "  SET HELPTEXT = ' ' WHERE BUILDTYPE='*';"
        resultado = dbexecutor.executor(sentencia)

        # haciendo no editable el campo ID
        sentencia = "update tblconfigcampos_" + tablename + "  SET ALTO = 100 WHERE BUILDTYPE='memo';"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_CAMPODISPLAY (IN _id INT(11))\r\n BEGIN  \r\n  UPDATE " + tablename + " SET CAMPODISPLAY=CONCAT(' '," + 'ID' + tablename.replace(
            'tbl', '') + ",'-','-',ifnull(" + campox[1] + ",''),'-',ifnull(" + campox[2] + ",''),'-',ifnull(" + campox[
                        3] + ",'')) WHERE " + 'ID' + tablename.replace('tbl', '') + "=_id;    \r\n  \r\n END"
        # print(sentencia)
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_REFRESCADOR (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_PROCESADOR1 (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_PROCESADOR2 (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_PROCESADOR3 (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_PROCESADOR4 (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_PROCESADOR5 (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_AFTER_UPDATE (IN _id INT(11))\r BEGIN \r update  " + tablename + " set guid=uuid() where (guid is null  or guid='') and " + 'ID' + tablename.replace(
            'tbl', '') + "=_id;\r END"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "insert into tblsystable(tabla,caption_grid,caption_form,caption_detail) values('" + tablename + "','Grid " + tablename + "','Form " + tablename + "','Detalle " + tablename + "')"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE PROCEDURE " + tablename + "_PROC_AFTER_INSERT (IN _id INT(11))\r BEGIN \r END"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "CREATE TRIGGER " + tablename + "_BU BEFORE UPDATE On " + tablename + '\r'
        sentencia = sentencia + "For Each ROW BEGIN" + '\r'
        sentencia = sentencia + "Set New.FECHAMODIFICACION := now();" + '\r'
        # sentencia= sentencia +  "Set New.ULTIMOUSUARIO := USER();" + '\r'
        sentencia = sentencia + "End;"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = "CREATE TRIGGER  " + tablename + "_BI BEFORE INSERT On " + tablename + '\r'
        sentencia = sentencia + "For Each ROW BEGIN" + '\r'
        sentencia = sentencia + "Set New.FECHAMODIFICACION := now();" + '\r'
        sentencia = sentencia + "Set New.GUID := UUID();" + '\r'
        sentencia = sentencia + "Set New.CREADOR := USER();" + '\r'
        # sentencia= sentencia + "Set New.ULTIMOUSUARIO := USER();"  + '\r'
        sentencia = sentencia + "Set New.FECHAALTA := now();" + '\r'
        sentencia = sentencia + "End;"
        resultado = dbexecutor.executor(sentencia)

        sentencia = "INSERT IGNORE INTO tblsyspermiso(tabla,idsysuser,acceso,modificar) SELECT tabla,'1','true','true' from tblsystable"
        resultado = dbexecutor.executor(sentencia)

        res = dbexecutor.executor('call Kill_Process();')

        sentencia = render_template("auditoria.txt", NOMBRETABLA=tablename, CAMPOKEY=campox[0])
        # print(tablename)
        # print(campox[0])
        # print(sentencia)
        resultado = dbexecutor.executor(sentencia)

        # sentencia="INSERT IGNORE INTO tblsysbuild(tablename,build) values('view_" + tablename + "_history','true');"
        # resultado=dbexecutor.executor(sentencia)

        # archivo de configuración general
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_config.html'), "w", encoding='utf8')
        configpage = render_template('templateconfigtable.html', tablename=tablename)
        f.write(configpage)
        f.close()

        # archivo en form  inclussion
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_body_form_inclusion.html')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_body_form_inclusion.html'), "w",
                     encoding='utf8')
            f.write('')
            f.close()

            # archivo en header form inclussion
        if os.path.exists(
                os.path.join(app.root_path, 'templates', 'tables', tablename + '_header_form_inclusion.html')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_header_form_inclusion.html'), "w",
                     encoding='utf8')
            f.write('')
            f.close()

        # archivo en header form inclussion
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_buttons.html')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_buttons.html'), "w",
                     encoding='utf8')
            f.write(render_template('templateformbuttons.html', tablename=tablename))
            f.close()

        # archivo en header form inclussion
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_buttons.html')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_buttons.html'), "w",
                     encoding='utf8')
            f.write(render_template('templategridbuttons.html', tablename=tablename))
            f.close()

            # archivo en header grid inclussion
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_header_inclusion.4tpy')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_header_inclusion.4tpy'), "w",
                     encoding='utf8')
            f.write('')
            f.close()

        # archivo population grid
        #if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_population.4tpy')):
        #    pass
        #else:
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_population.4tpy'), "w",
                     encoding='utf8')
        f.write("select " + quierotodosloscampos(
                tablename) + ", concat('<a style=\"color:blue;\" href=\"javascript:modoedicion('," + campox[
                        0] + ",');\"" + ">Editar</a>') as EDITAR from " + tablename + "  order by " + campox[
                        0] + " desc")
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        f.close()

        f = open(os.path.join(app.root_path, 'templates', 'tables', 'tblestatus_' + tablename + '_population.4tpy'),
                 "w", encoding='utf8')
        f.write('select * from tblestatus_' + tablename)
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        f.close()

        f = open(
            os.path.join(app.root_path, 'templates', 'tables', 'tblconfigcampos_' + tablename + '_population.4tpy'),
            "w", encoding='utf8')
        f.write('select * from tblconfigcampos_' + tablename)
        # f.write('select * from ' + tablename + ' order by ID' + tablename.replace('tbl','') + ' desc '  )
        f.close()

        # archivo de botones top del grid
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_top_buttons.4tpy')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_top_buttons.4tpy'), "w",
                     encoding='utf8')
            resultado = render_template('templategridbuttons.html', tablename=tablename)
            f.write(resultado)
            f.close()





        # grid blocky after load
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_after_load.block')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_after_load.block'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()
        # grid blocky after load js
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_after_load.js')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_after_load.js'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()




        # grid blocky before load
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_before_load.block')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_before_load.block'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()
        # grid blocky before load js
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_before_load.js')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_grid_blocky_before_load.js'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()



        # form blocky before load
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_before_load.block')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_before_load.block'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()
        # form blocky before load js
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_before_load.js')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_before_load.js'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()

        # form blocky after load
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_after_load.block')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_after_load.block'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()
        # form blocky after load
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_after_load.js')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_after_load.js'), "w",
                     encoding='utf8')
            resultado = ''
            f.write(resultado)
            f.close()






        # archivo css form
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables', tablename + '_css.css')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables', tablename + '_css.css'), "w", encoding='utf8')
            f.write(
                '<style>	h5{	color: #982d2d;    font-family: pompadour; font-size: 19px;    font-variant: small-caps;}	td{		color:#0014ff	;    font-family: pompadour;}</style>')
            f.close()

        # cortar conexiones
        sentencia = " call Kill_Process();"
        resultado = dbexecutor.executor(sentencia)

        return 'ok'
