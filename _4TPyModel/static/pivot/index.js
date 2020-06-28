




  var url_string = window.location.href;
            var url = new URL(url_string);
            var query = url.searchParams.get("query");
            var cwhere = url.searchParams.get("where");
            var perspectiva = url.searchParams.get("perspectiva");


if (cwhere=='null' || cwhere==null){
    cwhere='';}




 var summaryDisplayModes = [
        { text: "Ninguno", value: "none" },
        { text: "Variación Absoluta", value: "absoluteVariation" },
        { text: "% Variación", value: "percentVariation" },
        { text: "% Total de la Columna", value: "percentOfColumnTotal" },
        { text: "% Total Fila", value: "percentOfRowTotal" },
        { text: "% Columna Gran Total", value: "percentOfColumnGrandTotal" },
        { text: "% Fila Gran Total", value: "percentOfRowGrandTotal" },
        { text: "% Gran Total", value: "percentOfGrandTotal" }
    ];


$(function() {

  var pivotgrid=$("#pivotgrid").dxPivotGrid({
      loadPanel: true,
      allowSortingBySummary: true,
        allowSorting: true,
        allowFiltering: true,
        height: 620,
        showBorders: true,
        onContextMenuPreparing: contextMenuPreparing,
        rowHeaderLayout: "standard",
         export: {
            enabled: true,
            fileName: "pivot"
        },
        scrolling: {
            mode: "virtual"
        },headerFilter: {
            allowSearch: true,
            showRelevantValues: true,
            width: 300,
            height: 400,
            texts:{cancel:"Cancelar", emptyValue:"Valor vacío",    }
        },
        texts:{collapseAll:"Colapsar Todo" ,grandTotal:"Gran Total",dataNotAvailable:"Datos no disponibles", expandAll:"Expandir Todo", exportToExcel:"Exportar a Excel", noData:"Sin Datos" , removeAllSorting:"Eliminar Ordenamientos", showFieldChooser:"Mostrar Selector de Campos", sortColumnBySummary:"Ordenar Columnas por Resumen", sortRowBySummary:"Ordenar Filas por Resumen", total:"Total" },
        fieldPanel: {
            showColumnFields: true,
            showDataFields: true,
            showFilterFields: true,
            showRowFields: true,
            allowFieldDragging: true,
            visible: true,
            texts:{columnFieldArea:"Área de Columnas", dataFieldArea:"Área de datos" , filterFieldArea:"Área de filtros", rowFieldArea:"Área de filas" }
        },
        fieldChooser:{
            title:"Selector de Campos",
            texts:{ allFields:"Campos" , columnFields:"Columnas", dataFields:"Datos" , filterFields:"Filtros", rowFields:"Filas"  }

        },

         stateStoring: {
            enabled: true,
            type: "localStorage",
            storageKey: "7184468"
        },

        dataSource: {
 fields :damecolumnas(query,perspectiva)
            ,
            remoteOperations: false,
            store: DevExpress.data.AspNet.createStore({
              loadUrl: "../../displayquery2?query=" + query + "&where=" + cwhere
            })
        }
    }).dxPivotGrid("instance");





        $("#guardar").dxButton({
        text: "PivotGrid's State",
        onClick: function() {

            if (document.getElementById('nombre').value==''){

                alert('Para guardar una perspectiva es preciso indicar un nombre');


            }else{

                        var params = { state: pivotgrid.getDataSource().state() }
            $.ajax({
                type: "POST",
                url: "../../setperspectiva?query=" + query + "&perspectiva=" + document.getElementById('nombre').value,
                data: JSON.stringify(params),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {
                    DevExpress.ui.notify("State was saved");
                },
                failure: function (response) {
                    alert(response.d);
                }
            });

}

        }});


        $("#cargar").dxButton({
        text: "PivotGrid's State",
        onClick: function() {


                $.ajax({
                type: "POST",
                url: "../../getperspectiva?query=" + query + "&perspectiva=" + perspectiva,
                data: JSON.stringify({ userName: "UserA" }),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {


                    //alert(response);


                    var elestado=response.replace('{"state":',"");
                    elestado=elestado.replace("b'","");

                    //alert(elestado);

                    elestado =elestado.replace("}}'","}")    ;

                    //alert(elestado);

                    elestado=JSON.parse(elestado);


                    //var elestado=JSON.stringify( response).replace("{\"state\":","");
                    //var elestado = JSON.parse ( elestado.substring(0, elestado.length - 1)  );

                    //pivotgrid.getDataSource().state(response.d);
                    //pivotgrid.getDataSource().state(response);

                    //pivotgrid.getDataSource().state({"fields":[{"dataField":"ACCION"},{"dataField":"FECHA"},{"dataField":"HORA"},{"dataField":"IDPRODUCTIVIDAD"},{"dataField":"NAME","areaIndex":-1},{"dataField":"TABLA","area":"row","areaIndex":0},{"dataField":"USERNAME"}],"columnExpandedPaths":[],"rowExpandedPaths":[]});
                    //                                {"fields":[{"dataField":"ACCION"},{"dataField":"FECHA"},{"dataField":"HORA"},{"dataField":"IDPRODUCTIVIDAD"},{"dataField":"NAME","areaIndex":-1},{"dataField":"TABLA","area":"row","areaIndex":0},{"dataField":"USERNAME"}],"columnExpandedPaths":[],"rowExpandedPaths":[]}

                    pivotgrid.getDataSource().state(elestado);
                    //window.localStorage.setItem("7184468", elestado);
                    DevExpress.ui.notify("Perspectiva cargada!");


                },
                failure: function (response) {
                    alert(response.d);
                }
            });


        }});


 });


        $("#formatoavanzado").dxButton({
        text: "Reset the PivotGrid's State",
        onClick: function() {
window.open('/static/ace/ace.html?archivo=config/pivotfield.js&tipo=javascript','_blank');
        }});

        $("#refrescar").dxButton({
        text: "Reset the PivotGrid's State",
        onClick: function() {
location.reload();
        }});

        $("#porcentaje").dxButton({
        text: "Reset the PivotGrid's State",
        onClick: function() {
window.open('/static/pivot/index2.html?query=' + query + "&perspectiva=" + perspectiva ,'_self');
        }});


        $("#listar").dxButton({
        text: "Reset the PivotGrid's State",
        onClick: function() {
window.open('/static/pivot/listar.html?query=' + query  ,'_self');
        }});



        $("#reset").dxButton({
        text: "Reset the PivotGrid's State",
        onClick: function() {
            pivotgrid.getDataSource().state({});
        }});



function onSave() {
            var params = { state: pivotgrid.getDataSource().state(), userName: "UserA" }
            $.ajax({
                type: "POST",
                url: "../../setperspectiva",
                data: JSON.stringify(params),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {
                    DevExpress.ui.notify("State was saved");
                },
                failure: function (response) {
                    alert(response.d);
                }
            });
        }
        function onLoad() {
            $.ajax({
                type: "POST",
                url: "../../getperspectiva",
                data: JSON.stringify({ userName: "UserA" }),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {
                    pivotgrid.getDataSource().state(response.d);
                    //window.localStorage.setItem("dx-widget-gallery-pivotgrid-storing", response);
                    DevExpress.ui.notify("State was loaded");

                },
                failure: function (response) {
                    alert(response.d);
                }
            });
        }




function contextMenuPreparing(e) {
        var dataSource = e.component.getDataSource(),
            sourceField = e.field;

        if (sourceField) {
            if(!sourceField.groupName || sourceField.groupIndex === 0) {
                e.items.push({
                    text: "Ocultar Campo",
                    onItemClick: function () {
                        var fieldIndex;
                        if(sourceField.groupName) {
                            fieldIndex = dataSource.getAreaFields(sourceField.area, true)[sourceField.areaIndex].index;
                        } else {
                            fieldIndex = sourceField.index;
                        }

                        dataSource.field(fieldIndex, {
                            area: null
                        });
                        dataSource.load();
                    }
                });
            }

            if (sourceField.dataType === "number") {
                var setSummaryType = function (args) {
                    dataSource.field(sourceField.index, {
                        summaryType: args.itemData.value
                    });

                    dataSource.load();
                },
                menuItems = [];

                e.items.push({ text: "Tipo de Resumen", items: menuItems });

                $.each(["Sum", "Avg", "Min", "Max", "Count"], function(_, summaryType) {
                    var summaryTypeValue = summaryType.toLowerCase();

                    menuItems.push({
                        text: summaryType,
                        value: summaryType.toLowerCase(),
                        onItemClick: setSummaryType,
                        selected: e.field.summaryType === summaryTypeValue,
                        selected: e.field.format === "currency"
                    });
                });
            }
        }
    }



$(document).ready(function () {
    //cargando la perspectiva indicada en la url

    if (perspectiva != null) {
        document.getElementById('nombre').value = perspectiva;
        //cargando la perspectiva
        $("#cargar").click();

        //document.getElementById("cargar").click();

    }


});

