

Blockly.defineBlocksWithJsonArray([{
  "type": "html_boton",
  "message0": "HTML BOTON - Valor %1 Estilo %2 Padre %3 Posición %4 Función %5",
  "args0": [
    {
      "type": "input_value",
      "name": "VALOR",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "ESTILO",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "PADRE",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "POSICION",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "Función",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "colour": 290,
  "tooltip": "",
  "helpUrl": ""
}]);







Blockly.defineBlocksWithJsonArray([{
  "type": "ejecutar_sentencia",
  "message0": "EJECUTAR SQL - Sentencia %1",
  "args0": [
    {
      "type": "input_value",
      "name": "Sentencia SQL",
      "check": "String"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
}]);

Blockly.JavaScript['ejecutar_sentencia'] = function(block) {
  var value_sentencia_sql = Blockly.JavaScript.valueToCode(block, 'Sentencia SQL', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '$.ajax({ ' +
   'url: "/sqlexec" + "?tablename=XXXX&sentencia=' +  '" + '  + value_sentencia_sql + ' + "' + '&idobjeto=0" ' +
   '   }).then(function (data) { ' +
   '                   });' +
   '              ';
  return code;
};


Blockly.defineBlocksWithJsonArray([{
  "type": "valor_objeto",
  "message0": "VALOR DE OBJETO - Nombre Objeto %1",
  "args0": [
    {
      "type": "input_value",
      "name": "VALOR_OBJETO",
      "check": "String"
    }
  ],
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
}]);


Blockly.defineBlocksWithJsonArray([{
  "type": "actualizar_formulario",
  "message0": "Actualizar Formulario",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "guardar_fomulario",
  "message0": "Guardar Formulario",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "ir_a_grid",
  "message0": "Ir al Grid",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "bloquear",
  "message0": "Bloquear",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "desbloquear",
  "message0": "Desbloquear",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "clonar",
  "message0": "Clonar",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "eliminar",
  "message0": "Eliminar",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "nuevoregistro",
  "message0": "Nuevo Registro",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "ejecutar_value_change",
  "message0": "EVENTO VALUE CHANGE - Nombre del Objeto %1 Función %2",
  "args0": [
    {
      "type": "input_value",
      "name": "nombre_objeto",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "function",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "aviso",
  "message0": "Notificar %1",
  "args0": [
    {
      "type": "input_value",
      "name": "NAME",
      "check": "String"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "cargar_agente",
  "message0": "Cargar Agente %1 Mov Coordenada X %2 Mov Coordenada Y %3 Mensaje %4",
  "args0": [
    {
      "type": "input_value",
      "name": "nombre_agente",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "Mov X",
      "check": "Number",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "Mov Y",
      "check": "Number",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "mensaje",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "animar_agente_cargado",
  "message0": "Agente Cargado - mensaje %1",
  "args0": [
    {
      "type": "input_value",
      "name": "Agente cargado - mensaje",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "mover_agente_cargado",
  "message0": "Agente Cargado - Mov X %1 Mov Y %2",
  "args0": [
    {
      "type": "input_value",
      "name": "Mov X",
      "check": "Number",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "Mov Y",
      "check": "Number",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "gesto_agente_cargado",
  "message0": "Gesto Agente Cargado - Mov X %1 Mov Y %2",
  "args0": [
    {
      "type": "input_value",
      "name": "Mov X",
      "check": "Number",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "Mov Y",
      "check": "Number",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "ocultar_agente",
  "message0": "Ocultar Agente Cargado",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "focus",
  "message0": "FOCUS Object %1",
  "args0": [
    {
      "type": "input_value",
      "name": "NAME",
      "check": "String"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "disable",
  "message0": "DISABLE Object %1",
  "args0": [
    {
      "type": "input_value",
      "name": "NAME",
      "check": "String"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "enable",
  "message0": "ENABLE Object %1",
  "args0": [
    {
      "type": "input_value",
      "name": "NAME",
      "check": "String"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
}]);


Blockly.JavaScript['ocultar_agente'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'robot.hide();\n';
  return code;
};

Blockly.JavaScript['focus'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
   var code = ' document.getElementById("' + value_name.replace("'","").replace("'","") + '").focus();\n';
  return code;
};

Blockly.JavaScript['disable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '$("#' + value_name.replace("'","").replace("'","") + '").jqxInput({disabled: true});\n';
  return code;
};

Blockly.JavaScript['enable'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
    var code = '$("#' + value_name.replace("'","").replace("'","") + '").jqxInput({disabled: false});\n';
  return code;
};

Blockly.JavaScript['mover_agente_cargado'] = function(block) {
  var value_mov_x = Blockly.JavaScript.valueToCode(block, 'Mov X', Blockly.JavaScript.ORDER_ATOMIC);
  var value_mov_y = Blockly.JavaScript.valueToCode(block, 'Mov Y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'robot.moveTo(' + value_mov_x + ',' + value_mov_y + ');\n';
  return code;
};

Blockly.JavaScript['gesto_agente_cargado'] = function(block) {
  var value_mov_x = Blockly.JavaScript.valueToCode(block, 'Mov X', Blockly.JavaScript.ORDER_ATOMIC);
  var value_mov_y = Blockly.JavaScript.valueToCode(block, 'Mov Y', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
 var code = 'robot.gestureAt(' + value_mov_x + ',' + value_mov_y + ');\n';
  return code;
};

Blockly.JavaScript['animar_agente_cargado'] = function(block) {
  var value_agente_cargado___mensaje = Blockly.JavaScript.valueToCode(block, 'Agente cargado - mensaje', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'robot.speak(' + value_agente_cargado___mensaje + ');\n';
  return code;
};


Blockly.JavaScript['cargar_agente'] = function(block) {
  var value_nombre_agente = Blockly.JavaScript.valueToCode(block, 'nombre_agente', Blockly.JavaScript.ORDER_ATOMIC);
  var value_mov_x = Blockly.JavaScript.valueToCode(block, 'Mov X', Blockly.JavaScript.ORDER_ATOMIC);
  var value_mov_y = Blockly.JavaScript.valueToCode(block, 'Mov Y', Blockly.JavaScript.ORDER_ATOMIC);
  var value_mensaje = Blockly.JavaScript.valueToCode(block, 'mensaje', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '    clippy.load(' +  value_nombre_agente +  ', function(agent) { ' +
   '     agent.show();  ' +
   '     robot = agent;  ' +
   '     agent.moveTo(' + value_mov_x + ',' + value_mov_y + ');  ' +
  ' agent.speak(' + value_mensaje + ');    });;\n';
  return code;
};



Blockly.JavaScript['aviso'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'aviso(' + value_name +  ');\n';
  return code;
};


Blockly.JavaScript['ejecutar_value_change'] = function(block) {
  var value_nombre_objeto = Blockly.JavaScript.valueToCode(block, 'nombre_objeto', Blockly.JavaScript.ORDER_ATOMIC);
  var value_function = Blockly.JavaScript.valueToCode(block, 'function', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '$(document).ready(function () { $("#' + value_nombre_objeto.replace("'","").replace("'","") + '").on("change", ' +
' function (event) { ' + value_function.replace("'","").replace("'","") + '();' + ' });});';
  return code;
};



Blockly.JavaScript['actualizar_formulario'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'actualizardatos();\n';
  return code;
};

Blockly.JavaScript['guardar_fomulario'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'procesarguardado();\n';
  return code;
};

Blockly.JavaScript['ir_a_grid'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'regresarx();\n';
  return code;
};

Blockly.JavaScript['bloquear'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'bloquear();\n';
  return code;
};

Blockly.JavaScript['desbloquear'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'desbloquear();\n';
  return code;
};

Blockly.JavaScript['clonar'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'clonarregistro();\n';
  return code;
};

Blockly.JavaScript['eliminar'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'eliminarregistro();\n';
  return code;
};

Blockly.JavaScript['nuevoregistro'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'nuevoregistro();\n';
  return code;
};





Blockly.defineBlocksWithJsonArray([{
  "type": "concatenador5",
  "message0": "cadena 1 %1 cadena 2 %2 cadena 3 %3 cadena 4 %4 cadena 5 %5",
  "args0": [
    {
      "type": "input_value",
      "name": "segmento1",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento2",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento3",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento4",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento5",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "concatenador4",
  "message0": "cadena 1 %1 cadena 2 %2 cadena 3 %3 cadena 4 %4",
  "args0": [
    {
      "type": "input_value",
      "name": "segmento1",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento2",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento3",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento4",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "concatenador3",
  "message0": "cadena 1 %1 cadena 2 %2 cadena 3 %3",
  "args0": [
    {
      "type": "input_value",
      "name": "segmento1",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento2",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento3",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "concatenador2",
  "message0": "cadena 1 %1 cadena 2 %2",
  "args0": [
    {
      "type": "input_value",
      "name": "segmento1",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "segmento2",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
}]);



Blockly.JavaScript['concatenador5'] = function(block) {
  var value_segmento1 = Blockly.JavaScript.valueToCode(block, 'segmento1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento2 = Blockly.JavaScript.valueToCode(block, 'segmento2', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento3 = Blockly.JavaScript.valueToCode(block, 'segmento3', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento4 = Blockly.JavaScript.valueToCode(block, 'segmento4', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento5 = Blockly.JavaScript.valueToCode(block, 'segmento5', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_segmento1 + '+' + value_segmento2  + '+' +  value_segmento3  + '+' +  value_segmento4  + '+' +  value_segmento5 ;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['concatenador4'] = function(block) {
  var value_segmento1 = Blockly.JavaScript.valueToCode(block, 'segmento1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento2 = Blockly.JavaScript.valueToCode(block, 'segmento2', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento3 = Blockly.JavaScript.valueToCode(block, 'segmento3', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento4 = Blockly.JavaScript.valueToCode(block, 'segmento4', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_segmento1 + '+' + value_segmento2  + '+' +  value_segmento3  + '+' +  value_segmento4  ;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['concatenador3'] = function(block) {
  var value_segmento1 = Blockly.JavaScript.valueToCode(block, 'segmento1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento2 = Blockly.JavaScript.valueToCode(block, 'segmento2', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento3 = Blockly.JavaScript.valueToCode(block, 'segmento3', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_segmento1 + '+' + value_segmento2  + '+' +  value_segmento3    ;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['concatenador2'] = function(block) {
  var value_segmento1 = Blockly.JavaScript.valueToCode(block, 'segmento1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_segmento2 = Blockly.JavaScript.valueToCode(block, 'segmento2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_segmento1 + '+' + value_segmento2   ;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};



Blockly.defineBlocksWithJsonArray([{
  "type": "ir_url",
  "message0": "IR URL - Url %1 Target %2",
  "args0": [
    {
      "type": "input_value",
      "name": "laurl",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "eltarget",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "valor_de_campo",
  "message0": "VALOR DE CAMPO - Sentencia %1 Objeto Destino %2",
  "args0": [
    {
      "type": "input_value",
      "name": "sentencia",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "objeto_destino",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "valor_de_campo_2_var",
  "message0": "VALOR DE CAMPO 2 VAR - Sentencia %1 variable %2",
  "args0": [
    {
      "type": "input_value",
      "name": "sentencia",
      "check": "String",
      "align": "RIGHT"
    },
    {
      "type": "input_value",
      "name": "NAME",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "pausar_ejecucion",
  "message0": "PAUSAR EJECUCIÓN - Milisegundos %1 Función %2",
  "args0": [
    {
      "type": "input_value",
      "name": "segundos",
      "check": "Number"
    },
    {
      "type": "input_value",
      "name": "NAME",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "screen_width",
  "message0": "ANCHO DE PANTALLA",
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "screen_height",
  "message0": "ALTO DE PANTALLA",
  "output": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
},{
  "type": "cargar_agente_solamante",
  "message0": "Cargar Agente Sólamente %1",
  "args0": [
    {
      "type": "input_value",
      "name": "nombre_agente",
      "check": "String",
      "align": "RIGHT"
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 230,
  "tooltip": "",
  "helpUrl": ""
}
]);

Blockly.JavaScript['cargar_agente_solamante'] = function(block) {
  var value_nombre_agente = Blockly.JavaScript.valueToCode(block, 'nombre_agente', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '    clippy.load(' +  value_nombre_agente +  ', function(agent) { ' +
   '     agent.show();  ' +
   '     robot = agent;  ' +
   '    });;\n';
  return code;
};

Blockly.JavaScript['screen_width'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'screen.width';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.JavaScript['screen_height'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'screen.height';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['pausar_ejecucion'] = function(block) {
  var value_segundos = Blockly.JavaScript.valueToCode(block, 'segundos', Blockly.JavaScript.ORDER_ATOMIC);
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'setTimeout(' +  value_name.replace("'","").replace("'","")  + ', ' + value_segundos.replace("'","").replace("'","") + ');\n';
  return code;
};



Blockly.JavaScript['valor_de_campo_2_var'] = function(block) {
  var value_sentencia = Blockly.JavaScript.valueToCode(block, 'sentencia', Blockly.JavaScript.ORDER_ATOMIC);
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
   var code = '$.ajax({ async:false, ' +
   'url: "/obtenervalor?sentencia=' +  '" + '  + value_sentencia +
   '   }).then(function (data) {   ' + value_name.replace("'","").replace("'","") + '=JSON.stringify(data) ;  });  ' ;
  return code;
};

Blockly.JavaScript['valor_de_campo'] = function(block) {
  var value_sentencia = Blockly.JavaScript.valueToCode(block, 'sentencia', Blockly.JavaScript.ORDER_ATOMIC);
  var value_objeto_destino = Blockly.JavaScript.valueToCode(block, 'objeto_destino', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '$.ajax({ ' +
   'url: "/obtenervalor" + "?sentencia=' +  '" + '  + value_sentencia +
   '   }).then(function (data) {  $(' + "'" + '#' + value_objeto_destino.substr(1) + ').val(data);    });  ' ;
  return code;
};

Blockly.JavaScript['ir_url'] = function(block) {
  var value_laurl = Blockly.JavaScript.valueToCode(block, 'laurl', Blockly.JavaScript.ORDER_ATOMIC);
  var value_eltarget = Blockly.JavaScript.valueToCode(block, 'eltarget', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'window.open(' + value_laurl + ',' + value_eltarget  + ');';
  return code;
};


Blockly.JavaScript['valor_objeto'] = function(block) {
  var value_valor_objeto = Blockly.JavaScript.valueToCode(block, 'VALOR_OBJETO', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '  $(' + "'" + '#' + value_valor_objeto.substr(1) + ').val() ';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['html_boton'] = function(block) {
  var value_valor = Blockly.JavaScript.valueToCode(block, 'VALOR', Blockly.JavaScript.ORDER_ATOMIC);
  var value_estilo = Blockly.JavaScript.valueToCode(block, 'ESTILO', Blockly.JavaScript.ORDER_ATOMIC);
  var value_posicion = Blockly.JavaScript.valueToCode(block, 'POSICION', Blockly.JavaScript.ORDER_ATOMIC);
  var value_funci_n = Blockly.JavaScript.valueToCode(block, 'Función', Blockly.JavaScript.ORDER_ATOMIC);
  var value_padre = Blockly.JavaScript.valueToCode(block, 'PADRE', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.





  var posfinal='';
  if (value_posicion=="'Top'"){
    posfinal="'" +  'top_' + value_padre.replace("'","")   ;
  }
    if (value_posicion=="'Left'"){
  posfinal="'" +  'left_' + value_padre.replace("'","")  ;
  }
    if (value_posicion=="'Bottom'"){
  posfinal="'" +  'bottom_' + value_padre.replace("'","")  ;
  }

  var code = '$(document).ready(function () {\n' +
'var element = document.createElement("Button");\n' +
'element.innerHTML = ' + value_valor + ';\n' +
'element.setAttribute("onclick", ' + value_funci_n + ' + "();return false;");\n' +
'element.setAttribute("style",' + value_estilo + ');\n' +
'document.getElementById(' + posfinal + ').appendChild(element);})\n';
  return code;
};

