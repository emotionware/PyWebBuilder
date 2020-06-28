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
from _4TPyModel.code.gridpopulate import dametiposform
from _4TPyModel.code.gridpopulate import ordencampos
from _4TPyModel.code.gridpopulate import dimegrupos
from _4TPyModel.code.gridpopulate import damehijos
from _4TPyModel.code.dbexec import dbexecutor

from _4TPyModel.views import app

from _4TPyModel.code.dbexec import dbexecutor

# Project Paths
from _4TPyModel.code.settings import APP_STATIC
from _4TPyModel.code.settings import APP_TEMPLATE
from _4TPyModel.code.settings import APP_ROOT
from _4TPyModel.code.settings import APP_CODE


def topmenutemplate():
    # leer desde la base de datos el archivo de config del menu
    # return menutop();
    return render_template('config/topmenu.html')


def topmenutemplate2():
    # leer desde la base de datos el archivo de config del menu
    # return menutop();
    return render_template('config/topmenu2.html')


def formbuttons(tablename):
    # leer desde la base de datos el archivo de config del menu
    # return menutop();
    return render_template('tables/' + tablename + '_form_buttons.html', tablename=tablename)


def classformat(name):
    name = name.replace(" ", "").replace(".", "_")
    return name


def tradvalordis(valordisabledx):
    if valordisabledx == 'true':
        return 'disabled'
    else:
        return ''


def inserciongrabadora(valordisabledx, cadacampo):
    resultado = ''

    if valordisabledx == 'false':
        resultado = '<a href=\'javascript:startRecording("' + cadacampo + '");\' > <img id="microphone_' + cadacampo + '" src="/static/iconos/mic.png"  /> </a>'
    else:
        rsultado = ''

    return resultado


def blocky(param, tablename):
    datos = ''

    if param == 'bl':
        pathx = os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_before_load.js')
        f = open(pathx, "r", encoding='utf8')
        datos = f.read()
        f.close()

    if param == 'al':
        pathx = os.path.join(app.root_path, 'templates', 'tables', tablename + '_form_blocky_after_load.js')
        f = open(pathx, "r", encoding='utf8')
        datos = f.read()
        f.close()

    return datos


class builderform:

    def builderform(tablename):
        lafuente = ''
        elvalidador = ''

        ancho = []
        alto = []
        helptext = []
        ancho = ordencampos(tablename, 'ancho')
        alto = ordencampos(tablename, 'alto')
        helptext = ordencampos(tablename, 'helptext')

        campox = []
        campox = ordencampos(tablename, 'campos')

        captionx = []
        captionx = ordencampos(tablename, 'caption')

        grupocampox = []
        grupocampox = ordencampos(tablename, 'grupo')

        tipocampox = []
        tipocampox = ordencampos(tablename, 'buildtype')

        valordisabled = []
        valordisabled = ordencampos(tablename, 'editable')

        camposobligatorios = []
        camposobligatorios = ordencampos(tablename, 'obligatorio')

        grupox = []
        grupox = dimegrupos(tablename)

        mform = []
        mform = ordencampos(tablename, 'mostrarform')

        # cargando parametros de construccion

        cargavalores = ''

        pagchange = '<script>\r\n'

        resultadomobile = ''
        resultado1 = ''
        resultado2 = '<table class="ajustarposicion">'
        resultado3 = '<table class="ajustarposicion">'

        latiene = 2

        tabindex = 0

        tipoxform = []
        tipoxform = ordencampos(tablename, 'buildtype')

        for cadagrupo in grupox:

            if latiene == 1:
                latiene = 2
            else:
                latiene = 1

            grupomostrar = "<tr valign='top'   ><td  colspan='3'  ><h5>" + cadagrupo + "</h5> </tr>"
            yafuemostrado = 0

            contador = 0
            for cadacampo in campox:

                tabindex += 1

                # procesando campos
                elcampo = ''
                elobjeto = ''

                if grupocampox[contador] == cadagrupo:

                    if ('checklist' in tipoxform[contador]) or (
                            tipoxform[contador] == 'list' or tipoxform[contador] == '' or tipoxform[
                        contador] == 'gtime' or tipoxform[
                                contador].lower() == 'texto') and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')
                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxInput('val',  obj['" + cadacampo + "']);\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxInput({  theme:theme , disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'

                        if contador == 0:
                            elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td> <div id="slider" />  </td><td></td></tr><tr   class="filahalf_' + classformat(
                                cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                       captionx[contador] + '</td><td><input ' + tradvalordis(
                                valordisabledx) + '  name="' + cadacampo + '" style="' + marcado + '" class="input_' + classformat(
                                cadacampo) + '"  type="text" tabindex="' + str(
                                tabindex) + '" id="' + cadacampo + '"/> </td><td> <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                       helptext[contador] + '</div></td><td></td></tr></div>\r\n'
                        else:
                            if cadacampo != 'PROPIETARIO':
                                elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                    cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                    cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                           captionx[contador] + '</td><td><input ' + tradvalordis(
                                    valordisabledx) + '  name="' + cadacampo + '" style="' + marcado + '" class="input_' + classformat(
                                    cadacampo) + '"  type="text" tabindex="' + str(
                                    tabindex) + '" id="' + cadacampo + '"/> </td><td>  ' + inserciongrabadora(
                                    valordisabledx,
                                    cadacampo) + '  <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                    cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                           helptext[contador] + '</div></td><td></td></tr></div>\r\n'
                            else:
                                elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                    cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                    cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                           captionx[contador] + '</td><td><input ' + tradvalordis(
                                    valordisabledx) + '  name="' + cadacampo + '" style="' + marcado + '" class="input_' + classformat(
                                    cadacampo) + '"  type="text" tabindex="' + str(
                                    tabindex) + '" id="' + cadacampo + '"/> </td><td>    <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                    cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                           helptext[contador] + '</div></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'whatsapp' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxInput('val',  obj['" + cadacampo + "']);\r\n   document.getElementById('mail_" + cadacampo + "').href='https://api.whatsapp.com/send?phone=+' + obj['" + cadacampo.replace(
                            " ", "") + "'];     \r\n  "
                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxInput({ theme:theme , disabled:' + valordisabledx + ' , height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'

                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <input ' + tradvalordis(
                            valordisabledx) + ' name="' + cadacampo + '"  style="' + marcado + '"    class="input_' + classformat(
                            cadacampo) + '"  type="text" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td>' + inserciongrabadora(valordisabledx,
                                                                                                    cadacampo) + ' <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[
                                       contador] + '</div><a target="_blank" id="mail_' + cadacampo + '" ><div  style="font-size:10px;margin-bottom:5px;" >Abrir WhatsApp</div></a></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'url' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')
                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxInput('val',  obj['" + cadacampo + "']);\r\n   document.getElementById('mail_" + cadacampo + "').href=obj['" + cadacampo + "'];     \r\n  "

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxInput({ theme:theme , disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'

                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <input ' + tradvalordis(
                            valordisabledx) + ' name="' + cadacampo + '"   style="' + marcado + '"    class="input_' + classformat(
                            cadacampo) + '"  type="text" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/><a target="_blank" id="mail_' + cadacampo + '" >Open</a> </td><td style="text-align:left"><div id="left_' + cadacampo + '" /> </td></tr> <tr><td></td><td><a href="https://doc.new"  target="_blank" ><div  style="font-size:10px;margin-bottom:5px;" >*NewDoc</a><a href="https://sheet.new"  target="_blank" >*NewSheet</a><a href="https://slide.new"  target="_blank" >*NewSlide</a><a href="https://docs.google.com/drawings/create"  target="_blank" >*NewDrawing</a></div></td><td></td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div></td><td></td></tr>' + ' \r\n'

                    if tipoxform[contador].lower() == 'email' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')
                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxInput('val',  obj['" + cadacampo + "']);\r\n   document.getElementById('mail_" + cadacampo + "').href='mailto:' + obj['" + cadacampo + "'];     \r\n  "

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxInput({theme:theme , disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'

                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <input ' + tradvalordis(
                            valordisabledx) + ' name="' + cadacampo + '"   style="' + marcado + '"    class="input_' + classformat(
                            cadacampo) + '"  type="text" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td>' + inserciongrabadora(valordisabledx,
                                                                                                    cadacampo) + ' <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[
                                       contador] + '</div><a target="_blank" id="mail_' + cadacampo + '" ><div  style="font-size:10px;margin-bottom:5px;" >Enviar Email</div></a></td><td></td></tr></div>\r\n'

                    if tipoxform[contador] == '*' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')
                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxInput('val',  obj['" + cadacampo + "']);\r\n $(document).ready(function () {$.ajax({ url: '/quierodisplay' + '?idobjeto=' +  obj['" + cadacampo + "'] + '&tablename=' + 'tbl" + cadacampo[
                                                                                                                                                                                                                                                    2:] + "' }).then(function (data) {document.getElementById('bottom_" + cadacampo + "').innerHTML = data;});}); \r\n  "

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxInput({theme:theme , disabled:' + valordisabledx + ', dropDownWidth: 500, height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[
                                                                    contador]) + ', displayMember:"CAMPODISPLAY", valueMember:"' + cadacampo + '",source: function (query, response) {var dataAdapter = new $.jqx.dataAdapter({datatype: "json",datafields:[{ name: "CAMPODISPLAY" },{ name: "' + cadacampo + '" }],url: "populator?campofiltro=null&idobjetofiltro=null&tablename=tbl' + cadacampo[
                                                                                                                                                                                                                                                                                                                                                                                          2:] + '",data:{style: "full",maxRows: 25}},{autoBind: true,formatData: function (data) {data.CAMPODISPLAY_startsWith = query;return data;},loadComplete: function (data) {if (data.length > 0) {response($.map(data, function (item) {document.getElementById("bottom_' + cadacampo + '").innerHTML=""; return {label: item.CAMPODISPLAY,value: item.' + cadacampo + '}}));}}});}});    \r\n'

                        if 'IDESTATUS_' in cadacampo:
                            elobjeto = '<script>  $(document).ready(function () { $("#combodown_' + cadacampo + '").click(function () { $(\'#' + cadacampo + '\').focus();$(\'#' + cadacampo + '\').val(\'\');   simulateWrapper(\'#' + cadacampo + '\', "key-sequence", {sequence: " "});           });});</script><div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                       captionx[contador] + '</td><td> <input ' + tradvalordis(
                                valordisabledx) + ' name="' + cadacampo + '"  style="' + marcado + '"    class="input_' + classformat(
                                cadacampo) + '"  type="text" tabindex="' + str(
                                tabindex) + '" id="' + cadacampo + '"/> </td><td> <img id="combodown_' + cadacampo + '" src="/static/iconos/dropdown.png" height="25px" width="25px" /><a href="configstatus?tablename=' + tablename + '" target="_blank" ><img  id="comboleft_' + cadacampo + '"  src="/static/iconos/adelante.png" height="25px" width="25px" /></a></td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                cadacampo) + '" ><td></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                       helptext[
                                           contador] + '</div><div id="bottom_' + cadacampo + '" /></td><td>    </td></tr></div>\r\n '
                        else:
                            elobjeto = '<script>    function formadeabrir_' + cadacampo + '(){ if ($("#' + cadacampo + '").attr("data-value")!=null) { window.open("formrender?form=tables/tbl' + (
                                cadacampo.replace("ID",
                                                  "")).lower() + '_form&idobjeto=" + $("#' + cadacampo + '").attr("data-value") ,"_blank"); } else { window.open("rendergrid?grid=tables/tbl' + cadacampo[
                                                                                                                                                                                                2:].lower() + '","_blank"); }  }</script>  <script>   $(document).ready(function () { $("#combodown_' + cadacampo + '").click(function () { $(\'#' + cadacampo + '\').focus();$(\'#' + cadacampo + '\').val(\'\');$(\'#' + cadacampo + '\').focus();   simulateWrapper(\'#' + cadacampo + '\', "key-sequence", {sequence: " "});           });});</script><div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                       captionx[contador] + '</td><td> <input ' + tradvalordis(
                                valordisabledx) + ' name="' + cadacampo + '"  style="' + marcado + '"    class="input_' + classformat(
                                cadacampo) + '"  type="text" tabindex="' + str(
                                tabindex) + '" id="' + cadacampo + '"/> </td><td> <img id="combodown_' + cadacampo + '" src="/static/iconos/dropdown.png" height="25px" width="25px" /><a href="javascript:formadeabrir_' + cadacampo + '(); " ><img  id="comboleft_' + cadacampo + '"  src="/static/iconos/adelante.png" height="25px" width="25px" /></a></td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                cadacampo) + '" ><td></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                       helptext[
                                           contador] + '</div><div id="bottom_' + cadacampo + '" /></td><td>    </td></tr></div>\r\n '

                    ###################################SIN USO####################################################
                    if tipoxform[contador] == 'combo' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxComboBox('val',  obj['" + cadacampo + "']);\r\n"
                        elcampo = '$("#' + cadacampo + '").jqxComboBox({theme:theme , dropDownWidth: 500, height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[
                                                                    contador]) + ', displayMember:"CAMPODISPLAY", valueMember:"' + cadacampo + '",source: function (query, response) {var dataAdapter = new $.jqx.dataAdapter({datatype: "json",datafields:[{ name: "CAMPODISPLAY" },{ name: "' + cadacampo + '" }],url: "populator?tablename=tbl' + cadacampo[
                                                                                                                                                                                                                                                                                                                                                     2:] + '",data:{style: "full",maxRows: 25}},{autoBind: true,formatData: function (data) {data.CAMPODISPLAY_startsWith = query;return data;},loadComplete: function (data) {if (data.length > 0) {response($.map(data, function (item) {return {label: item.CAMPODISPLAY,value: item.' + cadacampo + '}}));}}});}});    \r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td><div name="' + cadacampo + '"   style="' + marcado + '"    class="input_' + classformat(
                            cadacampo) + '"  type="text" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'date' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = 'border-radius:6px;'
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-radius:6px;border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "var date_" + cadacampo + "=new Date(obj['" + cadacampo + "']);\r\n date_" + cadacampo + ".setDate(date_" + cadacampo + ".getDate() + 1);    \r\n  $('#" + cadacampo + "').jqxDateTimeInput({value: date_" + cadacampo + "  });\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxDateTimeInput({ theme:theme ,disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'

                        if cadacampo == 'FECHAALTA':
                            elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                       captionx[
                                           contador] + '</td><td> <div  name="' + cadacampo + '"    style="' + marcado + '"  class="input_' + classformat(
                                cadacampo) + '" tabindex="' + str(
                                tabindex) + '" id="' + cadacampo + '"/> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                       helptext[contador] + '</div></td><td></td></tr></div></div>\r\n'
                        else:
                            elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                                cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                                cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + \
                                       captionx[
                                           contador] + '</td><td> <div  name="' + cadacampo + '"    style="' + marcado + '"  class="input_' + classformat(
                                cadacampo) + '" tabindex="' + str(
                                tabindex) + '" id="' + cadacampo + '"/> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                                cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                       helptext[contador] + '</div></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'time' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = 'border-radius:6px;'
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-radius:6px;border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxDateTimeInput('val',  obj['" + cadacampo + "']);\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxDateTimeInput({ theme:theme ,disabled:' + valordisabledx + ',height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[
                                                                    contador]) + ', formatString: "HH:mm:ss" , showTimeButton: true, showCalendarButton: false});\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <div  name="' + cadacampo + '"    style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div> </td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'password' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxPasswordInput('val',  obj['" + cadacampo + "']);\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxPasswordInput({ theme:theme ,  disabled:' + valordisabledx + ',height: ' + str(
                            alto[contador]) + ', width: ' + str(
                            ancho[contador]) + ', showStrength: true, showStrengthPosition: "right" });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[contador] + '</td><td> <input  ' + tradvalordis(
                            valordisabledx) + '  name="' + cadacampo + '"   style="' + marcado + '"   type="password" class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div> </td><td></td></tr></div>\r\n'

                    ###################################SIN USO####################################################
                    if tipoxform[contador].lower().startswith('%'):
                        lacadena = tipoxform[contador].upper()[2:]
                        # print('CADENAAAAAAAAAAAAAAAAA --> ' + lacadena)

                        cargavalores += "$('#" + cadacampo + "').jqxListBox({value: obj['" + cadacampo + "']});\r\n"
                        elcampo = ' var source_' + cadacampo + '=[' + lacadena + ']; \r\n  $("#' + cadacampo + '").jqxListBox({ source: source_' + cadacampo + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ', theme: "classic"});\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td>' + marcado + '<div  name="' + cadacampo + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'rating' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxRating({value: obj['" + cadacampo + "']});\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxRating({ theme:theme , disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ', theme: "classic"});\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td>  <div  name="' + cadacampo + '"  style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div> </td><td></td></tr></div>\r\n'

                    ###################################SIN USO####################################################
                    if tipoxform[contador].lower() == 'editor' and mform[contador] == 0:
                        cargavalores += "$('#" + cadacampo + "').jqxEditor('val',  obj['" + cadacampo + "']);\r\n"
                        elcampo = '$("#' + cadacampo + '").jqxEditor({ theme:theme ,height: "400px", width: getWidth("editor") });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td>' + marcado + '<textarea  name="' + cadacampo + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></></textarea> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td></td><td></td></tr></div>\r\n'

                    ###################################SIN USO####################################################
                    if tipoxform[contador].lower() == 'calendar' and mform[contador] == 0:
                        cargavalores += "$('#" + cadacampo + "').jqxCalendar('val',  obj['" + cadacampo + "']);\r\n"
                        elcampo = '$("#' + cadacampo + '").jqxCalendar({theme:theme ,width: 220, height: 220});\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td>' + marcado + '<div  name="' + cadacampo + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'memo' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = ''
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxTextArea('val',  obj['" + cadacampo + "']);\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxTextArea({ theme:theme , disabled:' + valordisabledx + ', height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td valign="Top" class="caption_' + classformat(
                            captionx[contador]) + '" >' + captionx[contador] + '</td><td> <textarea ' + tradvalordis(
                            valordisabledx) + '  name="' + cadacampo + '"   style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"></textarea></td><td>' + inserciongrabadora(
                            valordisabledx,
                            cadacampo) + ' <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div> </td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'checkbox' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   // var value = $("#' + cadacampo + '").val(); \r\n });}); \r\n\r\n '

                        marcado = 'border-radius:6px;'
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "$('#" + cadacampo + "').jqxCheckBox('val',  obj['" + cadacampo + "']);\r\n"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxCheckBox({ hasThreeStates:false, theme:theme , disabled:' + valordisabledx + ',height: ' + str(
                            alto[contador]) + ', width: ' + str(ancho[contador]) + ' });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <div  name="' + cadacampo + '"    style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td><div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td><div id="bottom_' + cadacampo + '" /></td><td><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;;" >' + \
                                   helptext[contador] + '</div> </td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'money' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   var value = $("#' + cadacampo + '").val(); \r\n  $("#bottom_' + cadacampo + '").html(numberWithCommas(value));      });}); \r\n\r\n '

                        marcado = 'border-radius:6px;'
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "var number_" + cadacampo + "=obj['" + cadacampo + "'];\r\n  if (number_" + cadacampo + "==null) {number_" + cadacampo + "=0}    \r\n  $('#" + cadacampo + "').jqxNumberInput('val', number_" + cadacampo + "  );\r\n $('#bottom_" + cadacampo + "').html( numberWithCommas(obj['" + cadacampo + "']) );"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxNumberInput({ theme:theme , disabled:' + valordisabledx + ',max: 999999999999, digits: 25, height: ' + str(
                            alto[contador]) + ', width: ' + str(
                            ancho[contador]) + ', inputMode:"simple", spinButtons: true });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <div  name="' + cadacampo + '"  style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td> <td> ' + inserciongrabadora(valordisabledx,
                                                                                                      cadacampo) + ' <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td></td><td align="right"  style="position:relative;left:-26px" ><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;position:relative;left:-150px;" >' + \
                                   helptext[
                                       contador] + '</div> <div style="display:None;" id="bottom_' + cadacampo + '" /></td><td></td></tr></div>\r\n'

                    if tipoxform[contador].lower() == 'number' and mform[contador] == 0:

                        pagchange += '$(document).ready(function () { $("#' + cadacampo + '").on("change", \r\n function (event) { \r\n // var type = event.args.type; // keyboard, mouse or null depending on how the value was changed. \r\n   var value = $("#' + cadacampo + '").val(); \r\n  $("#bottom_' + cadacampo + '").html(numberWithCommas(value));      });}); \r\n\r\n '

                        marcado = 'border-radius:6px;'
                        # print ("OBLIGATORIO: " + cadacampo + '----' + str(camposobligatorios[contador]) + '888888888888888888888888888888888888888888888888')

                        if camposobligatorios[contador] == 1:
                            marcado = 'border-style: solid; border-top-width:0px; border-left-width:0px; border-right-width:0px; border-color: coral;'
                            elvalidador += "{ input: '#" + cadacampo + "', message: 'Campo requerido', action: 'keyup, blur', rule: 'required' },"

                        cargavalores += "var number_" + cadacampo + "=obj['" + cadacampo + "'];\r\n  if (number_" + cadacampo + "==null) {number_" + cadacampo + "=0}    \r\n  $('#" + cadacampo + "').jqxNumberInput('val', number_" + cadacampo + "  );\r\n $('#bottom_" + cadacampo + "').html( numberWithCommas(obj['" + cadacampo + "']) );"

                        if valordisabled[contador] == 0:
                            valordisabledx = 'true'
                        else:
                            valordisabledx = 'false'

                        elcampo = '$("#' + cadacampo + '").jqxNumberInput({ theme:theme , disabled:' + valordisabledx + ',max: 999999999999, digits: 25, height: ' + str(
                            alto[contador]) + ', width: ' + str(
                            ancho[contador]) + ', inputMode:"simple", spinButtons: true });\r\n'
                        elobjeto = '<div  style="position:relative;left:10px" id="campo' + cadacampo + '" ><tr   class="filatop_' + classformat(
                            cadacampo) + '"  ><td><div id="top_' + cadacampo + '" /></td><td></td><td></td></tr><tr   class="filahalf_' + classformat(
                            cadacampo) + '" ><td class="caption_' + classformat(captionx[contador]) + '" >' + captionx[
                                       contador] + '</td><td> <div  name="' + cadacampo + '"  style="' + marcado + '"  class="input_' + classformat(
                            cadacampo) + '" tabindex="' + str(
                            tabindex) + '" id="' + cadacampo + '"/> </td><td> ' + inserciongrabadora(valordisabledx,
                                                                                                     cadacampo) + ' <div id="left_' + cadacampo + '" /> </td></tr><tr  class="filabottom_' + classformat(
                            cadacampo) + '" ><td></td><td align="right"  style="position:relative;left:-26px" ><div  style="font-size:10px;margin-bottom: 5px;font-style: italic;color: navy;font-variant: all-small-caps;position:relative;left:-150px;" >' + \
                                   helptext[
                                       contador] + '</div> <div style="display:None;" id="bottom_' + cadacampo + '" /></td><td></td></tr></div>\r\n'

                    if yafuemostrado == 1:
                        resultadomobile = resultadomobile + elobjeto

                    if yafuemostrado == 0:
                        resultadomobile = resultadomobile + grupomostrar + elobjeto


                    if latiene == 1:
                        resultado1 = resultado1 + str(elcampo)

                        if yafuemostrado == 1:
                            resultado2 = resultado2 + elobjeto


                        if yafuemostrado == 0 or yafuemostrado == None:
                            resultado2 = resultado2 + grupomostrar + elobjeto
                            yafuemostrado = 1

                    if latiene == 2:
                        resultado1 = resultado1 + str(elcampo)

                        if yafuemostrado == 1:
                            resultado3 = resultado3 + elobjeto


                        if yafuemostrado == 0 or yafuemostrado == None:
                            resultado3 = resultado3 + grupomostrar + elobjeto
                            yafuemostrado = 1

                # time.sleep(0.4)
                contador += 1

        parte1 = "$('#theform').jqxValidator({ hintType: 'label', rules: ["
        parte2 = "]});"

        #

        elvalidador = parte1 + elvalidador[:-1] + parte2

        pagchange += "</script>"

        # guardando la página de control de cambios
        if os.path.exists(os.path.join(app.root_path, 'templates', 'tables',
                                       tablename.lower() + '_config_fields_value_change.js')):
            pass
        else:
            f = open(os.path.join(app.root_path, 'templates', 'tables',
                                  tablename.lower() + '_config_fields_value_change.js'), "w", encoding='utf8')
            f.write(pagchange)
            f.close()

        # leyendo archivo 1
        f = open(
            os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_config_fields_value_change.js'),
            "r")
        pagchange = f.read()
        f.close

        # leyendo archivo 2
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_body_form_inclusion.html'),
                 "r")
        bodyforminclusion = f.read()
        f.close

        # leyendo archivo 3
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_header_form_inclusion.html'),
                 "r")
        headerforminclusion = f.read()
        f.close

        # leyendo archivo 4
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_css.css'), "r")
        cssinclusion = f.read()
        f.close

        # estableciendo páginas hijo
        hijos = []
        hijos = damehijos(tablename)

        loshijos = ''
        lostitulos = ''
        contadorhijos = 0
        asignaciones = ''
        asigdinamica = ''
        deshabilitarx = ''
        tienehijos = 'false'

        for valuex in hijos:
            loshijos += "<div> <embed  src='rendergrid?campofiltro=" + campox[
                0] + "&idobjetofiltro=' + document.getElementById('IDOBJECT').value + '&vistadetalle=true&grid=tables/" + valuex + "'  id='hijo_" + str(
                contadorhijos) + "' style='width:100%' height='1200'  />  </div> \r\n"
            lostitulos += "<li>" + dametitulodetail(valuex) + "</li> \r\n"
            asignaciones += "document.getElementById('hijo_" + str(
                contadorhijos) + "').src = 'rendergrid?campofiltro=" + campox[
                                0] + "&idobjetofiltro=' + document.getElementById('IDOBJECT').value + '&vistadetalle=true&grid=tables/" + valuex + "';  \r\n"
            asigdinamica += "if (nombrex=='hijo_" + str(contadorhijos) + "') { document.getElementById('hijo_" + str(
                contadorhijos) + "').setAttribute('src','rendergrid?campofiltro=" + campox[
                                0] + "&idobjetofiltro=' + document.getElementById('IDOBJECT').value + '&vistadetalle=true&grid=tables/" + valuex + "'); } \r\n"
            deshabilitarx += " if (document.getElementById('IDOBJECT').value=='') { $('#tabs').jqxTabs('disableAt', " + str(
                contadorhijos + 2) + ");  } \r\n"
            tienehijos = 'true'

            contadorhijos += 1

            # print(loshijos)
            # print(lostitulos)

        formx = render_template("templateform.html", tablename=tablename, topmenu=topmenutemplate(),
                                buttons=formbuttons(tablename), campokey=campox[0], campos1=resultado1,
                                campos3=resultado3 + '</table>', campos2=resultado2 + '</table>',
                                cargavalores=cargavalores, valuechanges=pagchange, bodyforminclusion=bodyforminclusion,
                                headerforminclusion=headerforminclusion, cssinclusion=cssinclusion,
                                tabletitle=tabletitlex(tablename), tablashijo=loshijos, tituloshijo=lostitulos,
                                asignacionesiframe=asignaciones, asignaciondinamica=asigdinamica,
                                elicono=dameicono(tablename), deshabilitarx=deshabilitarx, tienehijos=tienehijos,
                                elvalidador=elvalidador, BLOCKY_BEFORE_LOAD=blocky('bl', tablename),
                                BLOCKY_AFTER_LOAD=blocky('al', tablename))

        print('campo llave es --> ' + campox[0])

        # cortar conexiones
        sentencia = " call Kill_Process();"
        resultado = dbexecutor.executor(sentencia)

        # archivo de configuración general
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_form.html'), "w",
                 encoding='utf8')
        f.write(formx)
        f.close()

        # mobile#################################
        #######################################
        formx = render_template("templateformmobile.html", tablename=tablename, topmenu2=topmenutemplate2(),
                                buttons=formbuttons(tablename), campokey=campox[0], campos1=resultado1,
                                campos3='' + '</table>', campos2=resultadomobile + '</table>',
                                cargavalores=cargavalores, valuechanges=pagchange, bodyforminclusion=bodyforminclusion,
                                headerforminclusion=headerforminclusion, cssinclusion=cssinclusion,
                                tabletitle=tabletitlex(tablename), tablashijo=loshijos, tituloshijo=lostitulos,
                                asignacionesiframe=asignaciones, asignaciondinamica=asigdinamica,
                                elicono=dameicono(tablename), deshabilitarx=deshabilitarx, tienehijos=tienehijos,
                                elvalidador=elvalidador, BLOCKY_BEFORE_LOAD=blocky('bl', tablename),
                                BLOCKY_AFTER_LOAD=blocky('al', tablename))

        print('campo llave es --> ' + campox[0])

        # cortar conexiones
        sentencia = " call Kill_Process();"
        resultado = dbexecutor.executor(sentencia)

        # archivo de configuración general
        f = open(os.path.join(app.root_path, 'templates', 'tables', tablename.lower() + '_form_mobile.html'), "w",
                 encoding='utf8')
        f.write(formx)
        f.close()

        return "ok"


def dameicono(tablename):
    mydb = mysql.connector.connect(
        host=hostx,
        user=userx,
        passwd=passwdx,
        database=databasex,
        port=portx
    )
    mycursor = mydb.cursor()
    laorden = "SELECT icon_form  from tblsystable where tabla='" + tablename.lower() + "'"
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

    if resultado == 'None':
        resultado = '/static/iconos/form.png'
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
