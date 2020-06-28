function damecolumnas(query,perspectiva){
var campos=[];

//format option;
//currency
//###,###,###,###.##
//shortDate
//longDate
//fixedPoint" - 100.11 → 100
//"percent" - 0.1 → 10%
//"decimal" - 100.11 → 100
//"exponential" - 1 000 → 1E+3
//"thousands" - 1 000.11 → 1K
//"millions" - 1 000 000.11 → 1M
//"billions" - 1 000 000 000.11 → 1B
//"trillions" - 1 000 000 000 000 → 1T
//"largeNumber"*

//dataType option;
//date
//number

//Se puede modificar el Caption del Campo con caption:"Nuevo Caption"

/////////////////////////////////////////EJEMPLO
if (query=='view_flujo_semanal'){
    campos=[
          { format:"###,###,###,###.##", dataType:"number", dataField: "IMPORTE_MN"},
          { format:"shortDate", dataType: "date", dataField: "FECHA"}
          ];
}
/////////////////////////////////////////////////

/////////////////////////////////////////EJEMPLO
if (query=='view_flujo_semanal' && perspectiva=="porcentual"  ){
    campos=[
          { format:"percent", dataType:"number", dataField: "IMPORTE_MN"},
          { format:"shortDate", dataType: "date", dataField: "FECHA"}
          ];
}
/////////////////////////////////////////////////



 
 
 
 
 



return campos;
}