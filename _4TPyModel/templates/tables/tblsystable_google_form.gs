var address = 'localhost';
var user = 'root';
var userPwd = 'ks2106';
var db = '4tempty';
function formbuild() { 
var form = FormApp.create("Tablas de Sistema"); 
var conexion=conectar_mysql(); //realizo conexion con mysql



var guardar = SpreadsheetApp.create('Tablas de Sistema');
form.setDestination(FormApp.DestinationType.SPREADSHEET, guardar.getId());


ScriptApp.newTrigger('enviar2database')
.forForm(form)
.onFormSubmit()
.create();

var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Tabla");


var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Titulo Del Grid");


var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Titulo Del Form");


var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Titulo Como Detalle");


var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Icono Grid");


var form = FormApp.openById(form.getId());
var item = form.addTextItem(); //
item.setTitle("Icono Form");


var form = FormApp.openById(form.getId());
var item = form.addParagraphTextItem(); //
item.setTitle("Observaciones");


function conectar_mysql(){
var instanceUrl = 'jdbc:mysql://' + address;
var dbUrl = instanceUrl + '/' + db;
var dbUrl = instanceUrl + '/' + db;
var conn = Jdbc.getConnection('jdbc:mysql://' + address + ':3306/' + db, user, userPwd);
conn.setAutoCommit(false);
return conn;
}


}

function enviar2database(e){
var conn = Jdbc.getConnection('jdbc:mysql://' + address + ':3306/' + db, user, userPwd);
var itemResponses = e.response.getItemResponses();
var sentencia="insert into tblsystable(TABLA,CAPTION_GRID,CAPTION_FORM,CAPTION_DETAIL,ICON_GRID,ICON_FORM,OBSERVACIONES) values ('"  + itemResponses[0].getResponse() + "','"  + itemResponses[1].getResponse() + "','"  + itemResponses[2].getResponse() + "','"  + itemResponses[3].getResponse() + "','"  + itemResponses[4].getResponse() + "','"  + itemResponses[5].getResponse() + "','"  + itemResponses[6].getResponse() + "')";
var stmt = conn.prepareStatement(sentencia);
Logger.log("%s", sentencia);
stmt.execute();
}

